# Django & DRF Справочник

## 🔍 Оглавление
1. [Общие сведения о Django](#1-общие-сведения-о-django)
2. [MVC на примере Django](#2-mvc-на-примере-django)
3. [Обработка запроса в Django](#3-обработка-запроса-в-django)
4. [Что такое middleware](#4-что-такое-middleware)
5. [Стандартные middleware](#5-стандартные-middleware)
6. [Что такое сигналы](#6-что-такое-сигналы)
7. [Примеры сигналов](#7-примеры-сигналов)
8. [Кастомные команды manage.py](#8-кастомные-команды-managepy)
9. [Расширение модели User](#9-расширение-модели-user)
10. [Permission и Group](#10-permission-и-group)
11. [Смена SECRET_KEY](#11-смена-secret_key)
12. [select_related vs prefetch_related](#12-select_related-vs-prefetch_related)
13. [Когда prefetch_related лучше](#13-когда-prefetch_related-лучше)
14. [OuterRef](#14-outerref)
15. [only vs values vs values_list](#15-only-vs-values-vs-values_list)
16. [Q-объекты](#16-q-объекты)
17. [F-выражения](#17-f-выражения)
18. [Массовое создание объектов](#18-массовое-создание-объектов)
19. [count() vs len()](#19-count-vs-len)
20. [objects.none](#20-objectsnone)
21. [Ленивые и немедленные запросы](#21-ленивые-и-немедленные-запросы)
22. [annotate vs aggregate](#22-annotate-vs-aggregate)
23. [Абстрактные модели](#23-абстрактные-модели)
24. [Атрибуты class Meta](#24-атрибуты-class-meta)
25. [select_for_update](#25-select_for_update)
26. [Блокировка записей](#26-блокировка-записей)
27. [GenericForeignKey](#27-genericforeignkey)
28. [Проверка прав по группам](#28-проверка-прав-по-группам)
29. [Разные права для методов ViewSet](#29-разные-права-для-методов-viewset)
30. [Декоратор action](#30-декоратор-action)
31. [Throttling](#31-throttling)
32. [Плюсы и минусы DRF](#32-плюсы-и-минусы-drf)

---

### 1) Общие сведения о Django
**Ответ**: Django — это высокоуровневый Python-фреймворк...


### 2) MVC на примере Django
**Ответ**: Django использует паттерн MTV (Model-Template-View), который похож на MVC:

Model (Модель) – отвечает за данные и бизнес-логику (аналог Model в MVC).

Template (Шаблон) – отвечает за представление (аналог View в MVC).

View (Представление) – обрабатывает запросы и возвращает ответ (аналог Controller в MVC).

Пример:

Модель Post хранит данные о посте в блоге.

Шаблон post_detail.html отображает пост.

Представление PostDetailView получает пост из БД и передаёт его в шаблон.

### 3) Обработка запроса в Django (Request-Response Cycle)
**Ответ**: Запрос приходит в Django (через WSGI-сервер, например, Gunicorn).

URL-диспетчер (urls.py) определяет, какое view должно обработать запрос.

Middleware обрабатывает запрос (например, проверяет аутентификацию).

View выполняет логику (например, запрашивает данные через ORM).

Шаблон рендерится с данными (если используется).

Middleware обрабатывает ответ (например, добавляет заголовки).

Ответ возвращается клиенту.

### 4) Что такое middleware?
**Ответ**: Middleware — это прослойка между запросом и view (или ответом и клиентом), которая может изменять запрос/ответ. Например:

AuthenticationMiddleware – проверяет аутентификацию пользователя.

CsrfMiddleware – защищает от CSRF-атак.

### 5) Стандартные middleware?
**Ответ**: django.middleware.security.SecurityMiddleware – HTTPS, HSTS и другие заголовки безопасности.

django.contrib.sessions.middleware.SessionMiddleware – работа с сессиями.

django.middleware.csrf.CsrfViewMiddleware – CSRF-защита.

django.contrib.auth.middleware.AuthenticationMiddleware – аутентификация.

django.middleware.common.CommonMiddleware – базовые обработки URL.

SecurityMiddleware
Это стандартный middleware Django, который добавляет HTTP-заголовки для безопасности:
HSTS (HTTP Strict Transport Security) – принудительно переводит сайт на HTTPS.

X-Content-Type-Options: nosniff – запрещает браузеру "угадывать" MIME-тип.

X-XSS-Protection – защита от XSS-атак.

X-Frame-Options: DENY – запрещает встраивание сайта в <iframe>.

### 6) Что такое сигналы?
**Ответ**: Сигналы — это механизм для выполнения кода при определённых событиях (например, сохранение модели или запрос к БД).

### 7) Примеры сигналов?
**Ответ**: pre_save, post_save – до/после сохранения модели.

pre_delete, post_delete – до/после удаления.

request_started, request_finished – начало/конец запроса.

m2m_changed – изменение ManyToMany-поля.

Пример:

python
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def user_created(sender, instance, created, **kwargs):
    if created:
        print("Новый пользователь создан!")
        
### 8) Кастомные команды manage.py?
**Ответ**: Создать файл management/commands/mycommand.py в приложении.

Унаследоваться от BaseCommand:

python
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Описание команды"

    def handle(self, *args, **options):
        self.stdout.write("Hello, Django!")
Вызвать: python manage.py mycommand.

### 9) Расширение модели User?
**Ответ**: OneToOne-связь:

python
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
Proxy-модель (если нужно только добавить методы).

Абстрактный User (если нужна полная замена):

python
AUTH_USER_MODEL = "myapp.CustomUser"  # в settings.py

### 10) Permission и Group в Django?
**Ответ**:
Permission – права доступа (например, can_publish_post).

Group – группа пользователей с общими правами (например, "Редакторы").

Пример:

python
from django.contrib.auth.models import Group, Permission

editors = Group.objects.create(name="Редакторы")
permission = Permission.objects.get(codename="publish_post")
editors.permissions.add(permission)

### 11) Смена SECRET_KEY?
**Ответ**:
Сессии пользователей станут недействительными.

CSRF-токены перестанут работать.

Пароли, зашифрованные с его использованием (если использовался для хеширования), могут стать нечитаемыми.

### 12) select_related vs prefetch_related?
**Ответ**:
select_related – JOIN в SQL для ForeignKey и OneToOne.

prefetch_related – отдельный запрос для ManyToMany и reverse ForeignKey.

Пример:

python
# 1 запрос с JOIN
Author.objects.select_related('profile').get(id=1)

# 2 запроса: авторы + их книги
Author.objects.prefetch_related('books').all()

### 13) Когда prefetch_related лучше чем select_related для связи один ко многим?
**Ответ**:
Если у родителя много детей (например, у Автора 1000 Книг), prefetch_related может быть эффективнее, чтобы избежать огромного JOIN.

### 14) Что такое OuterRef?
**Ответ**:
OuterRef используется в подзапросах (например, в annotate).

Пример:

python
from django.db.models import OuterRef, Subquery

newest = Comment.objects.filter(post=OuterRef('pk')).order_by('-created_at')
Post.objects.annotate(newest_comment_text=Subquery(newest.values('text')[:1]))

### 15) Какая разница между only, values и values_list?
**Ответ**:
only('field') – загружает только указанные поля, но остальные доступны (ленивая загрузка).

values('field') – возвращает QuerySet словарей.

values_list('field', flat=True) – возвращает QuerySet кортежей (или значений, если flat=True).

### 16) Что такое Q-объекты?
**Ответ**:
Позволяют строить сложные запросы с OR, AND и NOT.

Пример:

python
from django.db.models import Q

Post.objects.filter(Q(title__startswith="Django") | Q(title__startswith="Python"))

### 17) Что такое F-выражения?
**Ответ**:
Позволяют ссылаться на значение поля в запросе.

Пример (увеличить счётчик):

python
from django.db.models import F

Product.objects.update(price=F('price') * 1.1)

### 18) Как создать 100 тысяч объектов в базе?
**Ответ**:
Через bulk_create:

python
objs = [MyModel(name=f"Object {i}") for i in range(100000)]
MyModel.objects.bulk_create(objs, batch_size=1000)  # Пакетами по 1000

Плюсы:

Уменьшает нагрузку на БД.

Работает в 10-100 раз быстрее, чем цикл с save().

Ограничения:

Не вызывает save() и сигналы (post_save и т.д.).

Не работает с auto_now_add (если не указать batch_size).

### 19) Почему надо использовать objects.count() вместо len(objects)?
**Ответ**:
count() делает SELECT COUNT(*) – быстро.

len() загружает все объекты в память – медленно.

### 20) Что делает objects.none?
**Ответ**:
Возвращает пустой QuerySet (полезно для начального значения в методах).

### 21) В каких случаях Django выполняет запросы немедленно, в каких лениво?
**Ответ**:
Лениво:

filter(), all(), exclude() – не выполняют запрос, пока не нужно реальное значение.

Немедленно:

len(), list(), итерация, bool(), count(), exists().

Ленивые (запрос выполняется только при обращении)
python
queryset = Book.objects.all()  # Запрос не выполнен
books = list(queryset)         # Запрос выполнен (SELECT * FROM books)
Немедленные (запрос выполняется сразу)
python
count = Book.objects.count()    # SELECT COUNT(*) FROM books
exists = Book.objects.exists()  # SELECT 1 FROM books LIMIT 1

### 22) В чём разница между annotate и aggregate?
**Ответ**:
annotate() – добавляет вычисляемое поле к каждому объекту.

aggregate() – возвращает общий результат (например, Avg, Sum).

Пример:

python
# Средний рейтинг каждого автора
Author.objects.annotate(avg_rating=Avg('books__rating'))

# Общий средний рейтинг всех книг
Book.objects.aggregate(Avg('rating'))

### 23) Что такое абстрактные модели?
**Ответ**:
Это модели, которые не создают таблицу в БД, но от них можно наследоваться.

Пример:

python
class TimestampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Post(TimestampModel):
    title = models.CharField(max_length=100)
    
### 24) Какие атрибуты у class Meta для моделей знаешь?
**Ответ**:
verbose_name – человекочитаемое имя.

ordering – сортировка по умолчанию (['-created_at']).

indexes – индексы ([models.Index(fields=['title'])]).

unique_together – уникальные комбинации полей.

### 25) Зачем нужен select_for_update?
**Ответ**:
Блокирует строки в БД для конкурентного доступа (используется в транзакциях).

Пример:

python
from django.db import transaction

with transaction.atomic():
    product = Product.objects.select_for_update().get(id=1)
    product.stock -= 1
    product.save()
    
### 26) Что будет если обратимся к записям, заблокированным через select_for_update?
**Ответ**:
Запрос будет ждать, пока блокировка не снимется (если nowait=False) или получит ошибку (если nowait=True).

### 27) Когда пригодится GenericForeignKey?
**Ответ**:
Когда нужно связать модель с разными типами моделей (например, комментарии к Постам и Видео).

### 28) Как реализовать проверку прав по наличию определённой группы у пользователя?
**Ответ**:
Через permission_classes в DRF:

python
from rest_framework.permissions import BasePermission

class IsEditor(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name="Редакторы").exists()

class MyView(APIView):
    permission_classes = [IsEditor]
    
### 29) Как дать разные доступ в рамках одного viewset для разных методов?
**Ответ**:
Через get_permissions:

python
class MyViewSet(ViewSet):
    def get_permissions(self):
        if self.action == 'create':
            return [IsAdminUser()]
        return [IsAuthenticated()]
        
### 30) Зачем нужен декоратор action?
**Ответ**:
Добавляет кастомные методы во ViewSet (например, @action(detail=True, methods=['post'])).

### 31) Что такое throttling и как его настроить?
**Ответ**:
Throttling – ограничение количества запросов.

Настройка:

python
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_RATES': {
        'user': '100/hour',
    }
}

### 32) Плюсы и минусы DRF
**Ответ**:
**Плюсы**:
- Быстрое создание API
- Гибкость (сериализаторы, permissions, throttling)
- Поддержка REST

**Минусы**:
- Иногда избыточность
- Медленнее, чем чистое ASGI
