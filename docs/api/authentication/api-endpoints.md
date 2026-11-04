hide:
    - navigation

# Endpoints internes

Les endpoints ci-dessous sont réservés aux applications clientes enregistrées. Les chemins indiqués correspondent aux routes utilisées dans l'implémentation Afendar.

## `POST /api/internal/authenticate`

Authentifie une application et un utilisateur, puis crée un token interne lié aux deux.

En-têtes :

```http
Content-Type: application/json
Afendar-Client-Id: afendar-front
Afendar-Client-Secret: <secret-client>
```

Corps :

```json
{
  "login": "utilisateur@example.test",
  "password": "<mot-de-passe>"
}
```

Réponse de succès : données utilisateur, profil, `access_token`, `token_type` et `expires_in`.

Erreurs possibles :

- `401 invalid_client` : client absent, désactivé ou secret incorrect ;
- `401` d'authentification utilisateur : identifiants utilisateur invalides, selon le contrat du contrôleur.

## `GET /api/internal/me`

Retourne les informations de l'utilisateur associé au token.

En-têtes requis :

```http
Afendar-Client-Id: afendar-front
Afendar-Client-Secret: <secret-client>
Authorization: Bearer <token-interne>
```

Réponse de succès : identifiant, email, rôles, profil et informations du client.

## `POST /api/internal/logout`

Vérifie le client et le token, puis révoque le token correspondant.

En-têtes requis : les mêmes que pour `/api/internal/me`.

Réponse de succès :

```json
{
  "success": true,
  "message": "Session révoquée."
}
```

## Règles communes

- Les secrets client ne doivent jamais être écrits dans les logs.
- Le token Bearer ne doit jamais être écrit dans les logs.
- Un token ne peut être utilisé que par le client auquel il est rattaché.
- Les endpoints internes doivent être exposés uniquement sur un canal HTTPS en production et protégés par les contrôles réseau adaptés.
- Les réponses d'erreur doivent rester cohérentes avec les statuts HTTP.
