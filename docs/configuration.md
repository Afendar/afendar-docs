# Configuration

## Variables d'environnement

La configuration globale du projet est centralisée dans le fichier .env.

Exemple :

```
MYSQL_DATABASE=afendar
MYSQL_ROOT_PASSWORD=secret

MYSQL_PORT=3306

REDIS_PASSWORD=secret
REDIS_PORT=6379
```

!!! warning

    Les valeurs présentées ici sont uniquement des exemples.
    N'utilisez jamais les mots de passe de développement ou de production dans un repository Git.
    Démarrer l'environnement Docker

Depuis le dossier docker :

```bash
cd docker
docker compose up -d
```

Vérifiez que les différents services sont démarrés :

```
docker compose ps
```

Les principaux services sont :

|Service|	Rôle|
|---|---|
|mysql|	Base de données MySQL|
|redis|	Cache / stockage Redis|
|php-fpm|	Exécution PHP|
|node	|Environnement Node.js|
|web	|Serveur Nginx|
|api	|Nginx pour l'API|
|docs	|Documentation MkDocs|

## Accès aux applications

Une fois l'environnement démarré, les différentes applications sont accessibles avec les hosts locaux suivants :

| Application|	URL|
|---|---|
|API|	http://afendar-api.local|
|Administration|	http://afendar-admin.local:8080|
|Front|	http://afendar-front.local:8080|
|Bugs|	http://afendar-bugs.local:8080|
|Documentation|	http://afendar-docs.local:8080|

Pour utiliser ces domaines en local, ajoutez-les à votre fichier /etc/hosts :

```
127.0.0.1 afendar-api.local
127.0.0.1 afendar-admin.local
127.0.0.1 afendar-front.local
127.0.0.1 afendar-bugs.local
127.0.0.1 afendar-docs.local
```
