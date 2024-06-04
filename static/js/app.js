document.addEventListener("DOMContentLoaded", function() {
        const issueTypeSelect = document.getElementById("id_issue_type");
        const descriptionField = document.getElementById("id_description");

        // Fonction pour afficher ou masquer le champ de description
        function toggleDescriptionField() {
            if (issueTypeSelect.value === "") {
                descriptionField.style.display = "none";
            } else {
                descriptionField.style.display = "block";
            }
        }

        // Écouteur d'événements pour détecter les changements dans le champ de type d'incident
        issueTypeSelect.addEventListener("change", toggleDescriptionField);

        // Assurez-vous que le champ de description est initialisé correctement au chargement de la page
        toggleDescriptionField();
    });