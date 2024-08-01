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

## 30.07.2024 - Модели
* В приложении `todolist` создана модель `Task`
  * Миграции:
    * Создать `python manage.py makemigrations`
    * Применить (но не плохо было бы сначала позмотреть) `python manage.py migrate`
    * Проверить `python manage.py showmigrations`
    * Откатить `python manage.py migrate todolist 0001`
* Создана миграция модели `Task` в приложении `todolist` и 
как следствие в базе данных создана таблица `todolist_task`
* Модель `Task` изменена. Добавлены поля: `status`, `owner` 
с использованием свойства `choices`. 
Создана и применена миграция (**0002_task_owner_task_status.py**)

## 30.07.2024 - Настройка админки
* Создаем суперпользователя `python manage.py createsuperuser`
* Переход по адресу http://127.0.0.1:8000/admin/
* Регистрируем и настраиваем модель (модели) в админке 
в файле **admin.py**
  ```python
  # todolist/admin.py
  
  from django.contrib import admin
  from todolist.models import Task
  
  # admin.site.register(Task)
  # или по красоте:
  @admin.register(Task)
  class TaskAdmin(admin.ModelAdmin):
      list_display = ('name', 'status', 'owner', 'due_date')
      list_filter = ('status', 'owner', 'due_date')
      search_fields = ('name', 'description')
  ```
  `list_display` - что видим, `list_filter` - как фильтруем, 
`search_fields` - где ищем.

## 30.07.2024 - QuerySet

Тестим выборки через консоль: `python manage.py shell`

Выход из консоли: `exit()` или ctrl+d

* Выборки.
  * `Task.objects.get(id=6)`
  * `for task in Task.objects.all(): print(task.__dict__)`
  * `Task.objects.values('status').distinct()`
  * `Task.objects.all().order_by('due_date')`   # По возрастанию
  * `Task.objects.all().order_by('-due_date')`  # По убыванию
  * `Task.objects.all()[:10]`  # Первые десять задач
  * `Task.objects.all()[10:20]`  # Задачи с 11-й по 20-ю
* Фильтрация данных, модификаторы фильтрации
  * `Task.objects.filter(status='Черновик')` # выбрали
  * `Task.objects.exclude(status='Черновик')` # исключили
  * `Task.objects.filter(status__iexact='черновик')` # точное совпадение, но не чувствуем регистр
  * `Task.objects.filter(status__contains='рнови')` # подстрока, чувствуем регистр
  * `Task.objects.filter(status__icontains='РНОВИ')` # подстрока, не чувствуем регистр
  * `__startswith` - Проверка начала строки, чувствуем регистр
  * `__istartswith` - Проверка начала строки, не чувствуем регистр
  * `__endswith` - Проверка конца строки, чувствуем регистр
  * `__iendswith` - Проверка конца строки, не чувствуем регистр
  * `__gt`, `__gte`, `__lt`, `__lte` (больше, больше или равно, меньше, меньше или равно)
  * `Task.objects.filter(due_date__gt=datetime.date.today())`

* Проверка принадлежности к списку значений
  ```python
  list_owner = ['admin', 'anonim', 'faka']
  Task.objects.filter(owner__in=list_owner)
  ```
* Проверка на null (или отсутствие значения) (!!! не None !!!)
  ```python
  Task.objects.filter(due_date__isnull=True)
  ```
* Проверка диапазона значений
  ```python
  Task.objects.filter(due_date__range=[start_of_week, end_of_week])
  ```

* Комплексная фильтрация (Q-объекты)
  ```python
  complex_filter = Task.objects.filter(
      status='completed', 
      priority='high'
  ).exclude(due_date__lt=datetime.date.today())
  ```
  ```python
  from django.db.models import Q
  
  complex_filter = Task.objects.filter(
      Q(status='completed') & (Q(priority='high') | Q(priority='urgent'))
  )
  ```
## 01.08.2024 - Модели. Связь "один-ко-многим"
* В приложении `todolist` создана модель `Comment`
* Создана миграция модели `Comment`
* Связали `Task` и `Comment` "один-ко-многим"
* Настроили админку для добавления записей в `Comment` 
через `TabularInline` (отображает связанные объекты в табличном виде)

## 02.08.2024 - Модели. Связь "многие-ко-многим"
* В приложении `todolist` создана модель `Tag`
* В модель `Task` добавлено поле tags
  ```python
  tags = models.ManyToManyField(
    to='todolist.Tag', 
    verbose_name='теги', 
    related_name='tasks',
  )
  ```
* Создана миграция. Результат - две таблицы:
  * SELECT id, name FROM todolist_tag
  * SELECT id, task_id, tag_id FROM todolist_task_tags
* Добавление тегов через `python manage.py shell`:
  * `from todolist.models import Tag, Task`
  * `task = Task.objects.get(pk=1)`
  * `tag = Tag.objects.create(name='новый тег')`
  * `task.tags.add(tag)`
  * `task.save()` # обязательно !
  * `task.tags.all()`

## 02.08.2024 - REST API и Django REST Framework (DRF)
* https://www.django-rest-framework.org/
* Установка `pip install djangorestframework` или через **requirements.txt**
* Добавили `'rest_framework'` в список `INSTALLED_APPS` в файле **settings.py**
* Создали отображение (вьюсет) `TodolistViewSet` на основе модели `Task`
в файле **todolist/views.py**. 
* Создали для `TodolistViewSet` сериализатор `TaskSerializer`
для преобразования модели в JSON и обратно в файле **serializers.py**
* `TodolistViewSet` зарегестрировали в роутере с префиксом 'tasks' в файле **todolist/urls.ry**
* Роутер добавили в `urlpatterns` в файле **myproject/urls.ry**
* API доступен по адресу http://127.0.0.1:8000/tasks/

