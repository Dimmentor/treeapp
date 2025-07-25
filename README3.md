# Справочник по Django и DRF

## 🔍 Оглавление  
1. [Отличие F от Func](#1-отличие-f-от-func)  
2. [Что такое OuterRef](#2-что-такое-outerref)  
3. [Как получить только нужные колонки](#3-как-получить-только-нужные-колонки)  
4. [Поведение get() при отсутствии записи](#4-поведение-get-при-отсутствии-записи)  
5. [Поведение get() при нескольких записях](#5-поведение-get-при-нескольких-записях)  
6. [Разница между blank и null](#6-разница-между-blank-и-null)  
7. [Обновление указанных полей](#7-обновление-указанных-полей)  
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
F-выражения:

Используются для ссылки на значение поля модели в запросе

Позволяют выполнять атомарные обновления

Работают на уровне базы данных

python
from django.db.models import F

Product.objects.update(price=F('price') * 1.1)  # Увеличить все цены на 10%
Func-выражения:

Позволяют использовать SQL-функции в запросах

Более сложные вычисления (например, строковые операции)

Могут комбинироваться с другими выражениями

python
from django.db.models.functions import Concat, Upper

Author.objects.annotate(
    full_name=Concat('first_name', models.Value(' '), 'last_name'),
    upper_name=Upper('first_name')
)
Ключевые отличия:

F - только ссылки на поля

Func - вызов SQL-функций (CONCAT, UPPER, COALESCE и т.д.)

2) Что такое OuterRef
OuterRef используется для создания коррелированных подзапросов, когда внутренний запрос ссылается на поле внешнего запроса.

Пример:

python
from django.db.models import OuterRef, Subquery

# Найти последний комментарий для каждого поста
latest_comments = Comment.objects.filter(
    post=OuterRef('pk')
).order_by('-created_at')

posts = Post.objects.annotate(
    last_comment=Subquery(latest_comments.values('text')[:1])
)
Когда использовать:

Когда нужно аннотировать QuerySet данными из связанной модели

Для сложных условий в подзапросах

В комбинации с Subquery

Особенности:

Может использоваться только внутри Subquery

Автоматически разрешает связи между моделями

3) Как получить только нужные колонки из таблицы
1. values() - возвращает словари:

python
Book.objects.values('title', 'author__name')
# [{'title': 'Book1', 'author__name': 'Author1'}, ...]
### 2. values_list() - возвращает кортежи:

python
Book.objects.values_list('title', flat=True)  # ['Book1', 'Book2']
Book.objects.values_list('id', 'title')  # [(1, 'Book1'), (2, 'Book2')]
### 3. only() - загружает только указанные поля, но остальные доступны (ленивая загрузка):

python
books = Book.objects.only('title')
for book in books:
    print(book.title)  # Загружено сразу
    print(book.author)  # Догрузится отдельным запросом
### 4. defer() - противоположность only():

python
books = Book.objects.defer('description')  # Не загружать описание
Оптимизация:

only/defer уменьшают размер SELECT запроса

values/values_list полностью исключают создание объектов модели

### 4) Что будет, если вызвать get и записей не будет найдено
Вызывает исключение DoesNotExist:

python
try:
    book = Book.objects.get(id=999)
except Book.DoesNotExist:
    print("Книга не найдена")
Особенности:

Исключение является атрибутом модели (Book.DoesNotExist)

Рекомендуется всегда обрабатывать это исключение

Альтернатива - get_object_or_404() для веб-запросов

### 5) Что будет, если вызвать get и записей будет найдено несколько
Вызывает исключение MultipleObjectsReturned:

python
try:
    book = Book.objects.get(title='Common Title')
except Book.MultipleObjectsReturned:
    print("Найдено несколько книг с таким названием")
Как избежать:

Убедиться, что поле уникально

Использовать filter() вместо get() для неоднозначных запросов

### 6) В чем разница между blank и null
Параметр	Формы	База данных	Пример
blank=True	Поле может быть пустым в форме	Не влияет	name = models.CharField(blank=True)
null=True	Не влияет	NULL в базе	count = models.IntegerField(null=True)
Рекомендации:

Для строковых полей обычно blank=True, null=False (хранить пустую строку вместо NULL)

Для числовых полей null=True если нужно различать 0 и отсутствие значения

### 7) Как обновить только указанные поля при вызове метода save
1. Использование update_fields:

python
book = Book.objects.get(id=1)
book.title = "New Title"
book.save(update_fields=['title'])  # Только UPDATE title
2. Метод refresh_from_db:

python
book.refresh_from_db(fields=['author'])  # Загрузить только author
Когда полезно:

Для оптимизации при частичных обновлениях

Чтобы избежать перезаписи изменений других полей

### 8) Когда может пригодиться objects.none
1. Возврат пустого QuerySet в методах:

python
def get_books(user):
    if not user.has_perm('app.view_book'):
        return Book.objects.none()
    return Book.objects.all()
2. Начальное значение для агрегации:

python
books = Book.objects.none()
for category in categories:
    books |= category.books.all()
Преимущества:

Не выполняет SQL-запросов

Совместим с цепочками методов (filter, annotate и т.д.)

### 9) Как совершить какое-либо действие после создания объекта модели
1. Сигнал post_save:

python
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Book)
def book_created(sender, instance, created, **kwargs):
    if created:
        print(f"Создана новая книга: {instance.title}")
2. Переопределение save:

python
class Book(models.Model):
    def save(self, *args, **kwargs):
        created = not self.pk
        super().save(*args, **kwargs)
        if created:
            print(f"Создана новая книга: {self.title}")
Рекомендации:

Для простых действий - переопределение save()

Для сложной логики или внешних интеграций - сигналы

### 10) Что такое class Meta и для чего он нужен
Класс Meta определяет метаданные модели:

python
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
Частые атрибуты:

db_table - имя таблицы в БД

ordering - сортировка по умолчанию

abstract - абстрактная модель

constraints - ограничения уровня БД

### 11) Когда пригодится GenericForeignKey
GenericForeignKey позволяет создать связь с любой другой моделью:

python
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Comment(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    text = models.TextField()
Применение:

Комментарии к разным типам объектов

Логирование действий

Универсальные рейтинги/лайки

Альтернативы:

Полиморфные модели (django-polymorphic)

Отдельные связи для каждого типа

### 12) Где нужно и не нужно писать бизнес логику
Правильные места:

Модели - основная бизнес-логика

Сервисные слои - сложные операции

Forms/Serializers - валидация данных

Неправильные места:

Views - только обработка HTTP

Шаблоны - только представление

URLs - только маршрутизация

Пример правильной структуры:

python
# models.py
class Order(models.Model):
    def cancel(self):
        self.status = 'cancelled'
        self.save()
        self._send_notification()
    
    def _send_notification(self):
        # Логика отправки уведомления

# services.py
class OrderService:
    @staticmethod
    def process_order(order):
        # Сложная логика обработки
### 13) Что такое ModelViewSet и GenericViewSet
ModelViewSet:

Полный набор CRUD операций

Автоматическая маршрутизация

Для стандартных операций с моделью

python
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
GenericViewSet:

Базовый класс для кастомных действий

Требует явного определения @action

Для нестандартной логики

python
class ReportViewSet(viewsets.GenericViewSet):
    @action(detail=False, methods=['get'])
    def sales(self, request):
        # Кастомная логика отчетов
### 14) Как реализовать свой менеджер моделей
1. Создание менеджера:

python
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')

class Book(models.Model):
    objects = models.Manager()  # Дефолтный менеджер
    published = PublishedManager()  # Кастомный
2. Добавление методов:

python
class BookManager(models.Manager):
    def bestsellers(self):
        return self.filter(sales__gt=1000)
        
class Book(models.Model):
    objects = BookManager()
Использование:

python
Book.published.all()  # Только опубликованные
Book.objects.bestsellers()  # Бестселлеры


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
