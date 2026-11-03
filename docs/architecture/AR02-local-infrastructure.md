hide:
    - navigation

# Inventaire de l’infrastructure locale

> Généré automatiquement le **2026-11-03 12:46:23 +0100** sur **LAPTOP-8DCOORLE**.

!!! warning "Portée de cet inventaire"
    Cet export décrit l’environnement observé au moment de l’exécution. Il ne remplace pas
    une sauvegarde, un audit de sécurité ni la validation des versions et paramètres de production.


## 1. Environnement hôte

- Distribution : **Ubuntu 22.04.3 LTS**
- Noyau : `6.18.54.1-microsoft-standard-WSL2`
- Architecture : `x86_64`
- Utilisateur : `afendar`

## 2. Environnement Docker

- Docker : `Docker version 24.0.6, build ed223bc`
- Compose : `Docker Compose version v2.21.0`
- Contexte Docker : `default`

## 3. Vue d’ensemble des conteneurs

| Nom | Image | Statut | Ports |
|---|---|---|---|
| api | `nginx:1.27-alpine` | Up About an hour | 0.0.0.0:80->80/tcp, :::80->80/tcp |
| web | `nginx:1.27-alpine` | Up About an hour | 80/tcp, 0.0.0.0:8080->8080/tcp, :::8080->8080/tcp |
| php-fpm | `docker-php-fpm` | Up About an hour | 9000/tcp |
| node | `node:20-alpine` | Up About an hour |  |
| docs | `squidfunk/mkdocs-material:latest` | Up About an hour | 8000/tcp |
| mysql | `mysql:8.0.34` | Up About an hour | 0.0.0.0:3306->3306/tcp, :::3306->3306/tcp, 33060/tcp |
| redis | `redis:7-alpine` | Up About an hour | 0.0.0.0:6379->6379/tcp, :::6379->6379/tcp |

## 4. Services


### 4.5 — api

- Image : `nginx:1.27-alpine`
- ID conteneur : `dddb1bd0ce96`
- En cours d’exécution : **true**
- Image ID : `sha256:6769dc3a703c719c1d2756bda113659be28ae16cf0da58dd5fd823d6b9a050ea`
- Plateforme : `linux/amd64`

#### Configuration Docker
| Élément | Valeur |
|---|---|
| Redémarrage | unless-stopped |
| Réseau(x) | docker_default  |
| Utilisateur conteneur |  |

#### Variables d’environnement (noms uniquement)
Les valeurs ne sont volontairement jamais exportées.

| Variable | Valeur exportée |
|---|---|
| `DYNPKG_RELEASE` | `[MASQUÉE]` |
| `NGINX_VERSION` | `[MASQUÉE]` |
| `NJS_RELEASE` | `[MASQUÉE]` |
| `NJS_VERSION` | `[MASQUÉE]` |
| `PATH` | `[MASQUÉE]` |
| `PKG_RELEASE` | `[MASQUÉE]` |

#### Ports, réseaux et montages
**Ports :**
```text
80/tcp -> 0.0.0.0:80
80/tcp -> [::]:80
```
**Réseaux et adresses :**
```text
docker_default : IP=172.18.0.4, aliases=[api api dddb1bd0ce96]
```
**Montages :**

| Type | Source | Destination | Lecture seule |
|---|---|---|---|
| bind | `/home/afendar/Projects/Web/afendar-games/docker/nginx/afendar-api.local.conf` | `/etc/nginx/conf.d/afendar-api.local.conf` | false |
| bind | `/home/afendar/Projects/Web/afendar-games/afendar-api` | `/var/www/afendar-api` | false |
|  | `` | `` |  |

#### Système et paquets
```text
ID=alpine
VERSION_ID=3.21.3
PRETTY_NAME="Alpine Linux v3.21"
```
<details><summary>Liste des paquets installés (déplier)</summary>

```text
alpine-baselayout-3.6.8-r1
alpine-baselayout-data-3.6.8-r1
alpine-keys-2.5-r0
alpine-release-3.21.3-r0
aom-libs-3.11.0-r0
apk-tools-2.14.6-r3
brotli-libs-1.1.0-r2
busybox-1.37.0-r12
busybox-binsh-1.37.0-r12
c-ares-1.34.5-r0
ca-certificates-20241121-r1
ca-certificates-bundle-20241121-r1
curl-8.12.1-r1
fontconfig-2.15.0-r1
freetype-2.13.3-r0
geoip-1.6.12-r5
gettext-envsubst-0.22.5-r0
libavif-1.0.4-r0
libbsd-0.12.2-r0
libbz2-1.0.8-r6
libcrypto3-3.3.3-r0
libcurl-8.12.1-r1
libdav1d-1.5.0-r0
libedit-20240808.3.1-r0
libexpat-2.7.0-r0
libgcrypt-1.10.3-r1
libgd-2.3.3-r9
libgpg-error-1.51-r0
libice-1.1.1-r6
libidn2-2.3.7-r0
libintl-0.22.5-r0
libjpeg-turbo-3.0.4-r0
libmd-1.1.0-r0
libncursesw-6.5_p20241006-r3
libpng-1.6.47-r0
libpsl-0.21.5-r3
libsharpyuv-1.4.0-r0
libsm-1.2.4-r4
libssl3-3.3.3-r0
libunistring-1.2-r0
libuuid-2.40.4-r1
libwebp-1.4.0-r0
libx11-1.8.10-r0
libxau-1.0.11-r4
libxcb-1.16.1-r0
libxdmcp-1.1.5-r1
libxext-1.3.6-r2
libxml2-2.13.4-r5
libxpm-3.5.17-r0
libxslt-1.1.42-r2
libxt-1.3.1-r0
musl-1.2.5-r9
musl-utils-1.2.5-r9
ncurses-terminfo-base-6.5_p20241006-r3
nghttp2-libs-1.64.0-r0
nginx-1.27.5-r1
nginx-module-geoip-1.27.5-r1
nginx-module-image-filter-1.27.5-r1
nginx-module-njs-1.27.5.0.8.10-r1
nginx-module-xslt-1.27.5-r1
pcre2-10.43-r0
scanelf-1.3.8-r1
ssl_client-1.37.0-r12
tiff-4.7.0-r0
tzdata-2025b-r0
xz-libs-5.6.3-r1
zlib-1.3.1-r2
zstd-libs-1.5.6-r2
```
</details>

#### NGINX
```text
nginx version: nginx/1.27.5
```
**Modules chargés :**
```text
Aucun module dynamique déclaré (modules probablement intégrés au binaire).
```
**VirtualHosts :**
```text

# configuration file /etc/nginx/conf.d/afendar-api.local.conf:
server {
	listen 80;
	server_name afendar-api.local;
	root /var/www/afendar-api/public;
	index index.php;
        fastcgi_pass php-fpm:9000;
}

# configuration file /etc/nginx/conf.d/default.conf:
server {
    listen       80;
    listen  [::]:80;
    server_name  localhost;
        root   /usr/share/nginx/html;
        index  index.html index.htm;
        root   /usr/share/nginx/html;
}
```

### 4.6 — web

- Image : `nginx:1.27-alpine`
- ID conteneur : `0ff8cf4dd168`
- En cours d’exécution : **true**
- Image ID : `sha256:6769dc3a703c719c1d2756bda113659be28ae16cf0da58dd5fd823d6b9a050ea`
- Plateforme : `linux/amd64`

#### Configuration Docker
| Élément | Valeur |
|---|---|
| Redémarrage | unless-stopped |
| Réseau(x) | docker_default  |
| Utilisateur conteneur |  |

#### Variables d’environnement (noms uniquement)
Les valeurs ne sont volontairement jamais exportées.

| Variable | Valeur exportée |
|---|---|
| `DYNPKG_RELEASE` | `[MASQUÉE]` |
| `NGINX_VERSION` | `[MASQUÉE]` |
| `NJS_RELEASE` | `[MASQUÉE]` |
| `NJS_VERSION` | `[MASQUÉE]` |
| `PATH` | `[MASQUÉE]` |
| `PKG_RELEASE` | `[MASQUÉE]` |

#### Ports, réseaux et montages
**Ports :**
```text
8080/tcp -> 0.0.0.0:8080
8080/tcp -> [::]:8080
```
**Réseaux et adresses :**
```text
docker_default : IP=172.18.0.3, aliases=[web web 0ff8cf4dd168]
```
**Montages :**

| Type | Source | Destination | Lecture seule |
|---|---|---|---|
| bind | `/home/afendar/Projects/Web/afendar-games/docker/nginx/afendar-front.local.conf` | `/etc/nginx/conf.d/afendar-front.local.conf` | false |
| bind | `/home/afendar/Projects/Web/afendar-games/afendar-admin` | `/var/www/afendar-admin` | false |
| bind | `/home/afendar/Projects/Web/afendar-games/afendar-bugs` | `/var/www/afendar-bugs` | false |
| bind | `/home/afendar/Projects/Web/afendar-games/afendar-front` | `/var/www/afendar-front` | false |
| bind | `/home/afendar/Projects/Web/afendar-games/docker/nginx/afendar-admin.local.conf` | `/etc/nginx/conf.d/afendar-admin.local.conf` | false |
| bind | `/home/afendar/Projects/Web/afendar-games/docker/nginx/afendar-bugs.local.conf` | `/etc/nginx/conf.d/afendar-bugs.local.conf` | false |
| bind | `/home/afendar/Projects/Web/afendar-games/docker/nginx/afendar-docs.local.conf` | `/etc/nginx/conf.d/afendar-docs.local.conf` | false |
|  | `` | `` |  |

#### Système et paquets
```text
ID=alpine
VERSION_ID=3.21.3
PRETTY_NAME="Alpine Linux v3.21"
```
<details><summary>Liste des paquets installés (déplier)</summary>

```text
alpine-baselayout-3.6.8-r1
alpine-baselayout-data-3.6.8-r1
alpine-keys-2.5-r0
alpine-release-3.21.3-r0
aom-libs-3.11.0-r0
apk-tools-2.14.6-r3
brotli-libs-1.1.0-r2
busybox-1.37.0-r12
busybox-binsh-1.37.0-r12
c-ares-1.34.5-r0
ca-certificates-20241121-r1
ca-certificates-bundle-20241121-r1
curl-8.12.1-r1
fontconfig-2.15.0-r1
freetype-2.13.3-r0
geoip-1.6.12-r5
gettext-envsubst-0.22.5-r0
libavif-1.0.4-r0
libbsd-0.12.2-r0
libbz2-1.0.8-r6
libcrypto3-3.3.3-r0
libcurl-8.12.1-r1
libdav1d-1.5.0-r0
libedit-20240808.3.1-r0
libexpat-2.7.0-r0
libgcrypt-1.10.3-r1
libgd-2.3.3-r9
libgpg-error-1.51-r0
libice-1.1.1-r6
libidn2-2.3.7-r0
libintl-0.22.5-r0
libjpeg-turbo-3.0.4-r0
libmd-1.1.0-r0
libncursesw-6.5_p20241006-r3
libpng-1.6.47-r0
libpsl-0.21.5-r3
libsharpyuv-1.4.0-r0
libsm-1.2.4-r4
libssl3-3.3.3-r0
libunistring-1.2-r0
libuuid-2.40.4-r1
libwebp-1.4.0-r0
libx11-1.8.10-r0
libxau-1.0.11-r4
libxcb-1.16.1-r0
libxdmcp-1.1.5-r1
libxext-1.3.6-r2
libxml2-2.13.4-r5
libxpm-3.5.17-r0
libxslt-1.1.42-r2
libxt-1.3.1-r0
musl-1.2.5-r9
musl-utils-1.2.5-r9
ncurses-terminfo-base-6.5_p20241006-r3
nghttp2-libs-1.64.0-r0
nginx-1.27.5-r1
nginx-module-geoip-1.27.5-r1
nginx-module-image-filter-1.27.5-r1
nginx-module-njs-1.27.5.0.8.10-r1
nginx-module-xslt-1.27.5-r1
pcre2-10.43-r0
scanelf-1.3.8-r1
ssl_client-1.37.0-r12
tiff-4.7.0-r0
tzdata-2025b-r0
xz-libs-5.6.3-r1
zlib-1.3.1-r2
zstd-libs-1.5.6-r2
```
</details>

#### NGINX
```text
nginx version: nginx/1.27.5
```
**Modules chargés :**
```text
Aucun module dynamique déclaré (modules probablement intégrés au binaire).
```
**VirtualHosts :**
```text

# configuration file /etc/nginx/conf.d/afendar-admin.local.conf:
server {
	listen 8080;
	server_name afendar-admin.local;
	root /var/www/afendar-admin/public;
	index index.php;
        fastcgi_pass php-fpm:9000;
}

# configuration file /etc/nginx/conf.d/afendar-bugs.local.conf:
server {
	listen 8080;
	server_name afendar-bugs.local;
	root /var/www/afendar-bugs/public;
	index index.php;
        fastcgi_pass php-fpm:9000;
}

# configuration file /etc/nginx/conf.d/afendar-docs.local.conf:
server {
    listen 8080;
    server_name afendar-docs.local;
        proxy_pass http://docs:8000;
}

# configuration file /etc/nginx/conf.d/afendar-front.local.conf:
server {
    listen 8080;
    index index.php;
    server_name afendar-front.local;
    root /var/www/afendar-front/public;
        fastcgi_pass php-fpm:9000;
}

# configuration file /etc/nginx/conf.d/default.conf:
server {
    listen       80;
    listen  [::]:80;
    server_name  localhost;
        root   /usr/share/nginx/html;
        index  index.html index.htm;
        root   /usr/share/nginx/html;
}
```

### 4.7 — php-fpm

- Image : `docker-php-fpm`
- ID conteneur : `503b523e877f`
- En cours d’exécution : **true**
- Image ID : `sha256:47bb26650bd9a11824d3934b41f572c5fa877f770ed1c35b9ed9022a2bbda886`
- Plateforme : `linux/amd64`

#### Configuration Docker
| Élément | Valeur |
|---|---|
| Redémarrage | unless-stopped |
| Réseau(x) | docker_default  |
| Utilisateur conteneur |  |

#### Variables d’environnement (noms uniquement)
Les valeurs ne sont volontairement jamais exportées.

| Variable | Valeur exportée |
|---|---|
| `GPG_KEYS` | `[MASQUÉE]` |
| `PATH` | `[MASQUÉE]` |
| `PHPIZE_DEPS` | `[MASQUÉE]` |
| `PHP_ASC_URL` | `[MASQUÉE]` |
| `PHP_CFLAGS` | `[MASQUÉE]` |
| `PHP_CPPFLAGS` | `[MASQUÉE]` |
| `PHP_INI_DIR` | `[MASQUÉE]` |
| `PHP_LDFLAGS` | `[MASQUÉE]` |
| `PHP_SHA256` | `[MASQUÉE]` |
| `PHP_URL` | `[MASQUÉE]` |
| `PHP_VERSION` | `[MASQUÉE]` |

#### Ports, réseaux et montages
**Ports :**
```text

```
**Réseaux et adresses :**
```text
docker_default : IP=172.18.0.8, aliases=[php-fpm php-fpm 503b523e877f]
```
**Montages :**

| Type | Source | Destination | Lecture seule |
|---|---|---|---|
| bind | `/home/afendar/Projects/Web/afendar-games/afendar-admin` | `/var/www/afendar-admin` | true |
| bind | `/home/afendar/Projects/Web/afendar-games/afendar-api` | `/var/www/afendar-api` | true |
| bind | `/home/afendar/Projects/Web/afendar-games/afendar-bugs` | `/var/www/afendar-bugs` | true |
| bind | `/home/afendar/Projects/Web/afendar-games/afendar-front` | `/var/www/afendar-front` | true |
|  | `` | `` |  |

#### Système et paquets
```text
PRETTY_NAME="Debian GNU/Linux 13 (trixie)"
VERSION_ID="13"
ID=debian
```
<details><summary>Liste des paquets installés (déplier)</summary>

```text
sh: 1: Bad substitution
```
</details>

#### PHP
```text
PHP 8.5.12 (cli) (built: Oct 28 2026 01:21:03) (NTS)
Copyright (c) The PHP Group
Built by https://github.com/docker-library/php
Zend Engine v4.5.12, Copyright (c) Zend Technologies
    with Xdebug v3.5.3, Copyright (c) 2002-2026, by Derick Rethans
    with Zend OPcache v8.5.12, Copyright (c), by Zend Technologies
```
**Extensions PHP chargées (CLI) :**
```text
[PHP Modules]
bcmath
bz2
calendar
Core
ctype
curl
date
dom
exif
fileinfo
filter
gd
hash
iconv
intl
json
ldap
lexbor
libxml
mbstring
memcached
mysqli
mysqlnd
openssl
pcre
PDO
pdo_mysql
pdo_pgsql
pdo_sqlite
pgsql
Phar
posix
random
readline
redis
Reflection
session
SimpleXML
sockets
sodium
SPL
sqlite3
standard
tokenizer
uri
xdebug
xml
xmlreader
xmlwriter
xsl
Zend OPcache
zip
zlib

[Zend Modules]
Xdebug
Zend OPcache
```
**Fichiers de configuration PHP (CLI) :**
```text
Configuration File (php.ini) Path: "/usr/local/etc/php"
Loaded Configuration File:         (none)
Scan for additional .ini files in: "/usr/local/etc/php/conf.d"
Additional .ini files parsed:      /usr/local/etc/php/conf.d/10-opcache.ini,
/usr/local/etc/php/conf.d/20-xdebug.ini,
/usr/local/etc/php/conf.d/99-afendar.ini,
/usr/local/etc/php/conf.d/docker-fpm.ini,
/usr/local/etc/php/conf.d/docker-php-ext-bcmath.ini,
/usr/local/etc/php/conf.d/docker-php-ext-bz2.ini,
/usr/local/etc/php/conf.d/docker-php-ext-calendar.ini,
/usr/local/etc/php/conf.d/docker-php-ext-exif.ini,
/usr/local/etc/php/conf.d/docker-php-ext-gd.ini,
/usr/local/etc/php/conf.d/docker-php-ext-intl.ini,
/usr/local/etc/php/conf.d/docker-php-ext-ldap.ini,
/usr/local/etc/php/conf.d/docker-php-ext-mysqli.ini,
/usr/local/etc/php/conf.d/docker-php-ext-pdo_mysql.ini,
/usr/local/etc/php/conf.d/docker-php-ext-pdo_pgsql.ini,
/usr/local/etc/php/conf.d/docker-php-ext-pgsql.ini,
/usr/local/etc/php/conf.d/docker-php-ext-redis.ini,
/usr/local/etc/php/conf.d/docker-php-ext-sockets.ini,
/usr/local/etc/php/conf.d/docker-php-ext-sodium.ini,
/usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini,
/usr/local/etc/php/conf.d/docker-php-ext-xsl.ini,
/usr/local/etc/php/conf.d/docker-php-ext-zip.ini,
/usr/local/etc/php/conf.d/xx-php-ext-memcached.ini
```
- Répertoire d’extensions : `/usr/local/lib/php/extensions/no-debug-non-zts-20250925`

#### Composer
```text
Composer version 2.10.3 2026-08-27 13:34:23
PHP version 8.5.12 (/usr/local/bin/php)
Run the "diagnose" command to get more detailed diagnostics output.
```

### 4.8 — node

- Image : `node:20-alpine`
- ID conteneur : `b35cef3137f0`
- En cours d’exécution : **true**
- Image ID : `sha256:11cedc39e663e7c5d5cb9cc77a461a0d2adc25537b94e6831a6108f09cb2001b`
- Plateforme : `linux/amd64`

#### Configuration Docker
| Élément | Valeur |
|---|---|
| Redémarrage | unless-stopped |
| Réseau(x) | docker_default  |
| Utilisateur conteneur |  |

#### Variables d’environnement (noms uniquement)
Les valeurs ne sont volontairement jamais exportées.

| Variable | Valeur exportée |
|---|---|
| `NODE_VERSION` | `[MASQUÉE]` |
| `PATH` | `[MASQUÉE]` |
| `YARN_VERSION` | `[MASQUÉE]` |

#### Ports, réseaux et montages
**Ports :**
```text

```
**Réseaux et adresses :**
```text
docker_default : IP=172.18.0.2, aliases=[node node b35cef3137f0]
```
**Montages :**

| Type | Source | Destination | Lecture seule |
|---|---|---|---|
| volume | `/var/lib/docker/volumes/afendar-bugs-node-modules/_data` | `/var/www/afendar-bugs/node_modules` | true |
| bind | `/home/afendar/Projects/Web/afendar-games/afendar-docs` | `/var/www/afendar-docs` | true |
| volume | `/var/lib/docker/volumes/afendar-docs-node-modules/_data` | `/var/www/afendar-docs/node_modules` | true |
| bind | `/home/afendar/Projects/Web/afendar-games/afendar-front` | `/var/www/afendar-front` | true |
| volume | `/var/lib/docker/volumes/afendar-front-node-modules/_data` | `/var/www/afendar-front/node_modules` | true |
| bind | `/home/afendar/Projects/Web/afendar-games/afendar-admin` | `/var/www/afendar-admin` | true |
| volume | `/var/lib/docker/volumes/afendar-admin-node-modules/_data` | `/var/www/afendar-admin/node_modules` | true |
| bind | `/home/afendar/Projects/Web/afendar-games/afendar-bugs` | `/var/www/afendar-bugs` | true |
|  | `` | `` |  |

#### Système et paquets
```text
ID=alpine
VERSION_ID=3.23.4
PRETTY_NAME="Alpine Linux v3.23"
```
<details><summary>Liste des paquets installés (déplier)</summary>

```text
alpine-baselayout-3.7.2-r0
alpine-baselayout-data-3.7.2-r0
alpine-keys-2.6-r0
alpine-release-3.23.4-r0
apk-tools-3.0.6-r0
busybox-1.37.0-r30
busybox-binsh-1.37.0-r30
ca-certificates-bundle-20260413-r0
libapk-3.0.6-r0
libcrypto3-3.5.6-r0
libgcc-15.2.0-r2
libssl3-3.5.6-r0
libstdc++-15.2.0-r2
musl-1.2.5-r23
musl-utils-1.2.5-r23
scanelf-1.3.8-r2
ssl_client-1.37.0-r30
zlib-1.3.2-r0
```
</details>

#### Node.js et gestionnaires de paquets
```text
node : v20.20.2
npm : 10.8.2
yarn : 1.22.22
```

### 4.9 — docs

- Image : `squidfunk/mkdocs-material:latest`
- ID conteneur : `87bfbc5ffe84`
- En cours d’exécution : **true**
- Image ID : `sha256:09c3b867b8795057e88b0e2c39a389972696e7770b0b3d8699d5192d03baa30e`
- Plateforme : `linux/amd64`

#### Configuration Docker
| Élément | Valeur |
|---|---|
| Redémarrage | unless-stopped |
| Réseau(x) | docker_default  |
| Utilisateur conteneur |  |

#### Variables d’environnement (noms uniquement)
Les valeurs ne sont volontairement jamais exportées.

| Variable | Valeur exportée |
|---|---|
| `PATH` | `[MASQUÉE]` |

#### Ports, réseaux et montages
**Ports :**
```text

```
**Réseaux et adresses :**
```text
docker_default : IP=172.18.0.5, aliases=[docs docs 87bfbc5ffe84]
```
**Montages :**

| Type | Source | Destination | Lecture seule |
|---|---|---|---|
| bind | `/home/afendar/Projects/Web/afendar-games/afendar-docs` | `/docs` | true |
|  | `` | `` |  |

#### Système et paquets
```text
ID=alpine
VERSION_ID=3.21.7
PRETTY_NAME="Alpine Linux v3.21"
```
<details><summary>Liste des paquets installés (déplier)</summary>

```text
.python-rundeps-20251009.224302
alpine-baselayout-3.6.8-r1
alpine-baselayout-data-3.6.8-r1
alpine-keys-2.5-r0
alpine-release-3.21.7-r0
apk-tools-2.14.6-r3
brotli-1.1.0-r2
brotli-dev-1.1.0-r2
brotli-libs-1.1.0-r2
busybox-1.37.0-r14
busybox-binsh-1.37.0-r14
bzip2-dev-1.0.8-r6
c-ares-1.34.8-r0
ca-certificates-20260413-r0
ca-certificates-bundle-20260413-r0
cairo-1.18.4-r0
fontconfig-2.15.0-r1
freetype-2.13.3-r0
freetype-dev-2.13.3-r0
gdbm-1.24-r0
git-2.47.3-r0
git-fast-import-2.47.3-r0
git-init-template-2.47.3-r0
jpeg-dev-9f-r0
keyutils-libs-1.6.3-r4
krb5-conf-1.0-r2
krb5-libs-1.21.3-r0
lcms2-2.19-r0
libbsd-0.12.2-r0
libbz2-1.0.8-r6
libcom_err-1.47.1-r1
libcrypto3-3.3.7-r0
libcurl-8.14.1-r2
libedit-20240808.3.1-r0
libexpat-2.8.2-r0
libffi-3.4.7-r0
libgcc-14.2.0-r4
libidn2-2.3.7-r0
libintl-0.22.5-r0
libjpeg-turbo-3.0.4-r0
libjpeg-turbo-dev-3.0.4-r0
libmd-1.1.0-r0
libncursesw-6.5_p20241006-r3
libnsl-2.0.1-r0
libpanelw-6.5_p20241006-r3
libpng-1.6.57-r0
libpng-dev-1.6.57-r0
libpsl-0.21.5-r3
libssl3-3.3.7-r0
libtirpc-1.3.5-r0
libtirpc-conf-1.3.5-r0
libturbojpeg-3.0.4-r0
libunistring-1.2-r0
libuuid-2.40.4-r1
libverto-0.3.2-r2
libx11-1.8.10-r0
libxau-1.0.11-r4
libxcb-1.16.1-r0
libxdmcp-1.1.5-r1
libxext-1.3.6-r2
libxrender-0.9.11-r5
musl-1.2.5-r11
musl-utils-1.2.5-r11
ncurses-terminfo-base-6.5_p20241006-r3
nghttp2-libs-1.69.0-r0
openssh-9.9_p2-r0
openssh-client-common-9.9_p2-r0
openssh-client-default-9.9_p2-r0
openssh-keygen-9.9_p2-r0
openssh-server-9.9_p2-r0
openssh-server-common-9.9_p2-r0
openssh-sftp-server-9.9_p2-r0
pcre2-10.43-r0
pixman-0.43.4-r1
pkgconf-2.3.0-r0
pngquant-3.0.3-r0
readline-8.2.13-r0
scanelf-1.3.8-r1
sqlite-libs-3.48.0-r4
ssl_client-1.37.0-r14
tini-0.19.0-r3
tzdata-2026c-r0
xz-libs-5.8.3-r0
zlib-1.3.2-r0
zlib-dev-1.3.2-r0
zstd-libs-1.5.6-r2
```
</details>

### 4.10 — mysql

- Image : `mysql:8.0.34`
- ID conteneur : `820132b8ec7a`
- En cours d’exécution : **true**
- Image ID : `sha256:e1d66a2a0aa16e23edc8d1c1e08be4a0ba8c239c9414a90b1d0cb4944ca4a194`
- Plateforme : `linux/amd64`

#### Configuration Docker
| Élément | Valeur |
|---|---|
| Redémarrage | unless-stopped |
| Réseau(x) | docker_default  |
| Utilisateur conteneur |  |

#### Variables d’environnement (noms uniquement)
Les valeurs ne sont volontairement jamais exportées.

| Variable | Valeur exportée |
|---|---|
| `GOSU_VERSION` | `[MASQUÉE]` |
| `MYSQL_DATABASE` | `[MASQUÉE]` |
| `MYSQL_MAJOR` | `[MASQUÉE]` |
| `MYSQL_ROOT_PASSWORD` | `[MASQUÉE]` |
| `MYSQL_SHELL_VERSION` | `[MASQUÉE]` |
| `MYSQL_VERSION` | `[MASQUÉE]` |
| `PATH` | `[MASQUÉE]` |

#### Ports, réseaux et montages
**Ports :**
```text
3306/tcp -> 0.0.0.0:3306
3306/tcp -> [::]:3306
```
**Réseaux et adresses :**
```text
docker_default : IP=172.18.0.6, aliases=[mysql mysql 820132b8ec7a]
```
**Montages :**

| Type | Source | Destination | Lecture seule |
|---|---|---|---|
| volume | `/var/lib/docker/volumes/afendar-mysql-data/_data` | `/var/lib/mysql` | true |
|  | `` | `` |  |

#### Système et paquets
```text
ID="ol"
VERSION_ID="8.8"
PRETTY_NAME="Oracle Linux Server 8.8"
```
<details><summary>Liste des paquets installés (déplier)</summary>

```text
libgcc	8.5.0-18.0.6.el8
tzdata	2023c-1.el8
publicsuffix-list-dafsa	20180723-1.el8
pcre2	10.32-3.el8_6
setup	2.12.2-9.el8
basesystem	11-5.el8
libselinux	2.9-8.el8
glibc-minimal-langpack	2.28-225.0.4.el8_8.6
glibc	2.28-225.0.4.el8_8.6
zlib	1.2.11-21.el8_7
info	6.5-7.el8
xz-libs	5.2.4-4.el8_6
gmp	6.1.2-10.el8
libcom_err	1.45.6-5.el8
libxml2	2.9.7-16.el8_8.1
libidn2	2.2.0-1.el8
libacl	2.2.53-1.el8
sed	4.5-5.el8
p11-kit	0.23.22-1.el8
readline	7.0-10.el8
libgcrypt	1.8.5-7.el8_6
libsmartcols	2.32.1-42.el8_8
libuuid	2.32.1-42.el8_8
lua-libs	5.3.4-12.el8
pcre	8.42-6.el8
libblkid	2.32.1-42.el8_8
systemd-libs	239-74.0.5.el8_8.5
chkconfig	1.19.1-1.0.2.el8
ca-certificates	2023.2.60_v7.0.306-80.0.el8_8
libdb	5.3.28-42.el8_4
libarchive	3.3.3-5.el8
mpfr	3.1.6-1.el8
gnutls	3.6.16-6.el8_7
gobject-introspection	1.56.1-1.el8
libksba	1.3.5-9.el8_7
brotli	1.0.6-3.el8
keyutils-libs	1.5.10-9.el8
audit-libs	3.0.7-4.el8
libnghttp2	1.33.0-5.el8_8
gawk	4.2.1-4.el8
libverto	0.3.2-2.el8
cyrus-sasl-lib	2.1.27-6.el8_5
libyaml	0.1.7-5.el8
gnupg2	2.2.20-3.el8_6
libssh-config	0.9.6-10.el8_8
libcurl	7.61.1-30.el8_8.3
rpm	4.14.3-26.el8
libmodulemd	2.13.0-1.el8
librepo	1.14.2-4.el8
microdnf	3.8.0-2.el8
shadow-utils	4.6-17.el8
zstd	1.4.4-1.0.1.el8
openssl	1.1.1k-9.el8_7
findutils	4.6.0-20.el8_8.1
libtirpc	1.1.4-8.el8
mysql-community-server-minimal	8.0.34-1.el8
python39-pip-wheel	20.2.4-7.module+el8.6.0+20625+ee813db2
gdbm-libs	1.18-2.el8
python39-libs	3.9.16-1.module+el8.8.0+21116+ee8c18cf.1
python39-setuptools	50.3.2-4.module+el8.5.0+20364+c7fe1181
mysql-shell	8.0.34-1.el8
gpg-pubkey	ad986da3-5cabf60d
crypto-policies	20221215-1.gitece0092.el8
redhat-release	8.8-0.8.0.1.el8
ncurses-base	6.1-9.20180224.el8_8.1
oraclelinux-release	8.8-1.0.7.el8
filesystem	3.8-6.el8
ncurses-libs	6.1-9.20180224.el8_8.1
bash	4.4.20-4.el8_6
glibc-common	2.28-225.0.4.el8_8.6
libsepol	2.9-3.el8
libgpg-error	1.31-1.el8
bzip2-libs	1.0.6-26.el8
sqlite-libs	3.26.0-18.0.1.el8_8
libcap	2.48-5.el8_8
libzstd	1.4.4-1.0.1.el8
libunistring	0.9.9-3.el8
libattr	2.4.48-3.el8
coreutils-single	8.30-15.0.1.el8
libffi	3.1-24.el8
popt	1.18-1.el8
libassuan	2.5.1-3.el8
elfutils-libelf	0.188-3.el8
libtasn1	4.13-4.el8_7
libxcrypt	4.1.1-6.el8
lz4-libs	1.8.3-3.el8_4
grep	3.1-6.el8
libmount	2.32.1-42.el8_8
libusbx	1.0.23-4.el8
p11-kit-trust	0.23.22-1.el8
openssl-libs	1.1.1k-9.el8_7
libdb-utils	5.3.28-42.el8_4
libpsl	0.20.2-6.el8
nettle	3.4.1-7.el8
glib2	2.56.4-161.el8
libpeas	1.22.0-6.el8
file-libs	5.33-24.el8
json-c	0.13.1-3.el8
libcap-ng	0.7.11-1.el8
libsemanage	2.9-9.el8_6
libsigsegv	2.11-5.el8
libstdc++	8.5.0-18.0.6.el8
krb5-libs	1.18.2-25.0.1.el8_8
openldap	2.4.46-18.el8
npth	1.5-4.el8
gpgme	1.13.1-11.el8
libssh	0.9.6-10.el8_8
curl	7.61.1-30.el8_8.3
rpm-libs	4.14.3-26.el8
libsolv	0.7.20-4.el8_7
libdnf	0.63.0-14.0.1.el8_8
oraclelinux-release-el8	1.0-32.el8
tar	1.30-9.el8
xz	5.2.4-4.el8_6
gzip	1.9-13.el8_5
bzip2	1.0.6-26.el8
libaio	0.3.112-1.el8
python39-setuptools-wheel	50.3.2-4.module+el8.5.0+20364+c7fe1181
libnsl2	1.2.0-2.20180605git4a062cf.el8
expat	2.2.5-11.0.1.el8
python39	3.9.16-1.module+el8.8.0+21116+ee8c18cf.1
python39-pip	20.2.4-7.module+el8.6.0+20625+ee813db2
```
</details>

#### Moteurs de données et cache
```text
/usr/sbin/mysqld  Ver 8.0.34 for Linux on x86_64 (MySQL Community Server - GPL)
```

### 4.11 — redis

- Image : `redis:7-alpine`
- ID conteneur : `066ad6990125`
- En cours d’exécution : **true**
- Image ID : `sha256:5509c0097c6064aa8a3b1df58f1d950e67090fffa6678ae8f3f1dc2385f12deb`
- Plateforme : `linux/amd64`

#### Configuration Docker
| Élément | Valeur |
|---|---|
| Redémarrage | unless-stopped |
| Réseau(x) | docker_default  |
| Utilisateur conteneur |  |

#### Variables d’environnement (noms uniquement)
Les valeurs ne sont volontairement jamais exportées.

| Variable | Valeur exportée |
|---|---|
| `PATH` | `[MASQUÉE]` |
| `REDIS_REPLICATION_MODE` | `[MASQUÉE]` |
| `REDIS_VERSION` | `[MASQUÉE]` |

#### Ports, réseaux et montages
**Ports :**
```text
6379/tcp -> 0.0.0.0:6379
6379/tcp -> [::]:6379
```
**Réseaux et adresses :**
```text
docker_default : IP=172.18.0.7, aliases=[redis redis 066ad6990125]
```
**Montages :**

| Type | Source | Destination | Lecture seule |
|---|---|---|---|
| volume | `/var/lib/docker/volumes/afendar-redis-data/_data` | `/data` | true |
|  | `` | `` |  |

#### Système et paquets
```text
ID=alpine
VERSION_ID=3.21.7
PRETTY_NAME="Alpine Linux v3.21"
```
<details><summary>Liste des paquets installés (déplier)</summary>

```text
.redis-rundeps-20260818.165646
alpine-baselayout-3.6.8-r1
alpine-baselayout-data-3.6.8-r1
alpine-keys-2.5-r0
alpine-release-3.21.7-r0
apk-tools-2.14.6-r3
busybox-1.37.0-r14
busybox-binsh-1.37.0-r14
ca-certificates-bundle-20260413-r0
libcap-ng-0.8.5-r0
libcrypto3-3.3.7-r0
libssl3-3.3.7-r0
musl-1.2.5-r11
musl-utils-1.2.5-r11
scanelf-1.3.8-r1
setpriv-2.40.4-r1
ssl_client-1.37.0-r14
tzdata-2026c-r0
zlib-1.3.2-r0
```
</details>

#### Moteurs de données et cache
```text
Redis server v=7.4.11 sha=00000000:0 malloc=jemalloc-5.3.0 bits=64 build=fbf7a7d03c2e9219
```

## 5. Réseaux Docker

| Nom | Driver | Scope |
|---|---|---|
| bridge | bridge | local |
| docker_default | bridge | local |
| host | host | local |
| none | null | local |
| web_default | bridge | local |
| web_internal | bridge | local |
| web_test | bridge | local |

## 6. Volumes Docker

| Nom | Driver |
|---|---|
| `2b36786ee10800425a4d28fa3812a79146e64ece4eabc88ed9707b8f9cbcf049` | local |
| `3cfc537a6e6af27f9d9700e45be2b30fedcefe913fb01d7f2d7ab29c9509bbbe` | local |
| `4eff13729908dd3fee5ea978858f636a8b0b4cbbc2426fe7df35758c8293baee` | local |
| `24afb3dec96b9ac493afdf6a64309977a2e52c661e82fcd4d4a09e594c0a239f` | local |
| `37a63d67fe5a2b5abddc4a11d42e58ff9a73b3d2e8013c60a3bd7836c8eeb72b` | local |
| `394b932aee10c646450d9f0e98f25de9301c2db083a51e26dd1db3776e635dae` | local |
| `600f8e4185fe0b50943873ee5ccc914cf4e921c5967a99f5c1b2dcc41ea7d560` | local |
| `4283f3f8e21408354bc6b6d8af7657cfec267283d97d959ca05f861bbb8e86d4` | local |
| `20191d8fbf5ba12d744c98bd70e92a903f99ace7e822928ac1bdc554575f8b03` | local |
| `afendar-admin-node-modules` | local |
| `afendar-bugs-node-modules` | local |
| `afendar-docs-node-modules` | local |
| `afendar-front-node-modules` | local |
| `afendar-mysql-data` | local |
| `afendar-redis-data` | local |
| `b28c7d736281db40c04d17360865f37192cc8aa3d180a6c5c24c232e9ad9de97` | local |
| `c72da36d256824a4200c1a47913681ba17e2b5f7a07fb2f65e2c345afb55c646` | local |
| `d04aba0e4547db5548071084f6750b532879c4fa918d82ec4d9bc41d8227ebbc` | local |
| `d320462681a9b970103dba1039d9558b138b809756d1baf165f473d1e5bd5b53` | local |
| `e582fe56cc9146275e120bf654fee22f1d16ced09a8fddae2379529fcdf32927` | local |
| `ea7175147721b4400d11da0dde5a45c942c34fb9dd3b2a7dd05463a40205b3d7` | local |
| `web_mysql-data` | local |

## 7. Fichiers Compose et dépendances du projet

Répertoire analysé : `.` (profondeur maximale : 6).

### `docker/compose.yml`
**Services déclarés :**
```text
time="2026-11-03T12:46:55+01:00" level=warning msg="The \"REDIS_PASSWORD\" variable is not set. Defaulting to a blank string."
time="2026-11-03T12:46:55+01:00" level=warning msg="The \"REDIS_PORT\" variable is not set. Defaulting to a blank string."
time="2026-11-03T12:46:55+01:00" level=warning msg="The \"MYSQL_DATABASE\" variable is not set. Defaulting to a blank string."
time="2026-11-03T12:46:55+01:00" level=warning msg="The \"MYSQL_ROOT_PASSWORD\" variable is not set. Defaulting to a blank string."
time="2026-11-03T12:46:55+01:00" level=warning msg="The \"MYSQL_PORT\" variable is not set. Defaulting to a blank string."
redis
mysql
php-fpm
api
docs
node
web
```
**Images résolues :**
```text
time="2026-11-03T12:46:55+01:00" level=warning msg="The \"REDIS_PASSWORD\" variable is not set. Defaulting to a blank string."
time="2026-11-03T12:46:55+01:00" level=warning msg="The \"REDIS_PORT\" variable is not set. Defaulting to a blank string."
time="2026-11-03T12:46:55+01:00" level=warning msg="The \"MYSQL_DATABASE\" variable is not set. Defaulting to a blank string."
time="2026-11-03T12:46:55+01:00" level=warning msg="The \"MYSQL_ROOT_PASSWORD\" variable is not set. Defaulting to a blank string."
time="2026-11-03T12:46:55+01:00" level=warning msg="The \"MYSQL_PORT\" variable is not set. Defaulting to a blank string."
nginx:1.27-alpine
nginx:1.27-alpine
squidfunk/mkdocs-material:latest
redis:7-alpine
mysql:8.0.34
node:20-alpine
docker-php-fpm
```

### Fichiers de verrouillage et manifestes détectés
| Fichier | Rôle |
|---|---|
| `afendar-docs/requirements.txt` | Dépendances Python |
| `afendar-docs/package-lock.json` | Versions npm verrouillées |
| `afendar-docs/package.json` | Dépendances JavaScript déclarées |
| `afendar-bugs/composer.lock` | Versions PHP verrouillées |
| `afendar-bugs/package-lock.json` | Versions npm verrouillées |
| `afendar-bugs/composer.json` | Dépendances PHP déclarées |
| `afendar-bugs/package.json` | Dépendances JavaScript déclarées |
| `afendar-bugs/yarn.lock` | Versions Yarn verrouillées |
| `afendar-admin/composer.lock` | Versions PHP verrouillées |
| `afendar-admin/package-lock.json` | Versions npm verrouillées |
| `afendar-admin/composer.json` | Dépendances PHP déclarées |
| `afendar-admin/package.json` | Dépendances JavaScript déclarées |
| `afendar-front/composer.lock` | Versions PHP verrouillées |
| `afendar-front/package-lock.json` | Versions npm verrouillées |
| `afendar-front/composer.json` | Dépendances PHP déclarées |
| `afendar-front/package.json` | Dépendances JavaScript déclarées |
| `afendar-front/yarn.lock` | Versions Yarn verrouillées |
| `afendar-api/composer.lock` | Versions PHP verrouillées |
| `afendar-api/composer.json` | Dépendances PHP déclarées |

## 8. Points de contrôle avant production

- [ ] Images Docker référencées par tag immuable ou digest vérifié.
- [ ] Versions PHP, extensions et modules Apache validés en production.
- [ ] Secrets fournis par un gestionnaire de secrets ou variables sécurisées.
- [ ] Volumes persistants, sauvegardes et procédure de restauration documentés.
- [ ] Ports publiés limités au strict nécessaire.
- [ ] Réseaux et flux interservices documentés.
- [ ] Dépendances applicatives verrouillées (Composer/npm/etc.).
- [ ] Logs, supervision, healthchecks et politique de redémarrage vérifiés.

---
*Document généré automatiquement. Les variables d’environnement sont volontairement limitées à leurs noms ; leurs valeurs ne sont pas exportées.*
