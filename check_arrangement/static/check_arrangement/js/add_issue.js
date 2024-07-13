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

// Désactive bouton après le clic
function disabledButtonAfterClick() {
    const btnAddIssue = document.getElementById('btn-add-issue');
    setTimeout(() => {
        btnAddIssue.disabled = true;
    }, 10)

    setTimeout(() => {
        btnAddIssue.disabled = false;
    }, 1000);
}

