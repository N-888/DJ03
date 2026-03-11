from django.apps import AppConfig  # Импортируем AppConfig для настройки приложения

class MainConfig(AppConfig):  # Создаём конфигурацию приложения main
    default_auto_field = 'django.db.models.BigAutoField'  # Указываем тип поля id по умолчанию
    name = 'main'  # Указываем имя приложения
