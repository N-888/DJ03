from pathlib import Path  # Импортируем Path, чтобы удобно строить пути к папкам проекта

BASE_DIR = Path(__file__).resolve().parent.parent  # Получаем путь до корня проекта (где manage.py)

SECRET_KEY = 'django-insecure-change-me-to-a-random-secret-key'  # Задаём секретный ключ проекта для подписи куки и защиты

DEBUG = True  # Включаем режим отладки для разработки

ALLOWED_HOSTS: list[str] = []  # Разрешённые хосты, для локальной разработки оставляем пустым

INSTALLED_APPS = [  # Список подключённых приложений
    'django.contrib.admin',  # Админ-панель Django
    'django.contrib.auth',  # Пользователи и авторизация
    'django.contrib.contenttypes',  # Типы контента для моделей
    'django.contrib.sessions',  # Сессии (нужны для логина в админке)
    'django.contrib.messages',  # Сообщения Django
    'django.contrib.staticfiles',  # Работа со статическими файлами
    'main',  # Подключаем приложение main
    'news',  # Подключаем приложение news
]

MIDDLEWARE = [  # Слои обработки запросов
    'django.middleware.security.SecurityMiddleware',  # Базовая безопасность
    'django.contrib.sessions.middleware.SessionMiddleware',  # Сессии
    'django.middleware.common.CommonMiddleware',  # Общие настройки запросов
    'django.middleware.csrf.CsrfViewMiddleware',  # CSRF-защита форм
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Авторизация пользователя
    'django.contrib.messages.middleware.MessageMiddleware',  # Сообщения
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Защита от clickjacking
]

ROOT_URLCONF = 'zerocoder.urls'  # Указываем главный файл маршрутов проекта

TEMPLATES = [  # Настройки шаблонов
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # Движок шаблонов Django
        'DIRS': [],  # Дополнительные папки шаблонов, нам не нужно, потому что используем templates внутри приложений
        'APP_DIRS': True,  # Разрешаем искать шаблоны в папках templates/ внутри приложений
        'OPTIONS': {
            'context_processors': [  # Процессоры контекста, доступные во всех шаблонах
                'django.template.context_processors.debug',  # Добавляет debug переменные
                'django.template.context_processors.request',  # Добавляет request (нужно для активного пункта меню)
                'django.contrib.auth.context_processors.auth',  # Добавляет user
                'django.contrib.messages.context_processors.messages',  # Добавляет messages
            ],
        },
    },
]

WSGI_APPLICATION = 'zerocoder.wsgi.application'  # WSGI-точка входа

ASGI_APPLICATION = 'zerocoder.asgi.application'  # ASGI-точка входа

DATABASES = {  # Настройки базы данных
    'default': {  # База данных по умолчанию
        'ENGINE': 'django.db.backends.sqlite3',  # Используем SQLite
        'NAME': BASE_DIR / 'db.sqlite3',  # Путь к файлу базы данных
    }
}

AUTH_PASSWORD_VALIDATORS = [  # Валидаторы сложности паролей
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},  # Проверка похожести на логин
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},  # Проверка минимальной длины
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},  # Запрет самых популярных паролей
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},  # Запрет пароля только из цифр
]

LANGUAGE_CODE = 'ru'  # Ставим русский язык интерфейса (в том числе админки)

TIME_ZONE = 'Europe/Amsterdam'  # Ставим часовой пояс

USE_I18N = True  # Включаем интернационализацию

USE_TZ = True  # Включаем поддержку временных зон

STATIC_URL = 'static/'  # URL-префикс для статики

STATICFILES_DIRS = [  # Папки, где Django будет искать статику
    BASE_DIR / 'static',  # Подключаем папку static рядом с manage.py
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'  # Тип поля id по умолчанию
