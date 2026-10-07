hide:
    - toc
    - navigation

# Front

<div class="project-hero project-hero--front" markdown>

## 🌐 Afendar Front

Application frontend principale de la plateforme Afendar.

Le Front consomme principalement les données exposées par l'API et utilise notamment les contenus configurés depuis l'interface d'administration.

</div>

---

## Documentation

<div class="project-doc-grid" markdown>

<div class="project-doc-card" markdown>

### 🚧 Mode maintenance

Documentation du système de maintenance du Front.

Cette section présente :

- l'activation du mode maintenance
- son fonctionnement
- les conditions d'affichage
- la configuration associée

[Voir la documentation →](maintenance/index.md){ .md-button .md-button--primary }

</div>

<div class="project-doc-card project-doc-card--soon" markdown>

### 🔌 Intégration avec l'API

Fonctionnement de la communication entre le Front et l'API Afendar.

<span class="doc-status">Documentation à venir</span>

</div>

<div class="project-doc-card project-doc-card--soon" markdown>

### 🧱 Rendu des pages

Documentation du rendu des pages et des blocs provenant du Page Builder.

<span class="doc-status">Documentation à venir</span>

</div>

</div>

---

## Architecture

Le Front consomme les données exposées par l'API :

```mermaid
graph LR
    User[Utilisateur] --> Front[Afendar Front]
    Front --> API[Afendar API]
    API --> MySQL[(MySQL)]
    API --> Redis[(Redis)]
```

À terme, cette section documentera également le fonctionnement du rendu des pages générées par le Page Builder.