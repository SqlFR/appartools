// Bouton pour ouvrir formulaire Ajouter appartement
const boxArrowFormAddApart = document.getElementById('box-arrow-form-add-apart');

boxArrowFormAddApart.addEventListener('click', () => {
    boxArrowFormAddApart.classList.toggle('active');
    const formAddApart = document.getElementById('form-add-apart');
    formAddApart.classList.toggle('show-form-add-apart')
})

// Bouton valider formulaire Ajouter appartement
const btnConfirmFormAddApart = document.getElementById('btn-form-add-apart');

btnConfirmFormAddApart.addEventListener('click', () => {
    btnConfirmFormAddApart.classList.add('disable-link');
    setTimeout(() => {
    btnConfirmFormAddApart.classList.remove('disable-link');
    }, 1000)
})

