from django.contrib import admin  # Импортируем админку
from django.urls import path, include  # Импортируем path для маршрутов и include для подключения маршрутов приложений

urlpatterns = [  # Список маршрутов проекта
    path('admin/', admin.site.urls),  # Админка по адресу /admin/
    path('', include('main.urls')),  # Маршруты главного приложения по корню сайта
    path('news/', include('news.urls')),  # Маршруты новостей по адресу /news/
]
