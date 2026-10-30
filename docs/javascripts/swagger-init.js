
function initSwagger() {
  const container = document.querySelector("#swagger-ui");

  if (!container || typeof SwaggerUIBundle === "undefined") {
    return;
  }

  const specUrl = container.dataset.openapi;

  if (!specUrl) {
    return;
  }

  SwaggerUIBundle({
    url: specUrl,
    dom_id: "#swagger-ui",
    deepLinking: true,
    docExpansion: "list",
    filter: true,
    displayRequestDuration: true,

    // Consultation uniquement : pas d'exécution de requêtes.
    supportedSubmitMethods: [],

    // Évite l'envoi de la spécification à un service tiers.
    validatorUrl: null
  });
}

// Compatible avec la navigation instantanée de Material.
if (typeof document$ !== "undefined") {
  document$.subscribe(initSwagger);
} else {
  document.addEventListener("DOMContentLoaded", initSwagger);
}
