(() => { // Создаём самовызывающуюся функцию, чтобы всё было аккуратно
    const body = document.body; // Берём body, чтобы менять атрибут темы
    const toggle = document.getElementById("themeToggle"); // Ищем кнопку переключения темы
    const icon = document.getElementById("themeIcon"); // Ищем иконку внутри кнопки
    const text = document.getElementById("themeText"); // Ищем текст внутри кнопки

    const storageKey = "site-theme"; // Ключ, под которым будем хранить тему в localStorage

    const applyTheme = (theme) => { // Функция применения темы
        body.setAttribute("data-theme", theme); // Устанавливаем атрибут data-theme

        if (theme === "dark") { // Если тёмная тема
            icon.className = "bi bi-sun"; // Ставим иконку солнца
            text.textContent = "Светлая"; // Пишем “Светлая”
        } else { // Если светлая тема
            icon.className = "bi bi-moon-stars"; // Ставим иконку луны
            text.textContent = "Тёмная"; // Пишем “Тёмная”
        } // Закрываем условие
    }; // Закрываем функцию

    const savedTheme = localStorage.getItem(storageKey); // Берём сохранённую тему, если она есть
    const initialTheme = savedTheme ? savedTheme : "light"; // Если темы нет, ставим светлую
    applyTheme(initialTheme); // Применяем стартовую тему

    if (toggle) { // Проверяем, что кнопка существует
        toggle.addEventListener("click", () => { // Вешаем обработчик клика
            const current = body.getAttribute("data-theme"); // Получаем текущую тему
            const next = current === "dark" ? "light" : "dark"; // Вычисляем следующую тему
            localStorage.setItem(storageKey, next); // Сохраняем тему
            applyTheme(next); // Применяем новую тему
        }); // Закрываем обработчик
    } // Закрываем проверку
})(); // Запускаем функцию
