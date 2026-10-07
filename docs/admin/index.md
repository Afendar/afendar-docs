hide:
    - toc
    - navigation

# Administration

<div class="project-hero project-hero--admin" markdown>

## 🖥️ Afendar Admin

Interface d'administration permettant de gérer et configurer les différentes fonctionnalités de la plateforme Afendar.

L'Admin s'appuie notamment sur l'API Afendar pour la gestion des données et propose un **Page Builder** permettant de construire dynamiquement les pages du site.

</div>

---

## Documentation

<div class="project-doc-grid" markdown>

<div class="project-doc-card" markdown>

### 🧱 Architecture du Page Builder

Découvrez l'architecture du Page Builder, son fonctionnement interne et les différents éléments qui permettent de construire une page dynamiquement.

**Contenu :**

- architecture générale
- structure des pages
- composants du Page Builder
- cycle de rendu
- interactions avec l'API

[Explorer l'architecture →](page-builder/index.md){ .md-button .md-button--primary }

</div>

<div class="project-doc-card project-doc-card--soon" markdown>

### 🧩 Composants du Page Builder

Documentation détaillée des différents composants disponibles dans le Page Builder.

<span class="doc-status">Documentation à venir</span>

</div>

<div class="project-doc-card project-doc-card--soon" markdown>

### ⚙️ Configuration

Configuration spécifique de l'application d'administration.

<span class="doc-status">Documentation à venir</span>

</div>

</div>

---

## Architecture générale

L'application Admin communique principalement avec l'API Afendar pour récupérer et modifier les données.

```mermaid
graph LR
    Admin[Afendar Admin] --> API[Afendar API]
    Admin --> Builder[Page Builder]
    Builder --> API
    API --> MySQL[(MySQL)]
    API --> Redis[(Redis)]
```

!!!info

    Le Page Builder utilise les blocs et leur configuration fournis par l'API pour construire les pages administrables.
