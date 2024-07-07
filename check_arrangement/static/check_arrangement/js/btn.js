const boxArrowFormAddApart = document.getElementById('box-arrow-form-add-apart');

boxArrowFormAddApart.addEventListener('click', () => {
    boxArrowFormAddApart.classList.toggle('active');
    const formAddApart = document.getElementById('form-add-apart');
    formAddApart.classList.toggle('show-form-add-apart')
})

// const boxesArrow = document.querySelectorAll('.box-arrow');
//
// boxesArrow.forEach(box => {
//     box.addEventListener('click', e => {
//         e.target.classList.toggle('active');
//     })
// })
