import os  # Импортируем os, чтобы работать с переменными окружения
from django.core.wsgi import get_wsgi_application  # Импортируем функцию создания WSGI-приложения

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zerocoder.settings')  # Указываем Django, где находятся настройки проекта

application = get_wsgi_application()  # Создаём WSGI-приложение
