1. Générer les clés RSA

À la racine de ton projet Symfony, exécute :

```shell
mkdir -p config/jwt

openssl genrsa -out config/jwt/private.pem 4096

openssl rsa \
    -in config/jwt/private.pem \
    -pubout \
    -out config/jwt/public.pem
```

2. Générer les secrets

Pour générer une passphrase :

```shell
openssl rand -hex 32
```

Pour la clé de chiffrement OAuth2 :

```shell
php -r "echo bin2hex(random_bytes(16)).PHP_EOL;"
```

3. configurer `.env.local`

Ajoute les variables suivantes :

```env
OAUTH_PRIVATE_KEY=%kernel.project_dir%/config/jwt/private.pem
OAUTH_PUBLIC_KEY=%kernel.project_dir%/config/jwt/public.pem
OAUTH_PASSPHRASE=
OAUTH_ENCRYPTION_KEY=COLLE_ICI_TA_CLE_DE_32_CARACTERES
```

4. Protéger les fichiers

```shell
chmod 640 config/jwt/private.pem
chmod 644 config/jwt/public.pem
chown 1000:www-data config/jwt/private.pem
```

5. création du client

```shell
php bin/console league:oauth2-server:create-client \
  "Afendar Games" \
  "frontend-public" \
  --public \
  --redirect-uri="http://afendar-front.local:8080/oauth/callback" \
  --grant-type="authorization_code" \
  --grant-type="refresh_token" \
  --scope="email"
```

Contrôle de la création

```shell
php bin/console league:oauth2-server:list-clients
```