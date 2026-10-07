hide:
    - navigation

# Créer un bloc pour le front-office

## Généralités

Le type d'un bloc est de la forme : `{Name}`.

Un bloc est constitué de plusieurs fichiers :

- une classe déterminant son rendu, reprenant le nom du bloc, placée dans le dossier `src/Core/Presentation/Blocks/{Name}` et étendant `\App\Core\Presentation\Blocks\Block`
- une classe spécifiant ses paramètres, reprenant le nom du bloc suffixé par `Information`, elle aussi dans le dossier `src/Core/Presentation/Blocks/{Name}` et étendant `\App\Core\Presentation\Blocks\BlockInformation`
- un ou plusieurs templates des rendus dans le dossier `src/Core/Presentation/Blocks/{Name}/Assets`, nommés en *snake-case*

Le CLI propose une commande `afendar:dev:initialize-block` permettant d'initialiser les templates de vue relatifs à un modèle.

```bash
php bin/console afendar:dev:initialize-block MyBlock
```

Pour fonctionner, le bloc doit encore être enregistré sur le `BlockManager`. La commande indique la marche à suivre.

## La classe principale

Un bloc est destiné à rendre une portion d'HTML sur le site. En **aucun cas**, un bloc ne doit modifier la base de données

La classe principale se charge du rendu du bloc et contient essentiellement les trois méthodes suivantes.

### La méthode `parametrize()`

- agrège la configuration du bloc, des paramètres de requêtes, des paramètres de session, etc
- retourne un ensemble de paramètres scalaires (pas d'objets ou d'instances de modèles)
- transmis à la méthode `execute()`
- constitue la clé de cache du bloc

### La méthode `execute()`

- accède aux paramètres retournés par `parameterize()`
- ne doit en **aucun cas** faire appel à des paramètres de requête ou de session : tout doit être impérativement résolu dans `parameterize()`
- ne doit en **aucun cas** non plus modifier le contenu de la variable `parameters` car ces modifications ne seront pas restaurées lorsque le rendu du bloc est repris du cache
- peut interroger la base de données (mais en aucun cas y faire des mises à jour)
- remplit le tableau `$attributes` qui sera fourni au template
- les paramètres aussi sont transmis au template (dans la variable `parameters`), donc inutile de les recopier dans `$attributes`
- retourne un nom de template à rendre ou `null` (dans ce dernier cas, aucun HTML n'est rendu pour le bloc)
- on ne fournit jamais directement une instance d'un modèle au template mais plutôt le tableau résultant de l'appel de la méthode getAjaxData() (cf. API web)

## La classe information

La classe information définit deux choses :

- les paramètres du bloc qui pourront être renseignés en backoffice
- les templates alternatifs du bloc avec leurs paramètres propres s'ajoutant aux paramètres du bloc

L'ensemble se définit dans une unique méthode `onInformation()`.

La classe information étend `\App\Core\Presentation\Blocks\BlockInformation` qui fournit les méthodes suivantes :

- `setLabel()` : définit le libellé du bloc
- `addParameterInformation()` : retourne une instance de `\App\Core\Presentation\Blocks\ParameterInformation` représentant un nouveau paramètre du bloc
- `addDefaultTemplateInformation()` : retourne une instance de `\App\Core\Presentation\Blocks\TemplateInformation` représentant le template par défaut du bloc et permettant de lui ajouter des paramètres spécifiques qui ne seront pas répercutés sur les autres templates
- `addTemplateInformation()` : retourne une instance de `\App\Core\Presentation\Blocks\TemplateInformation` représentant un nouveau template alternatif du bloc
- `setDefaultTTL()` : définit la durée par défaut du cache (modifiable en backoffice)
- `disableCache()` : désactive le cache pour le bloc (positionne le TTL à -1, ce qui supprimera le champ en backoffice)

Dès lors qu'au moins un template alternatif a été déclaré sur le bloc, un sélecteur sera proposé en backoffice pour le choisir. Si un template est choisi de cette manière, il remplacera le template retourné par la méthode `execute()`, quel qu'il soit, sauf s'il vaut `null` auquel cas aucun template n'est rendu.

D'une manière générale, hors code projet, on prendra soin de bien séparer les paramètres qui servent à la préparation des données (que l'on associera au bloc) des paramètres affectant le rendu (à associer au template). Ceci afin d'éviter autant que possible d'avoir de nombreux paramètres dans l'éditeur de page qui ne seront finalement pas pris en compte dans le templates spécifique du projet.

### Types de paramètres

Les types de données pouvant être utilisés dans les paramètres de blocs sont les suivants :

|Nom|	Constante (code PHP)|	Nom technique (thèmes)|	Remarques |
|---|---|---|---|
|Booléen (oui/non)|	`\App\Core\Models\Property::TYPE_BOOLEAN`|	`Boolean`	||
|Nombre entier|	`\App\Core\Models\Property::TYPE_INTEGER`|	`Integer` ||
|Chaine de caractères < 255 caractères|	`\App\Core\Models\Property::TYPE_STRING`|	`String`||
|Chaine de caractères longue|	`\App\Core\Models\Property::TYPE_LONGSTRING`|	`LongString`||
|Texte riche|	`\App\Core\Models\Property::TYPE_RICHTEXT`|	`RichText`||
| Date|	`\App\Core\Presentation\Blocks\ParameterInformation::TYPE_DATE_STRING`|	`DateString`|	Le paramètre retournera **une chaine (ISO-8601)** et non une instance de `\DateTime`.|
||	`\App\Core\Models\Property::TYPE_DATE`|	`Date`|	*Alias de `DateString`*|
|Date et heure|	`\App\Core\Presentation\Blocks\ParameterInformation::TYPE_DATETIME_STRING`|	`DateTimeString`|	Le paramètre retournera **une chaine (ISO-8601)** et non une instance de `\DateTime`.|
||	`\App\Core\Models\Property::TYPE_DATETIME`|	`DateTime`|	*Alias de `DateTimeString`*|
|Identifiant de document	|`\App\Core\Models\Property::TYPE_MODELID`|	`ModelId`|	Le paramètre retournera **un identifiant** et non une instance du modèle.|
||	`\App\Core\Models\Property::TYPE_MODEL`|	`Model`|	*Alias de `ModelId`*|
|Tableau d'identifiants de modèles|	`\App\Core\Presentation\Blocks\ParameterInformation::TYPE_MODELID_ARRAY`|	`ModelIdArray`|	Le paramètre retournera **des identifiants** et non des instances des modèles.|
|| `\App\Core\Models\Property::TYPE_MODELARRAY`|	`ModelArray`|	*Alias de `ModelIdArray`*|

## Gestion du cache

Comme dit plus haut, la clé de cache est basée sur l'ensemble des paramètres retournés par la méthode `parameterize()`. Il est donc essentiel d'y effectuer toutes les récupérations d'information issues du contexte (requête, session, etc).

Par ailleurs le cache de bloc est basé sur le temps, sa durée étant modifiable en backoffice. Sa durée par défaut est d'une minute (valeur par défaut modifiable dans la classe information). Il n'y a pas d'autre invalidation du cache que la durée.

### Désactivation du cache

Pour forcer la désactivation du cache sur un bloc :

- dans l'information, appeler `disableCache()` (qui positionne le TTL à -1, ce qui supprimera le champ en backoffice)
- ndans le `parameterize()` appeler `$parameter->setNoCache()` après l'appel à `setLayoutParameters()` (qui force le passage à 0 du TTL)