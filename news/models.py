from django.db import models  # Импортируем models, чтобы описывать таблицы базы данных
from django.contrib.auth.models import User  # Импортируем User, чтобы связать новость с автором
from django.utils import timezone  # Импортируем timezone, чтобы ставить текущую дату по умолчанию

class NewsPost(models.Model):  # Создаём модель, которая станет таблицей в базе данных
    title = models.CharField('Название новости', max_length=50)  # Поле названия новости
    short_description = models.CharField('Краткое описание новости', max_length=200)  # Поле краткого описания
    text = models.TextField('Новость')  # Поле полного текста новости
    pub_date = models.DateTimeField('Дата публикации', default=timezone.now)  # Поле даты публикации с текущей датой по умолчанию
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', related_name='news_posts')  # Поле автора как связь с пользователем

    def __str__(self) -> str:  # Создаём строковое представление объекта
        return self.title  # Возвращаем название новости

    class Meta:  # Настройки отображения в админке
        verbose_name = 'Новость'  # Название одной записи
        verbose_name_plural = 'Новости'  # Название списка записей
        ordering = ['-pub_date']  # Сортировка: новые сверху
