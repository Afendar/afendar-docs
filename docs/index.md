hide:
    - toc
    - navigation

# Bienvenue sur la documentation Afendar

<div class="home-hero" markdown>

## Documentation technique Afendar

Bienvenue dans la documentation technique des projets **Afendar Games**.

Cette documentation centralise l'installation, la configuration et l'utilisation des différents composants de la plateforme.

<div class="home-actions" markdown>
[🚀 Commencer l'installation](install.md)
[⚙️ Configuration](configuration.md)
</div>

</div>

---

## Architecture du projet

Afendar Games est composé de plusieurs projets complémentaires :

<div class="project-grid" markdown>

<div class="project-card project-card--api" markdown>

### 🔌 API

API backend principale du projet.

Elle fournit les services nécessaires aux applications Afendar et gère notamment :

- l'authentification
- les données métier
- les utilisateurs
- les communications avec MySQL et Redis
- les endpoints REST

[Voir la documentation API →](api/index.md)

</div>

<div class="project-card project-card--admin" markdown>

### 🖥️ Administration

Interface d'administration permettant de gérer les données et la configuration de la plateforme.

- gestion des utilisateurs
- administration des données
- configuration
- outils internes

[Voir la documentation Admin →](admin/index.md)

</div>

<div class="project-card project-card--bugs" markdown>

### 🐛 Bugs

Application dédiée au suivi et à la gestion des bugs.

Elle permet notamment de centraliser :

- les anomalies
- les tickets
- leur état
- les informations de debug
- le suivi des corrections

[Voir la documentation Bugs →](bugs/index.md)

</div>

<div class="project-card project-card--front" markdown>

### 🌐 Front

Application frontend principale d'Afendar.

Cette section présente notamment :

- l'installation
- le développement local
- la configuration
- l'architecture frontend
- le déploiement

[Voir la documentation Front →](front/index.md)

</div>

</div>

---

## Développement de la documentation

La documentation utilise MkDocs Material.

Le service Docker monte directement le repository afendar-docs, ce qui permet de bénéficier du rechargement automatique lors de la modification des fichiers Markdown.

Pour consulter les logs :

```bash
docker compose logs -f docs
```

La documentation est disponible à :

```
http://afendar-docs.local:8080
```

### Strucuture de la documentation

```
afendar-docs/
├── docs/
│   ├── index.md
│   ├── api/
│   │   └── index.md
│   ├── admin/
│   │   └── index.md
│   ├── front/
│   │   └── index.md
│   ├── bugs/
│   │   └── index.md
│   └── stylesheets/
│       └── extra.css
└── mkdocs.yml
```