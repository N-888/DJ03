from django.urls import path  # Импортируем path для маршрутов
from . import views  # Импортируем views

urlpatterns = [  # Список маршрутов приложения news
    path('', views.home, name='news_home'),  # Страница новостей по адресу /news/
]
