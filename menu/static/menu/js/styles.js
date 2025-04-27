function toggleMenu(button) {
    const submenu = button.nextElementSibling; // Получаем следующий элемент (подменю)
    if (submenu.style.display === "none") {
        submenu.style.display = "block"; // Показываем подменю
        button.textContent = "-"; // Меняем знак на минус
    } else {
        submenu.style.display = "none"; // Скрываем подменю
        button.textContent = "+"; // Меняем знак на плюс
    }
}