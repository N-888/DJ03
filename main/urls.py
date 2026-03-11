from django.urls import path  # Импортируем path для создания маршрутов
from . import views  # Импортируем views, чтобы вызывать функции страниц

urlpatterns = [  # Список маршрутов приложения main
    path('', views.index, name='home'),  # Главная страница по адресу /
    path('newnewnew/', views.new, name='page2'),  # Второстепенная страница по адресу /newnewnew/
]
