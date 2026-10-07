hide:
    - navigation

# Mise en forme

## Template de mail

Les templates de mails sont identiques aux templates de pages à la nuance près que le fichier JSON de déclaration doit contenir `"mailSuitable": true`.

Cette propriété discrimine les templates utilisables en tant que mail et celles utilisables en tant que page.

Voir `Assets/Templates/mail.json`.

## Bloc de mail

Tout comme une page, il est possible de créer un bloc destiné aux mails.

Pour rappel, un bloc est soit destiné aux pages soit aux mails.

Pour cela il suffit d'ajouter dans la méthode `onInformation` de la classe `MonBlockMailInformation` :

```php
$this->setMailSuitable(true);
```

Dans l'exécution du bloc, il sera possible de récupérer toutes les substitutions configurées sur le mail :

```php
$substitutions = $event->getParam('substitutions');
```