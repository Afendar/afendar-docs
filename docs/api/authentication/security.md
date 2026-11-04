hide:
    - navigation

# Sécurité et exploitation

## Transport

En production, toutes les communications entre les applications internes et l'API doivent utiliser HTTPS. Le mécanisme d'identifiants client est serveur-à-serveur : le secret ne doit jamais être envoyé au navigateur.

## Stockage

| Donnée | Stockage |
|---|---|
| Secret client | Hash `password_hash()` dans `internal_clients` |
| Token utilisateur | Hash SHA-256 dans `internal_access_tokens` |
| Token en clair | Session serveur du front uniquement après connexion |
| Secret de configuration | Variables d'environnement protégées / coffre de secrets |

Les fichiers `.env.local` contenant des secrets ne doivent pas être versionnés.

## Réponses HTTP

Le service `AfendarApi` lève une `AfendarApiException` pour les réponses non-2xx. Cette exception expose le statut HTTP et le corps de réponse.

Le traitement centralisé distingue notamment :

| Statut | Signification générale | Traitement front |
|---|---|---|
| `401` | Client ou token non valide | Invalidation de la session locale si un utilisateur est connecté ; redirection ou réponse JSON selon la requête |
| `403` | Accès interdit | Présentation d'une erreur d'autorisation |
| `404` | Ressource absente | Présentation d'une erreur de ressource |
| `500` | Erreur serveur | Gestion d'une erreur technique |

Le code applicatif doit éviter de présenter directement au navigateur des détails techniques provenant du corps d'une erreur API.

## Déconnexion et disponibilité de l'API

La déconnexion locale doit rester possible même si l'API est temporairement indisponible. Dans ce cas, l'appel de révocation peut échouer alors que la session locale est détruite. Il faut donc journaliser l'échec de révocation sans enregistrer le secret client ni le token Bearer.

Le token non révoqué restera néanmoins inutilisable après son expiration. Pour les besoins d'audit, surveiller les échecs de révocation et conserver une politique de durée de vie courte.

## Rotation et désactivation des clients

- Désactiver un client en mettant `isActive` à `false` bloque ses futures authentifications.
- La rotation d'un secret doit mettre à jour le hash en base et la configuration du service appelant de manière coordonnée.
- Les secrets doivent être uniques et générés avec un générateur cryptographiquement sûr.

## Points de contrôle opérationnels

- Vérifier que les routes internes ne sont pas accessibles sans identifiants client.
- Vérifier qu'un token de `afendar-front` est refusé avec `afendar-admin`.
- Vérifier qu'un token expiré ou révoqué reçoit `401`.
- Vérifier que la déconnexion renseigne `revokedAt`.
- Vérifier que les secrets et tokens sont absents des journaux, traces et outils de monitoring.
- Prévoir une politique de purge ou d'archivage des anciens tokens révoqués, en fonction des besoins d'audit.

## Distinction OAuth2 / OIDC

Le mécanisme décrit ici est interne aux applications Afendar. OAuth2 / OpenID Connect demeure un mécanisme séparé, avec ses propres clients, scopes, tokens et endpoints. Ne pas confondre les tokens internes de session avec les access tokens OAuth2.
