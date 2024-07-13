// Désactive les boutons delete issue après le click
document.addEventListener('DOMContentLoaded', () => {
    function disabledButtonAfterClick() {
        const allBtnDelete = document.querySelectorAll('.btn-delete');

        allBtnDelete.forEach(link => {
            link.addEventListener('click', (e) => {
                    const linkElement = e.currentTarget
                    linkElement.classList.add('disable-link')
            });
        });
    }
    disabledButtonAfterClick();
});