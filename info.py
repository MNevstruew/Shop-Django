# НЕ ЗАБЫВАТЬ ЗАНЯТЫЕ (,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,)
# НЕ ЗАБЫВАЙ ЧТО ВСЕГДА ЕСТЬ ДОКУМЕНТАЦИЯ!!!!!!!!!
# 
# shift+als+f - редактировать - выравнивать строки
# 
# засширение Django Template
# Если всё сломалось на САЙТЕ иногда помогает (CTRL + F5)!!!!

# если не работает то доустановить
# python -m pip install --upgrade --force-reinstall pip
#
# Для обновления python в терминале команда:
# python3 -m venv --upgrade env
#
# 
# 
# Мультивалютность - работает с ценами и прочим
# django money pypi - https://pypi.org/project/django-money/ 
# 
# 
#
# Ссайт с документацией
# https://unfoldadmin.com/ - типа для админки что ли
# Там есть Docs
# там есть - Quickstart - по сути там нушно в settings добавить все что там есть
# для установки
# pip install django-unfold
# 
# Работа с картинками
# pip install pillow
#
# Иконки
# google icons
# 
# 
# Чтоб точно можно было подключится к старому проекту
# .venv\Scripts\activate
# 
# 

# Сборка команд типа по порядку
# >create - venv и актуальный пайтон (Создать окружение)
# .venv\Scripts\activate - точно все запустим
# pip install django
# django-admin startproject Site .                           (пробел точка обязательно) (Site - это название - может быть любым)
# python manage.py startapp appPages                         (создали приложение)
# python manage.py migrate                                   (Подключили таблицы)      
# python manage.py createsuperuser                           (Создание суперпользователя)
# имя пишем - почту пропускаем - пароль пишем и подтверждаем
# В соданном приложении - тут appPages - создаем 
# папка templates 
# папку - Static - в ней создаем
# папку css - в ней файл - style.css
# и папку photos
# в папку Site - файл settings.py - в нем 
# INSTALLED_APPS - добавляем наш проект - тут 'appPages'
# а также пишем в низу 'ru-ru' и 'Europe / Moscow'
# python manage.py runserver - запустить
# ctrl + c - остановить
# 
# python manage.py makemigrations                                     (пишем чтоб что-то добавил)
# python manage.py migrate                                            (всегда после чтоб проверить что сделалось и зафиксировать)   
# 
# 
# 
# 
# 
# 04.06
# appPages - models.py
# 
# 
# 
# 
# 


# >create - environment - создать среду ///потом vens /// выпираем последнюю версию пайтона
# создает терминал - пишем - .venv (можно нажать tab питон знает команды)
# Устанавливаем django - pip install django
# pip list - проверка установленного
# пишем в терминале - django-admin startproject (Site - это название проекто - придумай сам)
# там же пишем ( .) - пробел точка.
# python manage.py runserver - чтоб остановить - ctrl + c
# views.py - базовое название
# * - импортировать всё


# python manage.py startapp (pages) - создать новый проект - (pages) - название

# там создаем папку templares - там будут храниться все html
# и папку static - там будут храниться все стили и скрипты

# создаем главную страницу - home.html - иконка будет dj - не меняем, пока толка нет
# Если показывает dj - django html - то внизу справа нажимаем на html - и вверху в поисковике вводим html
# Каждый раз когда мы создоем приложение всегда должны его написать в SITE - settings.py - INSTALLED_APPS

# В папку - Site - urls.py - from pages.views import * и добавляем ниже путь - path('', page_home)



# шаг 1
# Создания приложения
# python manage.py startapp (название)

# шаг 2
# Регистрация приложения
# SITE - settings.py - INSTALLED_APPS - 'pages',
# необходимо добавить в этот список - название созданного приложения

# шаг 3
# Внутри приложения необходимо создать папку - "templates"
# templates - папка которая хранит html файлы

# шаг 4
# Создаем файлы html - внутри папки templates - внутри приложения

# шаг 5
# Внутри приложения создаем файл views.py
# создание функции
# функция должна вернуть render(request(обязательно), '')


# шаг 6
# регестрация views в urls.py


# если стоит django то мы пишем

# Расширения Django и Django Django Template Support


# .venv/Scrips/activate тк не доверяем терминалу запускаем принудительно
# python manage.py migrate - запоминаем команду - там 18 таблиц - говорят будем с этим работать очень часто - чтобы проверить все ли ок
# Надо создать супер пользователя - всегда через терминал - python manage.py createsuperuser
# Username (leave blank to use 'user'): admin - предлагает содать ник
# email address: - создать почку
# password: - пароль будет невидим в пользу беззомасности


# Site - settings.py - LANGUAGE_CODE = 'ru-ru' - переводим на русский
# Site - settings.py - TIME_ZONE = 'Europe/Moscow' - настраиваем время


# Создавая папку нужно её зарегестрировать в - settings.py - INSTALLED_APPS = 'tables',(например)

# python manage.py startapp appModels - создаем приложение
# регестрируем в settings.py - INSTALLED_APPS = 'appModels'

# Далее там работале в файле tables - models.py
# Можно русифицировать колонки - (verbose_name="Описание")

# всегда нужно получать сертификат - те убеждаться кадлый раз что все сделали норм и ошибок нет - python manage.py makemigrations
# django - анализирует все введенное - и если все норм то код работает
# каждый раз надо эту херню писать
# Сертификаты получаем тольк в .models

# python manage.py migrate  - чтобы проверить все ли ок


# потом работали в - tables - admin.py
# надо зарегестрировать то что мы делали в моделс
# пишем from .models import Datas - рассказывая где мы будем работать (Datas это название)
# @admin.register(Datas)
# class DatasAdmin(admin.ModelAdmin):
#    pass
# В admin.py - настраиваем как будет выглядеть наша таблица


# Русификация плашки с названием приложения которое мы сождали - к примеру - (AppModels или tables)
# в папке приложения в файле apps.py
# appModels(или table) - apps.py -

# и там внутри

# class AppmodelsConfig(AppConfig):
#    default_auto_field = 'django.db.models.BigAutoField'
#    name = 'appModels'
#    verbose_name= "Модели"                     - ПИШЕТСЯ ТОЛЬКО ЭТА СТРОКА - она переводит то что надо

# Русификация самой таблицы
# 
# Переходим в appModels - models.py
#
#     class Meta:
#       verbose_name = 'Продукт'
#       verbose_name_plural = 'Продукты'
# 
# в папке appModels - создали папку templates - создали products.html
# в нем пишем - html:5
# {% load static %} 
# 
# в папке appModels - создали папку static - создали style.css
# 
# далее работаем в в папке appModels в файле views.py
# там мы создадим page_prudects
#
# не забываем передать данные в Site - urls.py
#
# там мы его подключаем
# from appModels.views import *
# а ниже
# path('', page_products)
# 
# 
# 
# В templates - создали файл - это будет базовый шаблон - base.html
# {% load static %}   - самая верхняя строчка должна быть
# Поозже создали home.html
# 
# 
# потом в файле appPages - views.py:
# def page_home(request):
#    return render(request, 'home.html')
# и привязываем это в Site - urls.py
# from appPages.views import page_home
# path('', page_home
# 
# 
# потом работали в appPages - models.py
# 
# 
# потом работали в appPages - admin.py
# 
# from .models import (
#    Contacts
# )

# @admin.register(Contacts)
# class ContactsAdmin(admin.ModelAdmin):
#    list_display = ['email', 'phone', 'city']
#    list_display_links = ['email', 'phone', 'city']
#    list_filter = ['city']
#    search_fields = ['email', 'city']
# 
# потом вернулись в vievw.py
# 
# from .models import(
#    Contacts
# )
# 
# def page_contacts(request):
#    contacts = Contacts.objects.all()
#    return render(request, 'contacts.html', {
#        'contacts': contacts
#        })
# 
# дальше contacts.html
# 
# Настроили подвязку информации и 
# Настроили чтоб вместо none - там где пропуск - тире (-) показывал
# {% block content %}
#    <div class="cards">
#        {% for contact in contacts %}
#        <div class="card">
#            <p> Телефон:
#                {% if contact.phone %}
#                    {{contact.phone}}
#                {% else %}
#                    -
#                {% endif %}
#            </p>
#            <p> Почта: 
#                {% if contact.email %}
#                    {{contact.email}}
#                {% else %}
#                    -   
#                {% endif %}
#            </p>
#            <p>Город: 
#                {% if contact.city %}
#                    {{contact.city}}
#                {% else %}
#                    -
#            {% endif %}
#            </p>
#        </div>
#        {% endfor %}
#    </div>
# {% endblock content %}
# 
# 
# 
# 
# 
# 
# 09.06
# GET запросы
# 
# http://127.0.0.1:8000/products?rating=4                        Пример
# 
# get удаляет только один результат
# 
# 
# 
# 11.06
# Медиафайлы и форма на страница (типа форма обратной связи)
# 
# создали 2 прриложения
# 
# appModels - appPages
# 
# из appModels удалили лишний - views, test. Типа не нужные файлы
# из appPages удалили лишний - test, models. Типа не нужные
# Но всё можно создать обратно если нужно
# 
# 
# 
# 
# 
# 16.09
# Создали папку медиа
# MEDIA_URL = 'media/' - это прописали в site - settings - static_url
# MEDIA_ROOT = BASE_DIR / 'media'         - там же
#
#
# еще работали в аппМоделс - вьюс и моделс.пу
# 
# pip install Pillow             - без этогго не работает imageFild
# 
# 
# https://docs.djangoproject.com/en/5.2/howto/static-files/
# Официальная документация
# 
# 
# ctrl + левая кнопка мыши - телепортация на нужную строчку в нужном файле
# 
# 
# 
# 
# 
# 
# 25.06
# Создали папку appBooks
# делаем таблизу авторов в - appBooks - models.py
# Сделали объединение для двух колонок но только для предпросмотра
# Работа с картинками
# # картинку лучше давать в формате png - тем как с ней работать надо установить 
# pip install pillow
# если не работает то до-установить
# python -m pip install --upgrade --force-reinstall pip
# 
# 
# 
# 
# 
# 
# 
# сегодня 21.07 делали увидомления для пользователя
# 
# import smtplib
# from email.mime.multipart import MIMEMultipart
# Последние чтоб можно было бы отправлять нескольким пользователей, медиа файлы и письмо само и заголовок - 4 типа
# from email.mime.text import MIMEText           - Работа с текстом
# 
# 
# 18.08 
# работали с админкой
# изменения в конце файла 
# Shop - settings.py
# appSettings - admin.py
# appShop - models.py
# appShop - admin.py
# 
# 
# 20.08
# Продольжили верхний файл
# 
# Так же создали папки templates, static
#
# Еще работали в appShop - views.py
# Так же в appShop создали файл - urls.py
# 
# добавляли в Shop - urls.py
# include
# а ниже
# path('', include('appShop.urls'))
# 
# 
# Дописывали настройки в
# shop - settings - TEMPLATES
# 
# 'DIRS': [
#            BASE_DIR / 'templates'
#            ],
# 
# 
# shop - settings - STATIC_URL = 'static/'
# сверху перешли по ссылке там скопировали и вставили то что тут ниже
#
# STATICFILES_DIRS = [
#    BASE_DIR / "static",
# ]
# 
# 
# 25.08
# Скачали search.html
# его разбили по файлам - home.html, scripts.js, stule.css
# В scripts - реализован поиск по нажатию клавиши - enter
# 
# работали с файлом appShop - views.py
# appShop - urls.py
# скачивали JQuery - ajax - знак $ - в scripts.js
# 
# 
# 27.08
# GitHub
# github desktop надо утановить 
# iqunix42 - там этот файл
# git bash
# 
# .gitignore - файл который хранит ограничения на то что не надо загружать в github - напримерв venv - не надо туда грузить
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 