// Bouton formulaire Ajouter appartement
const boxArrowFormAddApart = document.getElementById('box-arrow-form-add-apart');

boxArrowFormAddApart.addEventListener('click', () => {
    boxArrowFormAddApart.classList.toggle('active');
    const formAddApart = document.getElementById('form-add-apart');
    formAddApart.classList.toggle('show-form-add-apart')
})

