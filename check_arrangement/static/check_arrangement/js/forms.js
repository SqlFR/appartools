// Ajoute class label-input a la div qui contient label/input ds le form add issue et add apart
const formDivs = document.querySelectorAll('.form-add > div');
formDivs.forEach((div) => {
    div.classList.add('label-input')
})

