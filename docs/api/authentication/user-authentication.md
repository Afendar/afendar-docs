# Authentification utilisateur

## Connexion

Le navigateur envoie ses identifiants à Afendar Front. Le contrôleur de connexion du front appelle ensuite l'endpoint interne d'authentification de l'API avec :

- les identifiants de l'utilisateur ;
- `Afendar-Client-Id` ;
- `Afendar-Client-Secret`.

Après vérification, l'API crée un token interne et retourne notamment :

```json
{
  "access_token": "<token-interne>",
  "token_type": "Bearer",
  "expires_in": 43200,
  "id": 123,
  "email": "utilisateur@example.test",
  "roles": ["ROLE_USER"],
  "profile": {}
}
```

Les valeurs sont illustratives. `expires_in` correspond à 12 heures, soit 43 200 secondes.

## Session Symfony du front

Afendar Front construit un objet `AuthenticatedUser` à partir des données renvoyées par l'API, puis ouvre une session Symfony avec `Security::login()`.

Cet objet conserve les informations nécessaires à l'application, notamment le token interne. Le token est conservé côté serveur dans la session Symfony ; il n'est pas placé dans le stockage local du navigateur.

Le service `AfendarApi` utilise `Symfony\Bundle\SecurityBundle\Security` pour récupérer l'utilisateur courant et ajouter automatiquement le Bearer token aux appels effectués pendant une session authentifiée.

## Appel protégé

Exemple de requête :

```http
GET /api/internal/me HTTP/1.1
Host: afendar-api.local
Accept: application/json
Afendar-Client-Id: afendar-front
Afendar-Client-Secret: <secret-client>
Authorization: Bearer <token-interne>
```

L'API valide le client, le token, son état et son rattachement au client avant de retourner les informations utilisateur.

## Séparation avec OAuth2 / OpenID Connect

Le token interne décrit dans cette documentation est un mécanisme de session applicatif propre à Afendar. Il ne s'agit pas d'un access token OAuth2.

Le flux OAuth2 Authorization Code avec PKCE et les endpoints OIDC restent indépendants. L'endpoint de connexion interne ne doit pas émettre ni remplacer les tokens OAuth2.
