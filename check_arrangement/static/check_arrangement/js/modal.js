// modal delete apart
document.addEventListener('DOMContentLoaded', (event) => {
    const modal = document.getElementById("deleteModal");
    const confirmDeleteBtn = document.getElementById("confirmDelete");
    const span = document.getElementsByClassName("close-delete")[0];
    let deleteUrl = '';

    document.querySelectorAll('.btn-delete').forEach(button => {
        button.addEventListener('click', () => {
            deleteUrl = `/check-apartment/delete_apartment/${button.dataset.id}`;
            modal.style.display = "block";
        });
    });

    confirmDeleteBtn.onclick = () => {
        window.location.href = deleteUrl;
    };

    document.getElementById("cancelDelete").onclick = () => {
        modal.style.display = "none";
    };

    span.onclick = () => {
        modal.style.display = "none"
    };

    window.onclick = (event) => {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    };
});
