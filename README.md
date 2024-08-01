### Проект Django `myproject`

## 24.06.2024 - Init
* `git init`
* Создан файл **requirements.txt**
  * ```pip install -r requirements.txt```
* Создан файл **.gitignore**
* Создан файл **README.md**

## 24.06.2024 - Creat
* Установка Django
  * ```pip install Django```
* Создание проекта Django
  * ```django-admin startproject myproject```
* Проверяем
  * Переходим в проект `cd myproject`
  * `python manage.py runserver`

## 24.06.2024 - Connecting GitHub

```chatinput
git branch -M main
git remote add origin https://github.com/VadonGera/Django-learn.git
git push -u origin main
```

## 24.06.2024 - Создание приложений `todolist` и `about`
* `python manage.py startapp todolist`
* `python manage.py startapp about`
* Файл **urls.py** проекта настроен, маршруты для 
приложений `todolist` и `about` подключены.
  ```chatinput
  urlpatterns = [
        path('admin/', admin.site.urls),
        path('todolist/', include('todolist.urls')),
        path('about/', include('about.urls')),
    ]
   ```
* В приложениях `todolist` и `about` созданы файлы **urls.py** и 
настроены маршруты для главной страницы и страницы About, 
которые связаны с функциями base и about соответственно.
  ```chatinput
  # ./todolist/urls.py
  from .views import base
  
  urlpatterns = [path('', base, name='base')]
  ```
  ```chatinput
  # ./about/urls.py
  from .views import about
  
  urlpatterns = [path('', about, name='about')]
  ```
* В файлах **views.py** приложений `todolist` и `about` созданы 
функции `base` и `about`, которые обрабатывает запрос и 
возвращают шаблоны **base.html** и **about.html** соответственно.
* Созданы директории **./todolist/templates/todolist** и 
**./about/templates/about**, в которых созданы файлы шаблонов 
**base.html** и **about.html**.
  * Переход по адресу http://127.0.0.1:8000/todolist/ отображает 
  шаблон **base.html**.
  * Переход по адресу http://127.0.0.1:8000/about/ отображает 
  шаблон **about.html**.

## 30.07.2024 - Подключение проекта к PostgreSQL
* Установка `pip install psycopg[binary]` или через **requirements.txt**
* Настройка Django для использования PostgreSQL
  ```python
  # settings.py
  
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.postgresql',
          'NAME': 'todolist',       # Имя базы данных
          'USER': 'postgres',       # Имя пользователя
          'PASSWORD': 'secret',     # !!! Пароль пользователя
          'HOST': 'localhost',      # Хост, по умолчанию 'localhost', опционально
          'PORT': '5432',           # Порт, по умолчанию '5432', опционально
      }
  }
  ```
* Миграции базы данных (те, что натворил создатель 
Django, наших еще нет)
  * ```python manage.py migrate``` 

