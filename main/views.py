from django.shortcuts import render  # Импортируем render, чтобы возвращать HTML-шаблоны

def index(request):  # Создаём обработчик главной страницы
    return render(request, 'main/index.html')  # Возвращаем шаблон главной страницы

def new(request):  # Создаём обработчик второстепенной страницы
    return render(request, 'main/new.html')  # Возвращаем шаблон второстепенной страницы
