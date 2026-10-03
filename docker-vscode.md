WSL env:

User: afendar
PWD: c...z...2

### 1. Vérifie d'abord que host.docker.internal fonctionne

Exécute :

```cmd
docker exec -it php-fpm getent hosts host.docker.internal
```

Tu devrais obtenir une ligne ressemblant à :

```
172.xx.xx.xx    host.docker.internal
```

Si tu as bien une IP, Docker sait résoudre l'hôte sur lequel VS Code va écouter.

### 2. Côté VS Code

Dans VS Code, vérifie que tu as l'extension :

**PHP Debug** de Xdebug.

Si tu l'as déjà installée comme prévu, rien à faire.

Ensuite, ouvre **le dossier racine de ton environnement** dans VS Code, idéalement :

```
/home/afendar/Projects/Web
```

### 3. Configuration launch.json

Dans :

```
/home/afendar/Projects/Web/.vscode/launch.json
```

mets :

.vscode/launch.json
```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Xdebug : écouter",
            "type": "php",
            "request": "launch",
            "port": 9003,
            "log": true,
            "pathMappings": {
                "/var/www/afendar-admin": "${workspaceFolder}/afendar-admin",
                "/var/www/afendar-api": "${workspaceFolder}/afendar-api",
                "/var/www/afendar-front": "${workspaceFolder}/afendar-front",
                "/var/www/afendar-bugs": "${workspaceFolder}/afendar-bugs"
            }
        }
    ]
}
```

Pourquoi ces pathMappings ?
C'est probablement le point qui t'avait posé problème avec PhpStorm.

PHP dans Docker voit ton code ici :

```
/var/www/afendar-api
```

alors que VS Code voit exactement le même fichier ici :

```
/home/afendar/Projects/Web/afendar-api
```

Le mapping dit à VS Code :

```
Docker                         WSL
------------------------------------------------
/var/www/afendar-api     ->    ~/Projects/Web/afendar-api
/var/www/afendar-admin   ->    ~/Projects/Web/afendar-admin
/var/www/afendar-front   ->    ~/Projects/Web/afendar-front
/var/www/afendar-bugs    ->    ~/Projects/Web/afendar-bugs
```

C'est ce qui permettra à VS Code de comprendre qu'un breakpoint placé dans ton fichier local correspond au fichier exécuté par PHP-FPM.

### 4. Mais il reste une chose : le trigger

Ton Xdebug est configuré avec :

xdebug.start_with_request = trigger

Donc simplement cliquer sur "Écouter Xdebug" dans VS Code ne suffit pas forcément à déclencher Xdebug sur une requête HTTP.

Pour notre premier test, je te propose de faire plus simple : temporairement passer à :

xdebug.start_with_request = yes

On vérifie que toute la chaîne fonctionne :

Navigateur
   ↓
Nginx
   ↓
PHP-FPM
   ↓
Xdebug
   ↓
VS Code

Puis, une fois que le breakpoint fonctionne, on remettra :

xdebug.start_with_request = trigger

et on configurera le déclenchement uniquement quand tu souhaites debugger.

C'est une méthode de diagnostic beaucoup plus fiable.

On peut également utiliser le paramètre ?XDEBUG_TRIGGER=1 pour les appels Ajax.