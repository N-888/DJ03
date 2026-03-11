import os  # Импортируем os, чтобы работать с переменными окружения
from django.core.asgi import get_asgi_application  # Импортируем функцию создания ASGI-приложения

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zerocoder.settings')  # Указываем Django, где находятся настройки проекта

application = get_asgi_application()  # Создаём ASGI-приложение
