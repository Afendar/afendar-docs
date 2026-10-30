Projet inspiré de https://github.com/intportg/Change

# Architecture Content / Page Builder / Publication

- **Version**: 5.0**
- **Statut**: Proposition validée pour implémentation
- **Date**: 09 février 2025

---

## 1.Objectif

Cette architecture définit le fonctionnement global du système de gestion de contenu, du Page Builder, des corrections, des versions, de la validation, de la publication, du cache Redis et du rendu public.

L'objectif principal est de séparer clairement :

- les données métier ;
- la configuration de présentation ;
- le workflow éditorial ;
- les corrections ;
- l'historique et les changements ;
- la publication ;
- le cache ;
- le rendu public.
  
Le système doit permettre de modifier un contenu sans modifier immédiatement le contenu public.

Une modification suit donc généralement le cycle :

ÉDITION ↓ DRAFT ↓ VALIDATION ↓ VALIDCONTENT ↓ VALID ↓ PUBLISHABLE ↓ PUBLICATION ↓ PUBLISHED

Le workflow existant reste responsable de l'état du contenu.

Le stockage et la présentation du contenu sont traités par les composants dédiés décrits dans cette documentation.

## 2.Architecture générale

TODO Schema

## 3.Responsabilités des applications

### 3.1 Admin

L'Admin est une application cliente de l'API.

Il ne doit :

- pas accéder directement à MySQL ;
- pas accéder directement à Redis ;
- pas contenir la logique métier de publication ;
- pas décider si une transition de workflow est autorisée ;
- pas gérer lui-même la persistance définitive.

L'Admin est responsable principalement de :

- l'interface d'administration ;
- l'édition du Page Builder ;
- la manipulation des blocs ;
- la configuration des blocs ;
- l'affichage des erreurs de validation ;
- l'affichage des différences ;
- la prévisualisation ;
- les interactions utilisateur.

Toutes les opérations métier passent par l'API.

### 3.2 API

L'API est le cœur du système.

Elle est responsable de :

- la logique métier ;
- la validation ;
- la persistance ;
- le workflow ;
- les corrections ;
- les versions ;
- l'historique ;
- la publication ;
- l'invalidation du cache ;
- la génération du contenu public ;
- la gestion des previews ;
- l'exposition des données au Front et à l'Admin.

L'API est la seule application autorisée à communiquer directement avec MySQL et Redis.

### 3.3 Front

Le Front est responsable du rendu public.

Il ne doit pas :

- accéder directement à MySQL ;
- modifier les données ;
- appliquer les règles de workflow ;
- décider si un contenu est publiable.

Le Front consomme une représentation publique fournie par l'API.

Le rendu doit utiliser le même moteur de présentation pour :

- le contenu publié ;
- le preview.

Cela évite d'avoir deux systèmes de rendu différents.

### 3.4 Redis

Redis est une couche de cache.

Redis n'est jamais la source de vérité.

La source de vérité est MySQL.

MySQL
  │
  │ publication
  ▼
Redis
  │
  ▼
Front

Une perte totale de Redis doit être récupérable à partir de MySQL.

## 4. Source de vérité

La règle fondamentale est :

> MySQL contient l'état persistant et Redis contient une projection/cache de cet état.

Il ne faut donc jamais considérer Redis comme le stockage définitif d'un contenu.

Exemple :

Modification Admin
       ↓
API
       ↓
MySQL
       ↓
Publication
       ↓
Redis

En cas de suppression d'une entrée Redis :

Redis
  ↓
cache miss
  ↓
API
  ↓
MySQL
  ↓
reconstruction du cache

## 5. Entité Project

L'entité `Project` conserve ses données métier existantes.

Elle reçoit également les informations nécessaires au Page Builder.

Exemple conceptuel :

```php
class Project
{
    private string $label;

    private ?string $description;

    private ?string $pageTemplate;

    private array $editableContent = [];

    private bool $useCache = false;

    private int $cacheTTL = 0;
}
```

Les noms exacts des propriétés devront respecter les conventions déjà présentes dans le projet.

### 5.1 pageTemplate

`pageTemplate` définit le template de présentation utilisé pour afficher le contenu.

Exemple :

default

ou :

project

ou :

project-sidebar

Le template ne doit pas contenir les données éditoriales elles-mêmes.

Il définit uniquement la structure globale de rendu.

## 6. editableContent

`editableContent` contient le document du Page Builder.

Il est stocké sous forme JSON.

Exemple :

```json
{
  "schema": 1,
  "zones": {
    "main": {
      "type": "container",
      "items": [
        {
          "id": "a12",
          "type": "project.description"
        }
      ]
    }
  }
}
```

Le JSON est versionné via :

```JSON
{
  "schema": 1
}
```

Le champ schema permet de faire évoluer la structure sans casser les anciennes pages.

## 7.Pourquoi le Page Builder est stocké en JSON

Le Page Builder est une structure fortement orientée présentation.

Une normalisation complète en tables Doctrine conduirait à multiplier les entités :

Page
Container
Row
Cell
Block
BlockStyle
BlockVisibility
BlockCondition
...

Cette approche augmenterait fortement la complexité.

Le choix retenu est donc :

Document Page Builder
        ↓
      JSON
        ↓
    MySQL JSON

Le JSON est manipulé côté Vue et validé côté API.

## 8. Structure du document Page Builder

Structure générale :

```JSON
{
  "schema": 1,
  "zones": {
    "main": {
      "type": "container",
      "items": []
    }
  }
}
```JSON

Un bloc peut contenir :

```JSON
{
  "id": "a12",
  "type": "project.description",
  "style": {
    "classes": [
      "highlight",
      "rounded"
    ]
  },
  "cache": {
    "mode": "custom",
    "ttl": 600
  },
  "visibility": {
    "xs": true,
    "sm": true,
    "md": true,
    "lg": false
  },
  "conditions": {
    "operator": "AND",
    "rules": [
      {
        "field": "user.authenticated",
        "operator": "equals",
        "value": true
      }
    ]
  }
}
```

## 9. Identité d'un bloc

Chaque bloc possède un identifiant unique dans le document :

```JSON
{
  "id": "a12"
}
```

Cet identifiant est important pour :

- le diff ;
- l'historique ;
- les modifications ;
- les déplacements ;
- les suppressions ;
- les restaurations.

Le type identifie le type fonctionnel du bloc :

```JSON
{
  "type": "project.description"
}
```

## 10. Catalogue des blocs

Le nom du bloc ne doit pas être considéré comme une information éditoriale libre.

Il provient d'un catalogue de blocs connu de l'application.

Exemple :

project.description
project.images
project.price
project.reviews
project.download
project.categories

Le catalogue doit permettre à l'Admin de connaître :

- le nom ;
- le label ;
- la description ;
- les paramètres disponibles ;
- les règles de validation ;
- éventuellement les capacités du bloc.

Le label affiché dans l'interface n'a donc pas besoin d'être stocké dans chaque document.

Exemple :

```JSON
{
  "type": "project.description"
}
```

et non :

```JSON
{
  "type": "project.description",
  "label": "Description du projet"
}
```

## 11. Styles CSS

Chaque bloc peut définir des classes CSS.

Exemple :

```JSON
{
  "style": {
    "classes": [
      "highlight",
      "rounded"
    ]
  }
}
```

Le Page Builder ne doit pas générer arbitrairement du CSS.

Il référence des classes connues du système.

Cela permet :

- de garder le contrôle du design ;
- d'éviter l'injection de CSS arbitraire ;
- de conserver une cohérence avec le Front.

## 12. Cache au niveau du Project

Le Project dispose de :

useCache
cacheTTL

Exemple :

useCache = true
cacheTTL = 3600

Cela signifie que la représentation publique peut être mise en cache pendant 3600 secondes.

Valeur :

0

signifie qu'aucun cache n'est utilisé.

## 13. Cache au niveau du bloc

Chaque bloc peut également définir sa politique de cache.

La structure recommandée est :

```JSON
{
  "cache": {
    "mode": "inherit"
  }
}
```

ou :

```JSON
{
  "cache": {
    "mode": "none"
  }
}
```

ou :

```JSON
{
  "cache": {
    "mode": "custom",
    "ttl": 600
  }
}
```

Les trois modes sont :

inherit

Le bloc utilise la politique de cache du contexte parent.

none

Le bloc n'est jamais mis en cache.

custom

Le bloc possède son propre TTL.

## 14. Cache page et cache bloc

Il faut distinguer deux niveaux :

Page cache
    │
    └── cache global du rendu

Block cache
    │
    └── cache d'une partie du rendu

Les deux systèmes doivent rester indépendants dans le modèle.

La stratégie exacte de composition pourra être centralisée dans le CacheService.

Exemple de principe :

Project cacheTTL = 3600
Block cacheTTL   = 600

effective TTL = règle définie par CacheService

Aucune logique de calcul de TTL ne doit être dupliquée dans Vue ou dans les templates.

## 15. Responsive visibility

La visibilité responsive utilise des clés sémantiques.

```JSON
{
  "visibility": {
    "xs": true,
    "sm": true,
    "md": true,
    "lg": false
  }
}
```

Les valeurs sont centralisées par l'application.

Exemple :

xs : < 768px
sm : >= 768px
md : >= 992px
lg : >= 1200px

Ces valeurs ne doivent pas être répétées dans chaque bloc.

Le Front possède la définition des breakpoints.

## 16. Conditions d'affichage

Un bloc peut posséder des conditions dynamiques.

Exemple :

```JSON
{
  "conditions": {
    "operator": "AND",
    "rules": [
      {
        "field": "user.authenticated",
        "operator": "equals",
        "value": true
      }
    ]
  }
}
```

L'objectif est de ne pas coder en dur les conditions dans le Page Builder.

Exemples futurs :

user.authenticated
user.role
project.category
project.status
request.locale
request.device

L'API pourra exposer le catalogue disponible :

GET /api/page-builder/conditions

L'Admin construit alors son interface dynamiquement.

## 17. Validation du Page Builder

Le JSON provenant de l'Admin n'est jamais considéré comme fiable.

L'API doit valider :

- le schema ;
- les zones ;
- les types de blocs ;
- les identifiants ;
- les paramètres ;
- les styles ;
- les règles de visibilité ;
- les conditions ;
- les paramètres de cache.

Le flux est :

Admin
  ↓
JSON
  ↓
API
  ↓
Validation
  ├── erreur → HTTP 400
  │
  └── valide
        ↓
      persist

## 18. Workflow

Le workflow existant est conservé.

Les états principaux sont :

DRAFT
VALIDATION
VALIDCONTENT
VALID
PUBLISHABLE
PUBLISHED
UNPUBLISHABLE
FROZEN
FILED

Le Page Builder ne remplace pas le workflow.

Le workflow décide si une transition est autorisée.

## 19. Séparation entre contenu et workflow

Il faut distinguer :

Content
   ↓
Project / editableContent

Workflow
   ↓
État éditorial

Le workflow ne doit pas connaître les détails internes du JSON Page Builder.

Inversement, le Page Builder ne doit pas reproduire les règles du workflow.

## 20. Correction

Une correction représente une modification préparée sur une entité existante.

Table proposée :

entity_correction

Structure :

correction_id     BIGINT PK
entity_type       VARCHAR(100)
entity_id         BIGINT
lcid              BIGINT NULL
status            VARCHAR(50)
created_at        DATETIME
published_at      DATETIME NULL
base_revision     BIGINT NULL
data              JSON

Éventuellement :

created_by
published_by

pour l'audit.

## 21. Pourquoi entity_type est obligatoire

Un simple :

entity_id = 123

ne suffit pas.

Le 123 peut correspondre à :

Project #123
Category #123
User #123
...

Il faut donc :

entity_type = Project
entity_id   = 123

Cela permet d'identifier précisément la cible.

## 22. Base revision

Une correction doit idéalement indiquer sur quelle version elle a été créée.

Exemple :

Project #123
Revision 42
       ↓
création correction
       ↓
base_revision = 42

Si quelqu'un modifie le Project avant publication :

Project #123
Revision 43

l'API peut détecter :

correction basée sur 42
contenu actuel basé sur 43

et déclencher une gestion de conflit.

## 23. Conflits

Le système doit éviter d'écraser silencieusement les modifications concurrentes.

Exemple :

Utilisateur A
    ↓
Revision 42
    ↓
modification prix

Utilisateur B
    ↓
Revision 42
    ↓
modification description

Les deux modifications peuvent potentiellement être fusionnées.

À l'inverse :

A : prix = 20
B : prix = 25

constitue un conflit.

La stratégie de résolution sera idéalement basée sur un diff sémantique.

## 24. Historique

Les corrections et l'historique sont deux concepts différents.

Correction

Modification actuellement en préparation.

Historique

Trace de ce qui s'est passé.

L'historique est conservé même après publication.

## 25. EntityChange / History

Une table générique peut être utilisée :

entity_change

Structure :

id
entity_type
entity_id
user_id
created_at
operation
changes

Exemple :

```JSON
{
  "changes": [
    {
      "path": "price",
      "old": 19.99,
      "new": 24.99
    },
    {
      "path": "pageTemplate",
      "old": "default",
      "new": "sidebar"
    }
  ]
}
```

## 26. Diff

Le diff doit exister à deux moments.

Avant sauvegarde

Comparer :

état original
     VS
état actuellement édité

afin de présenter à l'utilisateur ce qui va être sauvegardé.

Après sauvegarde

Le changement est conservé dans l'historique.

## 27. Diff Page Builder

Le diff du Page Builder doit être sémantique.

Il ne faut pas simplement afficher :

{
- "foo": "bar"
+ "foo": "baz"
}

mais plutôt :

Bloc "Description"

Modification :
    Cache
        Aucun
        ↓
        10 minutes

Modification :
    CSS
        + rounded

Modification :
    Visibilité
        lg : visible
        ↓
        lg : masqué

Pour les structures complexes :

Bloc ajouté
Bloc supprimé
Bloc déplacé
Bloc modifié

## 28. Restauration

Une restauration ne doit pas immédiatement modifier la version publiée.

Flux :

Historique
    ↓
Restaurer
    ↓
nouveau draft
    ↓
diff
    ↓
validation
    ↓
workflow
    ↓
publication

Cela évite qu'une restauration contourne les règles éditoriales.

## 29. Publication

La publication est une opération métier explicite.

Elle doit :

1. vérifier l'état workflow ;
2. vérifier que le contenu est publiable ;
3. valider le contenu ;
4. persister l'état publié ;
5. invalider le cache ;
6. éventuellement reconstruire le cache ;
7. enregistrer l'historique.

Conceptuellement :

PUBLISHABLE
     ↓
PublicationService
     ↓
MySQL
     ↓
Invalidate Redis
     ↓
Rebuild Redis
     ↓
PUBLISHED

## 30. Publication et Redis

Redis ne doit jamais être mis à jour avant que la persistance MySQL soit confirmée.

Ordre :

1. Validation
2. Transaction MySQL
3. Commit
4. Invalidation Redis
5. Reconstruction éventuelle

Jamais :

Redis
  ↓
MySQL

comme source principale.

## 31. Transaction de publication

La publication doit être pensée comme une opération transactionnelle.

Exemple :

BEGIN TRANSACTION

  modifier contenu publié
  enregistrer revision
  enregistrer historique
  modifier état workflow

COMMIT

invalidate cache
rebuild cache

Si MySQL échoue :

ROLLBACK

Redis ne doit alors pas être modifié.

## 32. Preview

Le preview doit utiliser le même moteur de rendu que le Front.

Architecture :

ADMIN
  │
  │ demande preview
  ▼
API
  │
  ├── crée token temporaire
  │
  └── associe token au draft
  │
  ▼
FRONT /preview/...
  │
  ▼
API
  │
  ▼
draft
  │
  ▼
renderer

## 33. Token de preview

Le preview doit être protégé.

Le token doit être :

- temporaire ;
- non prédictible ;
- limité au contenu concerné ;
- idéalement lié à l'utilisateur ou à la session ;
- invalidable.

Exemple :

previewToken
    ↓
Project #123
Draft revision #44
Expiration

Le Front peut alors afficher :

https://front/.../preview/xxxxxxxx

## 34. Preview et publication

Le preview ne doit jamais modifier le contenu public.

Draft
  ↓
Preview
  ↓
Renderer

et non :

Draft
  ↓
Publication

Le preview peut donc afficher une version qui n'est pas encore `PUBLISHED`.

## 35. Rendu public

Le Front doit demander une représentation publique.

Conceptuellement :

GET /api/projects/123

L'API ne devrait idéalement pas exposer directement une entité Doctrine.

Elle doit retourner un DTO ou une représentation publique.

Exemple :

```JSON
{
  "id": 123,
  "label": "My Project",
  "template": "project",
  "content": {
    "zones": {}
  }
}
```

## 36. Doctrine

Les entités Doctrine restent internes à l'API.

Il faut éviter :

Doctrine Entity
       ↓
JSON automatique
       ↓
Front

Préférer :

Doctrine Entity
       ↓
Mapper / Transformer
       ↓
DTO
       ↓
JSON

Cela permet de contrôler précisément le contrat API.

## 37. Architecture API recommandée

Organisation conceptuelle :

src/
├── Entity/
├── Repository/
├── Controller/
├── Service/
│   ├── Publication/
│   ├── PageBuilder/
│   ├── Preview/
│   ├── Cache/
│   ├── Correction/
│   └── History/
├── Workflow/
├── DTO/
├── Validator/
└── Serializer/

Cette organisation reste à adapter à l'organisation actuelle du projet.

L'objectif n'est pas de déplacer artificiellement tout le code existant.

## 38. Services principaux

### PageBuilderService

Responsable du document Page Builder :

validate()
normalize()
save()

### PublicationService

Responsable de :

canPublish()
publish()
unpublish()
invalidateCache()

### PreviewService

Responsable de :

createToken()
validateToken()
getPreview()
invalidateToken()

### CacheService

Responsable de :

get()
set()
delete()
invalidate()
rebuild()

### CorrectionService

Responsable de :

create()
get()
validate()
publish()
cancel()

### ChangeSetService

Responsable de :

diff()
record()
format()
restore()

## 39. API Page Builder

Les endpoints exacts dépendront de l'API existante.

Conceptuellement :

GET /api/page-builder/blocks

Retourne le catalogue des blocs.

GET /api/page-builder/conditions

Retourne les conditions disponibles.

GET /api/projects/{id}/page-builder

Retourne le document éditable.

PUT /api/projects/{id}/page-builder

Enregistre une modification.

POST /api/projects/{id}/preview

Crée une session de preview.

## 40. Sauvegarde

Une sauvegarde suit :

Admin
  ↓
PUT
  ↓
API
  ↓
Authentication
  ↓
Authorization
  ↓
Validation JSON
  ↓
Conflict detection
  ↓
Diff
  ↓
MySQL
  ↓
Revision
  ↓
History

Le cache public n'est pas nécessairement modifié à ce stade.

## 41. Pourquoi le cache n'est pas modifié au simple save

Une modification en DRAFT ne doit pas devenir publique.

Exemple :

Admin modifie prix
        ↓
DRAFT
        ↓
save
        ↓
MySQL

Redis public reste inchangé.

Ce n'est qu'au moment de la publication que :

DRAFT
  ↓
PUBLISHED
  ↓
Redis invalidation/rebuild

est effectué.

## 43. Sécurité

Toutes les opérations sensibles sont contrôlées côté API.

L'Admin ne doit jamais être considéré comme une source de confiance.

Contrôles minimum :

Authentication
Authorization
Validation
Workflow authorization
Entity ownership / permissions
Preview token validation
Input sanitization

Les permissions doivent être déterminées côté API.

## 44. Versionnement

Le système doit distinguer :

schema version

et :

content revision

Exemple :

```JSON
{
  "schema": 1
}
```

indique la version du format Page Builder.

Une revision :

Project #123
Revision #42

indique une version particulière du contenu.

Ce sont deux concepts différents.

## 45. Migration du schema Page Builder

Lorsqu'un changement structurel intervient :

schema 1
   ↓
migration
   ↓
schema 2

L'API doit idéalement être capable de migrer les anciennes structures.

Exemple :

Page Builder schema 1
       ↓
PageBuilderMigration
       ↓
schema 2

Les migrations doivent être déterministes.

## 46. Observabilité

Les opérations importantes doivent être traçables.

À minima :

save
validation
workflow transition
publication
unpublication
preview creation
correction creation
correction publication
cache invalidation

Les logs doivent permettre de retrouver :

quoi ?
qui ?
quand ?
sur quelle entité ?
quelle revision ?
quel résultat ?

## 47. Principes d'architecture

- Règle 1: MySQL est la source de vérité.
- Règle 2: Redis est un cache/projection.
- Règle 3: L'API est la seule couche métier centrale.
- Règle 4: Admin et Front ne communiquent pas directement avec MySQL.
- Règle 5: Le workflow reste indépendant du Page Builder.
- Règle 6: Un draft n'est jamais public par défaut.
- Règle 7: La publication déclenche la mise à jour du cache public.
- Règle 8: Le preview utilise le même moteur de rendu que le public.
- Règle 9: Toute modification importante est historisée.
- Règle 10: Une restauration crée un nouveau draft.
- Règle 11: Les corrections détectent les conflits de version.
- Règle 12: Le JSON Page Builder est versionné.

## 48. Résumé des responsabilités

Composant	Responsabilité
Admin	Édition
API	Métier
Workflow	États et transitions
MySQL	Source de vérité
Redis	Cache
PageBuilderService	Document Page Builder
PublicationService	Publication
PreviewService	Prévisualisation
CorrectionService	Corrections
ChangeSetService	Diff / historique
Front	Rendu public

## 49 Flux de données final

Édition
Admin
 ↓
API
 ↓
MySQL
Preview
Admin
 ↓
API
 ↓
Preview Token
 ↓
Front
 ↓
API
 ↓
Draft
Publication
Admin
 ↓
API
 ↓
Workflow
 ↓
MySQL
 ↓
Redis
Public
Front
 ↓
API
 ↓
Redis
 ↓
cache hit

ou :

Front
 ↓
API
 ↓
Redis
 ↓
cache miss
 ↓
MySQL
 ↓
Redis
 ↓
Front

## 50. Évolution future

Cette architecture doit permettre ultérieurement d'ajouter :

- plusieurs templates ;
- davantage de blocs ;
- des blocs personnalisés ;
- des règles de visibilité avancées ;
- des conditions complexes ;
- des variantes de contenu ;
- du multilingue ;
- du A/B testing ;
- des publications planifiées ;
- des versions multiples ;
- une restauration avancée ;
- des permissions par zone ;
- des permissions par bloc ;
- une invalidation de cache ciblée.

Ces fonctionnalités ne doivent cependant pas être implémentées prématurément.

L'architecture actuelle doit d'abord fournir un socle propre et stable.

## 51. Roadmap d'implémentation

L'ordre recommandé est :

### Phase 1 — Modèle de données
- Ajouter pageTemplate
- Ajouter editableContent
- Ajouter useCache
- Ajouter cacheTTL
- Créer entity_correction
- Préparer le système de revision/history
### Phase 2 — Page Builder API
- validation du document ;
- catalogue des blocs ;
- catalogue des conditions ;
- sauvegarde ;
- gestion des revisions.
### Phase 3 — Admin
- branchement du Page Builder sur l'API ;
- édition ;
- cache ;
- responsive visibility ;
- conditions ;
- sauvegarde.
### Phase 4 — Diff
- snapshot initial ;
- comparaison ;
- affichage ;
- historique ;
- restauration.
### Phase 5 — Preview
- token ;
- endpoint preview ;
- rendu Front avec draft.
### Phase 6 — Publication
- intégration workflow ;
- PublicationService ;
- invalidation Redis ;
- reconstruction cache.
### Phase 7 — Front
- DTO public ;
- renderer Page Builder ;
- templates ;
- blocs ;
- règles responsive ;
- conditions.
### Phase 8 — Corrections avancées
- base revision ;
- conflits ;
- fusion ;
- historique complet.

## 52. Critère de réussite

L'architecture sera considérée comme fonctionnelle lorsque le scénario suivant sera entièrement possible :

1. Un administrateur ouvre un Project.

2. Il modifie le Page Builder.

3. Il déplace un bloc.

4. Il modifie ses classes CSS.

5. Il modifie son TTL.

6. Il modifie sa visibilité responsive.

7. Il ajoute une condition.

8. L'Admin affiche le diff.

9. L'Admin sauvegarde.

10. Le Project reste non publié.

11. L'Admin demande un preview.

12. Le Front affiche exactement la version draft.

13. Le workflow fait progresser le contenu.

14. Le contenu devient publiable.

15. L'utilisateur publie.

16. MySQL devient la nouvelle référence publiée.

17. Redis est invalidé/reconstruit.

18. Le Front public affiche la nouvelle version.

19. L'historique conserve le changement.

20. Une restauration peut créer un nouveau draft
    sans modifier immédiatement le contenu public.

## 53. Conclusion

L'architecture repose sur une séparation claire entre :

Données métier
      +
Page Builder
      +
Workflow
      +
Corrections
      +
Historique
      +
Publication
      +
Cache
      +
Rendu

Le principe central est :



MySQL conserve la vérité.
Le workflow contrôle le cycle de vie.
Le Page Builder décrit la présentation.
L'historique explique les changements.
Redis accélère l'accès.
Le Front ne fait que rendre.