from django.shortcuts import render  # Импортируем render для возврата HTML-шаблонов
from .models import NewsPost  # Импортируем NewsPost, чтобы получать новости из базы

def home(request):  # Создаём обработчик страницы /news/
    news = NewsPost.objects.all()  # Получаем все новости из базы данных
    return render(request, 'news/news.html', {'news': news})  # Передаём новости в шаблон
