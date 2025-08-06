# Справочник по Django и DRF

## 🔍 Оглавление  
1. [Отличие F от Func](#1-отличие-f-от-func)  
2. [Что такое OuterRef](#2-что-такое-outerref)  
3. [Как получить только нужные колонки из таблицы](#3-как-получить-только-нужные-колонки-из-таблицы)  
4. [Поведение get() при отсутствии записи](#4-поведение-get-при-отсутствии-записи)  
5. [Поведение get() при нескольких записях](#5-поведение-get-при-нескольких-записях)  
6. [Разница между blank и null](#6-разница-между-blank-и-null)  
7. [Как обновить только указанные поля при вызове метода save](#7-как-обновить-только-указанные-поля-при-вызове-метода-save)  
8. [Использование objects.none](#8-использование-objectsnone)  
9. [Действия после создания объекта](#9-действия-после-создания-объекта)  
10. [Класс Meta](#10-класс-meta)  
11. [Применение GenericForeignKey](#11-применение-genericforeignkey)  
12. [Размещение бизнес-логики](#12-размещение-бизнес-логики)  
13. [ModelViewSet и GenericViewSet](#13-modelviewset-и-genericviewset)  
14. [Собственный менеджер моделей](#14-собственный-менеджер-моделей)  
15. [Запросы методов QuerySet](#15-запросы-методов-queryset)  
16. [Система аутентификации](#16-система-аутентификации)  
17. [Проверка прав по группе](#17-проверка-прав-по-группе)  
18. [Разные доступы в ViewSet](#18-разные-доступы-в-viewset)  
19. [Обход в глубину и ширину](#19-обход-в-глубину-и-ширину)  
20. [Dependency Injection](#20-dependency-injection)  
21. [Unit of Work](#21-unit-of-work)  
22. [Сборщик мусора в Python](#22-сборщик-мусора-в-python)  


### 1) Отличие F от Func
В Django объект F и функция Func используются для работы с выражениями в ORM, но для разных целей. F представляет собой поле модели или его значение, позволяя ссылаться на данные непосредственно в запросе к базе данных. Func же используется для создания вычислений или агрегаций в запросах, часто применяясь для сложных операций с данными в базе. 

#### F-объекты (F expressions):
* Представляют собой ссылки на поля модели, позволяя выполнять операции над ними в рамках запроса к базе данных. 
* Позволяют избежать необходимости извлекать значения полей в Python для выполнения операций, что повышает эффективность запросов. 
* Используются для сравнения значений полей, обновления полей, аннотирования результатов и других операций, связанных с данными в базе. 

#### Функции (Func):
* Предоставляют возможность использовать агрегатные функции базы данных (например, SUM, AVG, COUNT, MAX, MIN) и другие функции в запросах.
* Используются для создания более сложных выражений и вычислений на уровне базы данных.
* Позволяют выполнять операции, которые не могут быть выражены простым сравнением или арифметическим выражением.

В итоге, F-объекты используются для работы с полями модели, в то время как Func предоставляет возможность использовать функции базы данных для вычислений и агрегации в запросах. 

### 2) Что такое OuterRef
OuterRef - это класс, который используется внутри подзапросов (subqueries) для ссылки на значения из внешнего запроса. Это позволяет выполнять фильтрацию или другие операции в подзапросе, основываясь на данных из основного запроса. 

OuterRef играет ключевую роль в работе с подзапросами, особенно когда необходимо соотнести данные из внешнего запроса с данными внутри подзапроса. 

Предположим, у вас есть модели Author и Book, и вы хотите получить всех авторов, у которых есть хотя бы одна книга с определенным названием. В этом случае вы можете использовать OuterRef для ссылки на primary key (pk) автора внутри подзапроса: 

```sh
from django.db.models import OuterRef, Subquery, Count

books_with_title = Book.objects.filter(
    author=OuterRef('pk'),  # Ссылка на pk автора из внешнего запроса
    title="My Awesome Book"
)

authors_with_book = Author.objects.annotate(
    num_books=Subquery(books_with_title.values('pk').annotate(count=Count('*')).values('count'))
).filter(num_books__gt=0)
```

### 3) Как получить только нужные колонки из таблицы

1. values() - позволяет получить список словарей, где ключами являются имена полей, а значениями - соответствующие значения для каждого объекта. Это может быть полезно, когда вам не нужен полноценный объект модели, а только набор значений для определенных полей. 

```sh
Book.objects.values('title', 'author__name')
[{'title': 'Book1', 'author__name': 'Author1'}, ...]
```
2. values_list() - возвращает кортежи. Если вам нужно получить только одно поле, используйте метод values_list() с аргументом flat=True, чтобы получить список значений, а не список кортежей из одного элемента. 
```sh
Book.objects.values_list('title', flat=True)  # ['Book1', 'Book2']
Book.objects.values_list('id', 'title')  # [(1, 'Book1'), (2, 'Book2')]
```

3. only() - Этот метод позволяет указать, какие поля нужно загружать из базы данных, что может значительно повысить производительность, особенно при работе с большими таблицами и сложными запросами. 
```
books = Book.objects.only('title')
for book in books:
    print(book.title)  # Загружено сразу
    print(book.author)  # Догрузится отдельным запросом
```
    
4. defer() - противоположность only():

```sh
books = Book.objects.defer('description')  # Не загружать описание
```

Оптимизация:

* only/defer уменьшают размер SELECT запроса

* values/values_list полностью исключают создание объектов модели


### 4) Поведение get() при отсутствии записи
Вызывает исключение DoesNotExist:
```sh
try:
    book = Book.objects.get(id=999)
except Book.DoesNotExist:
    print("Книга не найдена")
```
#### Особенности:

* Исключение является атрибутом модели (Book.DoesNotExist)

* Рекомендуется всегда обрабатывать это исключение

* Альтернатива - get_object_or_404() для веб-запросов

### 5) Поведение get() при нескольких записях
Вызывает исключение MultipleObjectsReturned:
```sh
try:
    book = Book.objects.get(title='Common Title')
except Book.MultipleObjectsReturned:
    print("Найдено несколько книг с таким названием")
```
#### Как избежать:

* Убедиться, что поле уникально

* Использовать filter() вместо get() для неоднозначных запросов

### 6) Разница между blank и null

В Django, null=True указывает, что поле может содержать значение NULL в базе данных, в то время как blank=True указывает, что поле может быть пустым при валидации формы (например, в формах Django или в админке). Важно понимать, что эти два параметра отвечают за разные аспекты обработки данных: null относится к базе данных, а blank - к валидации формы. 

#### Рекомендации:

* Для строковых полей обычно blank=True, null=False (хранить пустую строку вместо NULL)

* Для числовых полей null=True если нужно различать 0 и отсутствие значения

### 7) Как обновить только указанные поля при вызове метода save

1. Использование update_fields:

```sh
book = Book.objects.get(id=1)
book.title = "New Title"
book.save(update_fields=['title'])  # Только UPDATE title
```
2. Метод refresh_from_db:

```sh
book.refresh_from_db(fields=['author'])  # Загрузить только author
```

#### Когда полезно:

* Для оптимизации при частичных обновлениях

* Чтобы избежать перезаписи изменений других полей

### 8) Использование objects.none

1. Возврат пустого QuerySet в методах:

```sh
def get_books(user):
    if not user.has_perm('app.view_book'):
        return Book.objects.none()
    return Book.objects.all()
 ```
   
2. Начальное значение для агрегации:

```sh
books = Book.objects.none()
for category in categories:
    books |= category.books.all()
```

#### Преимущества:

* Не выполняет SQL-запросов

* Совместим с цепочками методов (filter, annotate и т.д.)

### 9) Как совершить какое-либо действие после создания объекта модели
1. Сигнал post_save:

```sh
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Book)
def book_created(sender, instance, created, **kwargs):
    if created:
        print(f"Создана новая книга: {instance.title}")
```
2. Переопределение save:

```sh
class Book(models.Model):
    def save(self, *args, **kwargs):
        created = not self.pk
        super().save(*args, **kwargs)
        if created:
            print(f"Создана новая книга: {self.title}")
```
#### Рекомендации:

* Для простых действий - переопределение save()

* Для сложной логики или внешних интеграций - сигналы

### 10) Что такое class Meta и для чего он нужен
Класс Meta определяет метаданные модели:

```sh
class Book(models.Model):
    title = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
        ordering = ['-published_date']
        unique_together = ['title', 'author']
        indexes = [
            models.Index(fields=['title']),
            models.Index(fields=['author', 'published_date']),
        ]
```
#### Частые атрибуты:

* db_table - имя таблицы в БД

* ordering - сортировка по умолчанию

* abstract - абстрактная модель

* constraints - ограничения уровня БД

### 11) Когда пригодится GenericForeignKey
GenericForeignKey позволяет создать связь с любой другой моделью:

```sh
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Comment(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    text = models.TextField()
```

Применение:

Комментарии к разным типам объектов

Логирование действий

Универсальные рейтинги/лайки

Альтернативы:

Полиморфные модели (django-polymorphic)

Отдельные связи для каждого типа

### 12) Где нужно и не нужно писать бизнес логику
#### Правильные места:

* Модели - основная бизнес-логика

* Сервисные слои - сложные операции

* Forms/Serializers - валидация данных

#### Неправильные места:

* Views - только обработка HTTP

* Шаблоны - только представление

* URLs - только маршрутизация

Пример правильной структуры:

```sh
# models.py
class Order(models.Model):
    def cancel(self):
        self.status = 'cancelled'
        self.save()
        self._send_notification()
    
    def _send_notification(self):
        # Логика отправки уведомления
```
```sh
# services.py
class OrderService:
    @staticmethod
    def process_order(order):
        # Сложная логика обработки
```
### 13) Что такое ModelViewSet и GenericViewSet
ModelViewSet:

Полный набор CRUD операций

Автоматическая маршрутизация

Для стандартных операций с моделью

```sh
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
```

GenericViewSet:

Базовый класс для кастомных действий

Требует явного определения @action

Для нестандартной логики

```sh
class ReportViewSet(viewsets.GenericViewSet):
    @action(detail=False, methods=['get'])
    def sales(self, request):
        # Кастомная логика отчетов
```
### 14) Как реализовать свой менеджер моделей
1. Создание менеджера:

```sh
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')

class Book(models.Model):
    objects = models.Manager()  # Дефолтный менеджер
    published = PublishedManager()  # Кастомный
```
2. Добавление методов:

```sh
class BookManager(models.Manager):
    def bestsellers(self):
        return self.filter(sales__gt=1000)
        
class Book(models.Model):
    objects = BookManager()
```
Использование:

```sh
Book.published.all()  # Только опубликованные
Book.objects.bestsellers()  # Бестселлеры
```

### 15) Какие запросы у методов QuerySet
Метод	SQL-запрос	Особенности
all()	SELECT * FROM table	Ленивый, не выполняется сразу
filter()	SELECT ... WHERE	Цепочка условий AND
get()	SELECT ... LIMIT 1	Немедленное выполнение
create()	INSERT	Создает и сохраняет объект
update()	UPDATE	Массовое обновление
delete()	DELETE	Массовое удаление
count()	SELECT COUNT(*)	Агрегация без загрузки объектов


### 16) Встроенная система аутентификации (django.contrib.auth)
Компоненты:

Модели:

User - стандартная модель пользователя

Group - группы пользователей

Permission - права доступа

Аутентификация:

Сессии и куки

Backend-система (можно добавлять свои)

Авторизация:

Декораторы (@login_required)

Permissions для views

Настройка:

python
AUTH_USER_MODEL = 'myapp.CustomUser'  # Кастомная модель пользователя
### 17) Проверка прав по группе
1. Permission класс:

python
from rest_framework.permissions import BasePermission

class IsEditor(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='editors').exists()
2. Использование в View:

python
class BookViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsEditor]
3. Проверка в шаблоне:

html
{% if user.groups.filter.name == 'editors' %}
   <button>Редактировать</button>
{% endif %}
### 18) Разные доступы в ViewSet
Через get_permissions:

python
class BookViewSet(viewsets.ModelViewSet):
    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            return [IsAdminUser()]
        return [IsAuthenticated()]
Через @action:

python
@action(detail=True, methods=['post'], permission_classes=[IsEditor])
def publish(self, request, pk=None):
    ...

    
### 19) Обход в глубину и ширину
DFS (Depth-First Search):

Рекурсивный обход "вглубь"

Использует стек (явный или неявный)

Применение: поиск пути, топологическая сортировка

python
def dfs(node, visited):
    visited.add(node)
    for neighbor in node.neighbors:
        if neighbor not in visited:
            dfs(neighbor, visited)
BFS (Breadth-First Search):

Обход "по уровням"

Использует очередь

Применение: кратчайший путь в невзвешенном графе

python
from collections import deque

def bfs(start):
    queue = deque([start])
    visited = set([start])
    while queue:
        node = queue.popleft()
        for neighbor in node.neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                
### 20) Что такое DI
Dependency Injection (DI) - паттерн, при котором зависимости передаются объекту извне, а не создаются внутри.

Преимущества:

Упрощает тестирование

Уменьшает связность

Делает код более гибким

Пример без DI:

python
class ReportGenerator:
    def __init__(self):
        self.db = PostgreSQLConnection()  # Жесткая зависимость
        
    def generate(self):
        data = self.db.query(...)
Пример с DI:

python
class ReportGenerator:
    def __init__(self, db_connection):  # Зависимость инжектируется
        self.db = db_connection
        
    def generate(self):
        data = self.db.query(...)

# Использование
generator = ReportGenerator(MySQLConnection())


### 21) Unit of Work
Unit of Work - паттерн, который отслеживает изменения объектов и выполняет все обновления БД одной транзакцией.

Как реализован в Django:

При вызове save() объект добавляется в "грязный" список

Перед завершением транзакции все изменения применяются

Либо все изменения сохраняются, либо ни одного (атомарность)

Пример:

python
from django.db import transaction

with transaction.atomic():  # Unit of Work
    order = Order.objects.create(...)
    order.add_item(...)
    order.calculate_total()
    # Все операции выполнятся или откатятся вместе

    
### 22) Сборщик мусора в Python
Механизмы:

Счетчик ссылок:

Каждый объект имеет счетчик ссылок

При достижении 0 - память освобождается

Не может обрабатывать циклические ссылки

Generational GC:

Три поколения объектов (0, 1, 2)

Новые объекты в поколении 0

Выжившие объекты переходят в старшие поколения

Чаще проверяет младшие поколения

Как работает:

Обнаружение достижимых объектов (mark)

Удаление недостижимых (sweep)

Дефрагментация памяти (если необходимо)

Управление:

python
import gc
gc.disable()  # Отключить GC
gc.collect()  # Принудительный сбор
