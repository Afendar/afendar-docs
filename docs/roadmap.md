---
hide:
    - navigation
---

# AFENDAR GAMES — ROADMAP DE DÉVELOPPEMENT

**Période** : `Décembre 2026` → `Novembre 2027`

**Objectif** : *construire une plateforme complète pour le studio Afendar, ses jeux et sa communauté.*

{{ progress }}

---

## PHASE 1 — FONDATIONS

{{ progress_section }}

### Décembre 2026 — Version 0.1 : Audit et fondations techniques

**Objectif :** préparer une base solide pour les futurs développements sans casser les fonctionnalités existantes.

{{ progress_section }}

#### Audit du projet

- [x] Faire l'inventaire des fonctionnalités existantes.
- [x] Identifier les pages terminées, incomplètes et manquantes.
- [x] Identifier les bugs existants.
- [x] Faire l'inventaire des composants réutilisables.
- [x] Vérifier la structure frontend et backend.
- [x] Vérifier la base de données et les relations existantes.

#### Architecture

- [x] Définir l'architecture générale du projet.
- [x] Définir les conventions de développement.
- [x] Organiser les routes et les pages.
- [x] Organiser les composants partagés.
- [ ] Définir la gestion des erreurs.
- [ ] Préparer les environnements de développement et de production.

#### Design system

- [x] Définir les couleurs et typographies Afendar.
- [x] Créer les composants de boutons.
- [x] Créer les composants de formulaires.
- [x] Créer les cartes de jeux et d'articles.
- [x] Créer les éléments de navigation.
- [ ] Vérifier le responsive mobile, tablette et desktop.

#### Release 0.1

- [x] Vérifier que les pages existantes fonctionnent.
- [x] Corriger les problèmes prioritaires.
- [x] Mettre en place une première version de référence.

---

### Janvier 2027 — Version 0.2 : Authentification et comptes

**Objectif :** permettre aux visiteurs de créer un compte Afendar.

{{ progress_section }}

#### Inscription

- [ ] Créer la page d'inscription `/register`.
- [ ] Créer le formulaire d'inscription.
- [ ] Vérifier l'unicité de l'adresse e-mail.
- [ ] Vérifier l'unicité du nom d'utilisateur.
- [ ] Ajouter la validation des mots de passe.
- [ ] Ajouter la vérification de l'adresse e-mail.
- [ ] Ajouter l'acceptation des conditions d'utilisation.

#### Connexion

- [x] Créer la page `/login`.
- [x] Créer le système de connexion.
- [x] Ajouter la déconnexion.
- [ ] Ajouter la récupération de mot de passe.
- [x] Gérer les sessions utilisateur.
- [ ] Gérer les erreurs d'authentification.

#### Sécurité

- [x] Hasher les mots de passe.
- [x] Protéger les routes privées.
- [ ] Ajouter une limitation des tentatives de connexion.
- [ ] Sécuriser les formulaires contre les abus.

#### Release 0.2

- [ ] Tester l'inscription.
- [x] Tester la connexion et la déconnexion.
- [ ] Tester la récupération de mot de passe.
- [ ] Publier le système de comptes.

---

### Février 2027 — Version 0.3 : Profils et espace personnel

**Objectif :** donner une véritable utilité au compte utilisateur.

{{ progress_section }}

#### Profil utilisateur

- [ ] Créer la page `/account/profile`.
- [ ] Permettre de choisir un pseudonyme.
- [ ] Permettre de choisir un avatar.
- [ ] Ajouter une biographie.
- [ ] Permettre de modifier les informations du profil.
- [ ] Ajouter les paramètres de visibilité.

#### Tableau de bord

- [x] Créer la page `/account`.
- [x] Afficher les informations du compte.
- [ ] Afficher les jeux favoris.
- [ ] Afficher les jeux suivis.
- [ ] Afficher les derniers scores.
- [ ] Afficher l'activité récente.
- [ ] Ajouter des raccourcis vers les différentes sections.

#### Paramètres

- [ ] Ajouter la modification de l'adresse e-mail (BackOffice uniquement).
- [ ] Ajouter la modification du mot de passe.
- [ ] Ajouter les paramètres de confidentialité.
- [ ] Prévoir la suppression du compte.

#### Release 0.3

- [ ] Tester les profils publics.
- [ ] Vérifier que les informations privées ne sont jamais exposées.
- [ ] Publier les profils et le tableau de bord.

---

## PHASE 2 — JEUX ET AVIS

{{ progress_section }}

### Mars 2027 — Version 0.4 : Catalogue de jeux

**Objectif :** transformer Games en véritable catalogue de jeux Afendar.

{{ progress_section }}

#### Catalogue

- [ ] Améliorer la page `/games`.
- [ ] Créer des catégories de jeux.
- [ ] Ajouter les filtres.
- [ ] Ajouter la recherche.
- [ ] Ajouter le tri par date, popularité et nom.
- [ ] Ajouter les jeux à venir.
- [ ] Ajouter les jeux en développement.

#### Fiches de jeux

- [ ] Créer un modèle de fiche de jeu.
- [ ] Ajouter une description.
- [ ] Ajouter des captures d'écran.
- [ ] Ajouter une bande-annonce.
- [ ] Ajouter les plateformes disponibles.
- [ ] Ajouter les informations techniques.
- [ ] Ajouter le statut du jeu.
- [ ] Ajouter les liens de téléchargement ou d'achat.
- [ ] Ajouter les changelogs propres à chaque jeu.

#### Gestion du catalogue

- [ ] Créer une structure de données pour les jeux.
- [ ] Préparer la gestion des images et médias.
- [ ] Préparer la gestion des versions.
- [ ] Préparer les statuts de publication.

#### Release 0.4

- [ ] Publier le nouveau catalogue.
- [ ] Publier les premières fiches de jeux complètes.
- [ ] Vérifier les performances et le référencement.

---

### Avril 2027 — Version 0.5 : Favoris, suivi et reviews

**Objectif :** permettre aux utilisateurs de suivre leurs jeux préférés et de partager leurs avis.

{{ progress_section }}

#### Favoris

- [ ] Ajouter un bouton « Ajouter aux favoris ».
- [ ] Créer `/account/favorites`.
- [ ] Enregistrer les favoris en base de données.
- [ ] Permettre de retirer un jeu des favoris.

#### Jeux suivis

- [ ] Ajouter un bouton « Suivre ce jeu ».
- [ ] Créer `/account/following`.
- [ ] Enregistrer les jeux suivis.
- [ ] Préparer les notifications liées aux jeux suivis.

#### Reviews

- [ ] Ajouter un système de notation de 1 à 5 étoiles.
- [ ] Ajouter un titre à une review.
- [ ] Ajouter un commentaire.
- [ ] Autoriser la lecture publique des reviews.
- [ ] Réserver la publication aux utilisateurs connectés.
- [ ] Autoriser la modification d'une review.
- [ ] Autoriser la suppression de sa propre review.
- [ ] Limiter à une review active par utilisateur et par jeu.
- [ ] Afficher la note moyenne.
- [ ] Afficher le nombre total de reviews.
- [ ] Ajouter le tri des reviews.
- [ ] Ajouter le signalement d'une review.
- [ ] Prévoir le badge « Joueur vérifié » uniquement si le statut peut être confirmé.

#### Release 0.5

- [ ] Tester les favoris et les suivis.
- [ ] Tester les reviews et les notes.
- [ ] Vérifier les permissions.
- [ ] Publier les fonctionnalités communautaires liées aux jeux.

---

## PHASE 3 — COMMUNAUTÉ ET ARCADE

{{ progress_section }}

### Mai 2027 — Version 0.6 : Community

**Objectif :** faire de Community un espace d'échange entre les joueurs et le studio.

{{ progress_section }}

#### Commentaires

- [ ] Ajouter les commentaires sur les articles.
- [ ] Ajouter les commentaires sur les publications communautaires.
- [ ] Ajouter les réponses aux commentaires.
- [ ] Ajouter la modification et suppression de ses commentaires.
- [ ] Ajouter le signalement des commentaires.

#### Votes et suggestions

- [ ] Créer une page de suggestions.
- [ ] Permettre de proposer une idée.
- [ ] Permettre de voter pour une proposition.
- [ ] Limiter à un vote par utilisateur et par proposition.
- [ ] Afficher le nombre de votes.
- [ ] Ajouter des catégories de suggestions.
- [ ] Ajouter des statuts : proposé, étudié, accepté, refusé, réalisé.

#### Activité communautaire

- [ ] Créer une page d'activité.
- [ ] Afficher les dernières publications.
- [ ] Afficher les dernières suggestions.
- [ ] Afficher les dernières discussions.
- [ ] Créer une page communautaire publique.

#### Release 0.6

- [ ] Tester les commentaires.
- [ ] Tester les votes.
- [ ] Tester les signalements.
- [ ] Publier la nouvelle Community.

---

### Juin 2027 — Version 0.7 : Arcade et mini-jeux

**Objectif :** créer une expérience ludique et récurrente sur Afendar, inspirée des mini-jeux et Google Doodles.

{{ progress_section }}

#### Arcade

- [ ] Créer la page `/arcade`.
- [ ] Créer un catalogue de mini-jeux.
- [ ] Créer une fiche par mini-jeu.
- [ ] Ajouter les instructions de jeu.
- [ ] Ajouter les images et illustrations.
- [ ] Ajouter un système de catégories.

#### Fonctionnement des jeux

- [x] Définir un système commun de lancement des mini-jeux.
- [ ] Ajouter la gestion des parties.
- [ ] Ajouter la sauvegarde des résultats.
- [ ] Ajouter la gestion des scores.
- [ ] Ajouter la validation serveur des scores.
- [ ] Ajouter un système anti-triche adapté aux mini-jeux.

#### Classements

- [ ] Créer `/arcade/leaderboards`.
- [ ] Ajouter les classements par mini-jeu.
- [ ] Ajouter les classements hebdomadaires.
- [ ] Ajouter les classements généraux.
- [ ] Afficher les profils des joueurs.
- [ ] Créer `/account/scores`.

#### Mini-jeu hebdomadaire

- [x] Prévoir un mini-jeu mis en avant.
- [x] Ajouter un système de rotation.
- [ ] Afficher le meilleur score de la semaine.
- [ ] Prévoir un historique des mini-jeux précédents.

#### Release 0.7

- [ ] Publier les premiers mini-jeux.
- [ ] Publier les classements.
- [ ] Tester la sauvegarde et la validation des scores.

---

## PHASE 4 — BIBLIOTHÈQUE ET NOTIFICATIONS

{{ progress_section }}

### Juillet 2027 — Version 0.8 : Bibliothèque personnelle

**Objectif :** permettre aux utilisateurs de retrouver les jeux auxquels ils ont accès.

{{ progress_section }}

#### Bibliothèque

- [ ] Créer `/account/library`.
- [ ] Afficher les jeux accessibles à l'utilisateur.
- [ ] Distinguer les jeux gratuits et les jeux possédés.
- [ ] Ajouter les jeux obtenus en bêta-test.
- [ ] Ajouter les jeux offerts ou attribués.
- [ ] Ajouter les informations de version.
- [ ] Ajouter les liens de téléchargement autorisés.

#### Droits d'accès

- [ ] Créer un système de droits d'accès aux jeux.
- [ ] Distinguer les droits permanents et temporaires.
- [ ] Gérer les accès aux bêtas privées.
- [ ] Gérer la révocation d'un accès.
- [ ] Protéger les téléchargements privés côté serveur.

#### Release 0.8

- [ ] Tester les droits d'accès.
- [ ] Tester la bibliothèque personnelle.
- [ ] Publier la bibliothèque.

---

### Août 2027 — Version 0.9 : Notifications

**Objectif :** permettre aux utilisateurs de ne rien manquer de l'actualité Afendar.

{{ progress_section }}

#### Notifications internes

- [ ] Créer `/account/notifications`.
- [ ] Ajouter les notifications de nouveaux jeux.
- [ ] Ajouter les notifications de mises à jour.
- [ ] Ajouter les notifications de changelog.
- [ ] Ajouter les notifications de nouveaux mini-jeux.
- [ ] Ajouter les notifications de réponses aux commentaires.
- [ ] Ajouter les notifications de réponses aux suggestions.
- [ ] Ajouter les notifications de modération.

#### Interface

- [ ] Ajouter une icône de notifications dans la navigation.
- [ ] Afficher le nombre de notifications non lues.
- [ ] Ajouter le marquage comme lu.
- [ ] Ajouter le marquage de toutes les notifications comme lues.
- [ ] Ajouter un historique des notifications.

#### Préférences

- [ ] Créer les préférences de notifications.
- [ ] Permettre de désactiver certaines catégories.
- [ ] Préparer les notifications par e-mail.
- [ ] Respecter les choix de confidentialité et de communication.

#### Release 0.9

- [ ] Tester chaque type de notification.
- [ ] Vérifier les préférences.
- [ ] Publier les notifications internes.

---

## PHASE 5 — STUDIO ET OUTILS D'ADMINISTRATION

{{ progress_section }}

### Septembre 2027 — Version 0.10 : Live, Blog et actualités

{{ progress_section }}

**Objectif :** rendre les contenus du studio plus dynamiques et centralisés.

#### Live

- [ ] Améliorer la page `/live`.
- [ ] Afficher le statut Twitch en direct.
- [ ] Intégrer le lecteur Twitch.
- [ ] Ajouter les liens YouTube.
- [ ] Afficher les dernières vidéos.
- [ ] Ajouter un calendrier des prochains lives.
- [ ] Ajouter les rediffusions.

#### Blog

- [ ] Améliorer la page `/blog`.
- [ ] Ajouter des catégories.
- [ ] Ajouter les images de couverture.
- [ ] Ajouter les articles mis en avant.
- [ ] Ajouter les dates de publication.
- [ ] Ajouter les commentaires si souhaité.

#### Actualités et changelogs

- [ ] Centraliser les actualités du studio.
- [ ] Ajouter les annonces de sorties.
- [ ] Ajouter les mises à jour de jeux.
- [ ] Ajouter les notes de version.
- [ ] Ajouter une page d'historique des versions.

#### Accueil

- [ ] Ajouter un jeu à la une.
- [ ] Ajouter le mini-jeu de la semaine.
- [ ] Ajouter le dernier changelog.
- [ ] Ajouter le statut Twitch.
- [ ] Ajouter les dernières actualités.
- [ ] Ajouter les dernières activités communautaires.

#### Release 0.10

- [ ] Vérifier les intégrations Twitch et YouTube.
- [ ] Tester la publication des actualités.
- [ ] Publier le nouvel accueil et les pages de contenus.

---

### Octobre 2027 — Version 0.11 : Back-office et modération

**Objectif :** permettre à l'équipe Afendar de gérer la plateforme sans intervention technique permanente.

{{ progress_section }}

#### Administration

- [x] Créer un espace `/admin`.
- [ ] Ajouter une gestion des utilisateurs.
- [ ] Ajouter une gestion des jeux.
- [ ] Ajouter une gestion des articles.
- [ ] Ajouter une gestion des changelogs.
- [ ] Ajouter une gestion des mini-jeux.
- [ ] Ajouter une gestion des publications communautaires.

#### Modération

- [ ] Créer une liste des signalements.
- [ ] Ajouter la modération des reviews.
- [ ] Ajouter la modération des commentaires.
- [ ] Ajouter la modération des suggestions.
- [ ] Ajouter la suspension temporaire d'un utilisateur.
- [ ] Ajouter la gestion des comptes bloqués.
- [ ] Conserver un historique des actions de modération.

#### Rôles et permissions

- [x] Définir les rôles administrateur et modérateur.
- [ ] Définir les permissions de chaque rôle.
- [ ] Séparer les droits de modération des droits de possession des jeux.
- [ ] Protéger toutes les actions administratives côté serveur.

#### Release 0.11

- [ ] Tester les rôles et permissions.
- [ ] Tester les outils de modération.
- [ ] Vérifier les journaux d'administration.
- [ ] Publier le back-office.

---

## PHASE 6 — STABILISATION ET LANCEMENT

{{ progress_section }}

### Novembre 2027 — Version 1.0 : Lancement public Afendar

**Objectif :** publier une plateforme stable, cohérente et prête à accueillir une communauté.

{{ progress_section }}

#### Qualité

- [ ] Corriger les bugs bloquants.
- [ ] Tester tous les parcours utilisateurs.
- [ ] Tester les formulaires.
- [ ] Tester les fonctionnalités mobiles.
- [ ] Vérifier les performances.
- [ ] Vérifier les temps de chargement.
- [ ] Tester les erreurs serveur.
- [ ] Tester les sauvegardes de données.

#### Sécurité et conformité

- [ ] Vérifier les contrôles d'accès.
- [ ] Vérifier la protection des comptes.
- [ ] Vérifier les permissions des téléchargements.
- [ ] Vérifier la protection anti-spam.
- [ ] Vérifier les règles de confidentialité.
- [ ] Finaliser les mentions légales.
- [ ] Finaliser la politique de confidentialité.
- [ ] Finaliser les conditions d'utilisation.
- [ ] Vérifier les mécanismes de suppression de compte et les demandes liées aux données personnelles.

#### Référencement et communication

- [ ] Optimiser les métadonnées.
- [ ] Ajouter les aperçus sociaux.
- [ ] Vérifier le sitemap XML.
- [ ] Vérifier les fichiers robots.txt.
- [ ] Préparer les annonces de lancement.
- [ ] Préparer une page de présentation d'Afendar.
- [ ] Préparer les visuels de lancement.

#### Mise en production

- [ ] Déployer la version candidate.
- [ ] Effectuer une phase de bêta-test.
- [ ] Corriger les derniers problèmes.
- [ ] Effectuer une sauvegarde complète.
- [ ] Déployer la version 1.0.
- [ ] Publier l'annonce officielle.
- [ ] Surveiller les erreurs après lancement.

#### Release 1.0

- [ ] Valider les fonctionnalités principales.
- [ ] Valider la stabilité de la plateforme.
- [ ] Ouvrir Afendar au public.

<!-- progress-stop -->

---

## APRÈS LA VERSION 1.0 — ÉVOLUTIONS FUTURES

Ces fonctionnalités ne sont pas obligatoires pour le lancement initial. Elles pourront faire l'objet de nouvelles versions.

### Boutique et monétisation

- [ ] Créer une boutique de jeux.
- [ ] Ajouter un système de panier.
- [ ] Intégrer un prestataire de paiement.
- [ ] Gérer les commandes.
- [ ] Gérer les remboursements.
- [ ] Ajouter les factures et reçus.
- [ ] Relier les achats à la bibliothèque.
- [ ] Ajouter les promotions et codes de réduction.

### Bêta-tests

- [ ] Créer un système de candidatures aux bêta-tests.
- [ ] Ajouter des invitations.
- [ ] Gérer les accès temporaires.
- [ ] Ajouter un espace de retours de bêta-test.
- [ ] Permettre de remonter des bugs.
- [ ] Ajouter des questionnaires.

### Fonctionnalités communautaires avancées

- [ ] Ajouter des badges et récompenses.
- [ ] Ajouter des succès.
- [ ] Ajouter des niveaux de profil.
- [ ] Ajouter des événements communautaires.
- [ ] Ajouter des défis Arcade.
- [ ] Ajouter des profils personnalisables.

### Fonctionnalités studio avancées

- [ ] Ajouter une page dédiée à l'équipe.
- [ ] Ajouter une page de recrutement.
- [ ] Ajouter un espace presse.
- [ ] Ajouter un kit média téléchargeable.
- [ ] Ajouter une page de présentation des projets.
- [ ] Ajouter une newsletter.

---

## RÈGLES DE RELEASE

Pour chaque version mensuelle :

- [ ] Les fonctionnalités prévues sont terminées ou explicitement reportées.
- [ ] Les tests de non-régression sont effectués.
- [ ] Les problèmes bloquants sont corrigés.
- [ ] Les migrations de base de données sont vérifiées.
- [ ] Une sauvegarde est disponible.
- [ ] Le changelog de la version est rédigé.
- [ ] La version est déployée en production.
- [ ] Les éventuels problèmes après déploiement sont surveillés.

**Principe :** mieux vaut sortir une release mensuelle plus petite et fiable qu'une grosse version instable.

---

## ANNONCES SUR SERVEUR DISCORD (DEVLOGS une fois par mois)

- [x] Les doodles [release 0.7](#juin-2027-version-07-arcade-et-mini-jeux)
- [ ] Le profil et l'espace personnel [release 0.2](#janvier-2027-version-02-authentification-et-comptes) et [release 0.3](#fevrier-2027-version-03-profils-et-espace-personnel)
- [ ] Mes jeux Favori et Mes jeux suivi et Reviews [release 0.5](#avril-2027-version-05-favoris-suivi-et-reviews)
- [ ] Amélioration du catalogue et de la page des jeux [release 0.4](#mars-2027-version-04-catalogue-de-jeux)
- [ ] Commentaires votes et suggestions [release 0.6](#mai-2027-version-06-community)
- [ ] Bibliothèque dans mon compte [release 0.8](#juillet-2027-version-08-bibliotheque-personnelle)
- [ ] Notifications [release 0.9](#aout-2027-version-09-notifications)
- [ ] Live, Blog et actualités [release 0.10](#septembre-2027-version-010-live-blog-et-actualites)
---
- [ ] **Mise en ligne afendar-games.fr novembre 2027** `release 1.0`

---
- [ ] Boutique et monétisation `release-1.6`
- [ ] Beta tests `release-1.4`
- [ ] Badges et récompenses `release-1.2`
- [ ] Succès `release-1.3`
- [ ] Niveaux de profil `release-1.5`
- [ ] Newsletter `release-1.1`