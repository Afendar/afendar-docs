hide:
    - toc
    - navigation

# `AR01` Architecture générale

<div class="diagram-box">
    <div class="box">
        <i class="fas fa-desktop"></i>
        <p>
            <span>
                <code><span>afendar-admin</span></code>
            </span>
        </p>
        <p>
            <small>Vue.js . Liste . Formulaire . Prévisualisation . Upload</small>
        </p>
    </div>
    <div class="box without-borders">
        <i class="fa-solid fa-up-down"></i>
        <p>
           <small>API REST — FOSRestBundle</small>
        </p>
    </div>
    <div class="box">
        <i class="fa-solid fa-server"></i>
        <p>
            <span>
                <code><span>afendar-api</span></code>
            </span>
        </p>
        <p>
            <small>
                Doodle . Règles de diffusion . Validation . Persistence
            </small>
        </p>
        <p>
            <small>
                Symfony . Doctrine . Workflow si nécessaire
            </small>
        </p>
    </div>
    <div class="box-row">
        <div class="box box-col">
            <i class="fas fa-database"></i>
            <p><span>MySQL</span></p>
            <p><small>Données et configurations</small></p>
        </div>
        <div class="box box-col">
            <i class="fas fa-database"></i>
            <p><span>Redis</span></p>
            <p><small>Cache</small></p>
        </div>
    </div>
    <div class="box">
        <i class="fas fa-globe"></i>
        <p>
            <span>
                <code><span>afendar-front</span></code>
            </span>
        </p>
        <p>
            <small>
                Symfony . Client HTTP . Contrôleur . Twig . Bandeau public
            </small>
        </p>
    </div>
</div>