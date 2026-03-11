#!/usr/bin/env python  # Указываем, что файл можно запускать как скрипт в Unix-системах
import os  # Импортируем os, чтобы работать с переменными окружения
import sys  # Импортируем sys, чтобы работать с аргументами командной строки

def main() -> None:  # Создаём главную функцию запуска Django-команд
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zerocoder.settings')  # Указываем Django, где лежат настройки проекта
    try:  # Начинаем блок, в котором пробуем импортировать Django
        from django.core.management import execute_from_command_line  # Импортируем функцию запуска команд Django
    except ImportError as exc:  # Если Django не установлен или не найден
        raise ImportError(  # Поднимаем понятную ошибку
            "Couldn't import Django. Are you sure it's installed and "  # Подсказываем возможную причину
            "available on your PYTHONPATH environment variable? Did you "  # Подсказываем про PYTHONPATH/окружение
            "forget to activate a virtual environment?"  # Подсказываем про виртуальное окружение
        ) from exc  # Привязываем оригинальную ошибку
    execute_from_command_line(sys.argv)  # Запускаем команду, которую ты ввела в терминале

if __name__ == '__main__':  # Проверяем, что файл запущен напрямую
    main()  # Вызываем главную функцию
