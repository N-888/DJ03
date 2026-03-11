from django.conf import settings  # Импортируем settings, чтобы ссылаться на AUTH_USER_MODEL
from django.db import migrations, models  # Импортируем migrations и models для описания миграции
import django.db.models.deletion  # Импортируем deletion для on_delete поведения
import django.utils.timezone  # Импортируем timezone для default значения даты

class Migration(migrations.Migration):  # Создаём класс миграции

    initial = True  # Указываем, что это начальная миграция приложения

    dependencies = [  # Указываем зависимости миграции
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),  # Говорим: нужна таблица пользователей, чтобы связать автора
    ]

    operations = [  # Описываем операции, которые нужно выполнить
        migrations.CreateModel(  # Операция создания таблицы
            name='NewsPost',  # Имя модели
            fields=[  # Поля таблицы
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),  # Автоматическое поле id
                ('title', models.CharField(max_length=50, verbose_name='Название новости')),  # Поле title
                ('short_description', models.CharField(max_length=200, verbose_name='Краткое описание новости')),  # Поле short_description
                ('text', models.TextField(verbose_name='Новость')),  # Поле text
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата публикации')),  # Поле pub_date
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news_posts', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),  # Поле author
            ],
            options={  # Настройки модели
                'verbose_name': 'Новость',  # Название одной записи
                'verbose_name_plural': 'Новости',  # Название списка
                'ordering': ['-pub_date'],  # Сортировка по дате
            },
        ),
    ]
