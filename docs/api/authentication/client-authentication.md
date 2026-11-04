hide:
    - navigation

# Authentification des applications clientes

## Clients enregistrés

Chaque application interne dispose de ses propres identifiants :

| Client ID | Application |
|---|---|
| `afendar-front` | Interface utilisateur |
| `afendar-admin` | Administration |
| `afendar-bugs` | Gestion des anomalies |

Les identifiants sont enregistrés dans `internal_clients`. Le secret est stocké sous forme de hash, jamais en clair.

## Entité `InternalClient`

L'entité contient notamment :

- `clientId` : identifiant unique de l'application ;
- `clientSecretHash` : hash du secret ;
- `name` : nom lisible ;
- `isActive` : permet de désactiver un client ;
- `createdAt` : date de création.

Le repository expose une recherche du client actif par identifiant. Le service `InternalClientAuthenticator` vérifie ensuite le secret avec `password_verify()`.

## En-têtes HTTP

Chaque appel interne transmet :

```http
Afendar-Client-Id: afendar-front
Afendar-Client-Secret: <secret-de-l-application>
```

Le préfixe `X-` n'est pas utilisé pour ces champs personnalisés. Le token utilisateur utilise l'en-tête standard :

```http
Authorization: Bearer <token-utilisateur>
```

## Configuration des secrets

Les secrets de provisioning des clients sont fournis à l'API par variables d'environnement, par exemple :

```dotenv
AFENDAR_FRONT_CLIENT_SECRET=
AFENDAR_ADMIN_CLIENT_SECRET=
AFENDAR_BUGS_CLIENT_SECRET=
```

Les vraies valeurs sont définies dans `.env.local`, dans les secrets Symfony ou dans le gestionnaire de secrets de l'environnement de déploiement. Elles ne doivent pas être commitées.

Les fixtures créent les clients et hachent les secrets. La fixture décrite dans le projet ne remplace pas le secret d'un client déjà présent : une rotation de secret doit donc faire l'objet d'une opération dédiée.

## Ajouter une application

1. Générer un secret aléatoire fort.
2. Définir le secret dans l'environnement de l'application et dans l'environnement de provisioning de l'API.
3. Créer le client interne avec un `clientId` unique et le hash du secret.
4. Configurer le client HTTP de l'application pour transmettre les deux en-têtes.
5. Vérifier qu'un token émis pour cette application ne peut pas être utilisé par un autre client.

> Un secret client ne doit jamais être embarqué dans du JavaScript, une application mobile distribuée ou du code exécuté dans le navigateur. Ce mécanisme est réservé aux communications serveur-à-serveur.
