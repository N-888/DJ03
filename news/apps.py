from django.apps import AppConfig  # Импортируем AppConfig для настройки приложения

class NewsConfig(AppConfig):  # Создаём конфигурацию приложения news
    default_auto_field = 'django.db.models.BigAutoField'  # Указываем тип поля id по умолчанию
    name = 'news'  # Указываем имя приложения
