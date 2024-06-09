// script.js
document.addEventListener('DOMContentLoaded', (event) => {
    const modal = document.getElementById("deleteModal");
    const span = document.getElementsByClassName("close")[0];
    const confirmDeleteBtn = document.getElementById("confirmDelete");
    let deleteUrl = '';

    document.querySelectorAll('.delete-btn').forEach(button => {
        button.addEventListener('click', () => {
            deleteUrl = `/check-apartment/delete_apartment/${button.dataset.id}`;
            modal.style.display = "block";
        });
    });

    span.onclick = () => {
        modal.style.display = "none";
    };

    confirmDeleteBtn.onclick = () => {
        window.location.href = deleteUrl;
    };

    document.getElementById("cancelDelete").onclick = () => {
        modal.style.display = "none";
    };

    window.onclick = (event) => {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    };
});
