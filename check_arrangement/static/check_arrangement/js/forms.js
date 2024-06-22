// Ajoute class label-input a la div qui contient label/input ds le form add issue et add apart
const formDivs = document.querySelectorAll('.form-add > div');
formDivs.forEach((div) => {
    div.classList.add('label-input')
})

// Gestion de la modal lors de l'ajout d'incident
const modalSuccessIssue = document.getElementById('add-issue-modal-success');
document.addEventListener("DOMContentLoaded", function() {
    // Récupère le paramètre dans l'URL
    const params = new URLSearchParams(window.location.search);
    if (params.get('success')) {
        modalSuccessIssue.classList.add('show');
        setInterval(function() {
            modalSuccessIssue.classList.remove('show');
        }, 2000)

    }
})