from django.contrib import admin  # Импортируем admin, чтобы регистрировать модели
from .models import NewsPost  # Импортируем модель NewsPost из models.py

@admin.register(NewsPost)  # Регистрируем модель NewsPost в админке через декоратор
class NewsPostAdmin(admin.ModelAdmin):  # Создаём настройки отображения модели в админке
    list_display = ('title', 'author', 'pub_date')  # Показываем колонки в списке новостей
    list_filter = ('pub_date', 'author')  # Добавляем фильтры справа
    search_fields = ('title', 'short_description', 'text', 'author__username')  # Добавляем поиск по полям и по username автора
