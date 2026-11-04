hide:
    - navigation

# Authentification Afendar

Cette section décrit le mécanisme d'authentification interne utilisé par les applications Afendar pour appeler l'API centrale.

## Objectifs

Le mécanisme permet de vérifier indépendamment :

- **l'application appelante** (`afendar-front`, `afendar-admin`, `afendar-bugs`) ;
- **l'utilisateur connecté**, au moyen d'un token de session interne ;
- **l'association entre le token et l'application** qui l'a créé.

Les secrets applicatifs et les tokens utilisateur sont transmis uniquement entre serveurs. Le navigateur ne reçoit pas le token interne.

## Périmètre

Ce mécanisme est distinct du serveur OAuth2 / OpenID Connect déjà présent dans Afendar-Games. Il ne remplace ni le flux Authorization Code + PKCE ni les endpoints OAuth2.

## Pages

- [Architecture générale](architecture.md)
- [Authentification des applications clientes](client-authentication.md)
- [Authentification utilisateur](user-authentication.md)
- [Cycle de vie des tokens](token-lifecycle.md)
- [Endpoints internes](api-endpoints.md)
- [Sécurité et exploitation](security.md)

## Paramètres principaux

| Paramètre | Valeur / règle |
|---|---|
| Durée de vie d'un token interne | 12 heures |
| Génération du token | `random_bytes(32)` encodé en hexadécimal |
| Stockage du token | Hash SHA-256 uniquement |
| Stockage du secret client | Hash produit par `password_hash()` |
| Transport du token utilisateur | `Authorization: Bearer <token>` |
| Identification du client | `Afendar-Client-Id` |
| Authentification du client | `Afendar-Client-Secret` |

> Les valeurs de configuration et les extraits de code doivent rester alignés sur le code réellement déployé. Les secrets réels ne doivent jamais être ajoutés à cette documentation.
