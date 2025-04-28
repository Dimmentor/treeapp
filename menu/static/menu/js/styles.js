function toggleMenu(button) {
    const submenu = button.nextElementSibling;
    if (submenu.style.display === "none") {
        submenu.style.display = "block";
        button.textContent = "-";
    } else {
        submenu.style.display = "none";
        button.textContent = "+";
    }
}