// Ajoute class label-input a la div qui contient label/input ds le form
const formDivs = document.querySelectorAll('#form-add-apart > div');
formDivs.forEach((div) => {
    div.classList.add('label-input')
})
