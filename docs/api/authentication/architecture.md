hide:
    - navigation

# Architecture générale

## Composants

- **Navigateur** : communique avec Afendar Front au moyen d'une session Symfony.
- **Afendar Front (BFF)** : authentifie l'utilisateur auprès de l'API et conserve le token interne côté serveur dans l'objet utilisateur de la session Symfony.
- **Afendar API** : authentifie les applications clientes, valide les tokens utilisateur et fournit les données métier.
- **Base de données API** : conserve les clients internes et les tokens sous forme hachée.

## Vue d'ensemble

```mermaid
flowchart TD
    Browser["Navigateur"]
    Front["Afendar Front<br/>Session Symfony / BFF"]
    API["Afendar API"]
    Clients[("internal_clients")]
    Tokens[("internal_access_tokens")]
    Users[("Utilisateurs")]

    Browser <-->|"Cookie de session"| Front
    Front -->|"Afendar-Client-Id<br/>Afendar-Client-Secret<br/>Authorization: Bearer"| API
    API --> Clients
    API --> Tokens
    API --> Users
    Tokens -->|"lié à"| Clients
    Tokens -->|"lié à"| Users
```

## Deux contrôles indépendants

Chaque requête interne protégée doit présenter :

1. les identifiants d'une application cliente active ;
2. un token utilisateur valide ;
3. un token rattaché au même client que celui authentifié dans la requête.

La validation du client ne remplace donc pas la validation de l'utilisateur, et inversement.

## Flux de connexion

```mermaid
sequenceDiagram
    actor U as Utilisateur
    participant B as Navigateur
    participant F as Afendar Front
    participant A as Afendar API
    participant DB as Base API

    U->>B: Saisit identifiant et mot de passe
    B->>F: POST /login
    F->>A: POST /api/internal/authenticate<br/>identifiants utilisateur + identifiants client
    A->>DB: Vérifie le client actif et son secret
    A->>DB: Vérifie les identifiants utilisateur
    A->>DB: Enregistre le hash du token<br/>lié à l'utilisateur et au client
    A-->>F: access_token, token_type, expires_in, profil
    F->>F: Crée AuthenticatedUser<br/>et ouvre la session Symfony
    F-->>B: Réponse de connexion
    Note over B,F: Le token interne reste côté serveur
```

## Flux d'un appel protégé

```mermaid
sequenceDiagram
    participant F as Afendar Front
    participant A as Afendar API
    participant DB as Base API

    F->>A: GET /api/internal/me
    Note right of F: Afendar-Client-Id<br/>Afendar-Client-Secret<br/>Authorization: Bearer token
    A->>DB: Authentifie le client
    A->>DB: Recherche le hash du token
    A->>DB: Vérifie expiration et révocation
    A->>DB: Vérifie le rattachement au client
    alt Toutes les vérifications réussissent
        A-->>F: 200 + données utilisateur
    else Une vérification échoue
        A-->>F: 401
    end
```

## Front comme BFF

Le navigateur ne doit pas recevoir ni stocker le token interne. Il détient uniquement le cookie de session Symfony. Les appels à l'API sont effectués par le serveur Afendar Front, qui ajoute les identifiants client et le Bearer token.
