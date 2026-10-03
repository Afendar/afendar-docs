# Project installation

## install database and fixtures

```
php bin/console doctrine:migrations:migrate
```

puis:

```
php bin/console doctrine:fixtures:load --group=settings
php bin/console doctrine:fixtures:load --group=project --append
php bin/console doctrine:fixtures:load --group=workflow --append
php bin/console doctrine:fixtures:load --group=user --append
php bin/console doctrine:fixtures:load --group=blog --append
```
## Utilisation de NPM

Pour installaer les dépendances

```
docker compose exec node npm --prefix /var/www/afendar-admin ci
```

puis:

```
docker compose exec node npm --prefix /var/www/afendar-admin run dev
```

ou:

```
docker compose exec node npm --prefix /var/www/afendar-admin run build
```

## Utilisation de XDEBUG

Pour activer XDEBUG à la demande, il faut ajouter `?XDEBUG_TRIGGER=1` à la fin de la requête que l'on souhaite analyser