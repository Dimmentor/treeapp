## 🔍 Оглавление

### #Pydantic:
1. [Что такое Pydantic и для чего он используется?](#1-что-такое-pydantic-и-для-чего-он-используется)
2. [Как создать базовую модель данных с использованием Pydantic?](#2-как-создать-базовую-модель-данных-с-использованием-pydantic)
3. [Как Pydantic осуществляет валидацию данных?](#3-как-pydantic-осуществляет-валидацию-данных)
4. [Чем отличается BaseModel от dataclass в Pydantic?](#4-чем-отличается-basemodel-от-dataclass-в-pydantic)
5. [Как задать типы данных для полей в Pydantic модели?](#5-как-задать-типы-данных-для-полей-в-pydantic-модели)
6. [Как использовать тип constr в Pydantic для ограничения длины строки?](#6-как-использовать-тип-constr-в-pydantic-для-ограничения-длины-строки)
7. [Как можно задать значения по умолчанию для полей модели Pydantic?](#7-как-можно-задать-значения-по-умолчанию-для-полей-модели-pydantic)
8. [Как определить кастомный валидатор для поля модели в Pydantic?](#8-как-определить-кастомный-валидатор-для-поля-модели-в-pydantic)
9. [В чем разница между @validator, @root_validator, @before, @after, @wrap, и @plain валидаторами?](#9-в-чем-разница-между-validator-root_validator-before-after-wrap-и-plain-валидаторами)
10. [Когда следует использовать @before валидатор и какие задачи он решает?](#10-когда-следует-использовать-before-валидатор-и-какие-задачи-он-решает)
11. [Как использовать @after валидатор и в каких случаях он применим?](#11-как-использовать-after-валидатор-и-в-каких-случаях-он-применим)
12. [Что такое @wrap валидатор и как он позволяет обернуть процесс валидации?](#12-что-такое-wrap-валидатор-и-как-он-позволяет-обернуть-процесс-валидации)
13. [Как работает @plain валидатор и чем он отличается от других типов валидаторов?](#13-как-работает-plain-валидатор-и-чем-он-отличается-от-других-типов-валидаторов)
14. [Как можно использовать вложенные модели в Pydantic?](#14-как-можно-использовать-вложенные-модели-в-pydantic)
15. [Как игнорировать или исключать поля из сериализации в Pydantic модели?](#15-как-игнорировать-или-исключать-поля-из-сериализации-в-pydantic-модели)
16. [Как работают алиасы полей (Field(..., alias='other_name')) в Pydantic?](#16-как-работают-алиасы-полей-field-aliasother_name-в-pydantic)
17. [Как использовать Config для настройки поведения модели в Pydantic?](#17-как-использовать-config-для-настройки-поведения-модели-в-pydantic)
18. [Как работает метод dict() в Pydantic и какие параметры он поддерживает?](#18-как-работает-метод-dict-в-pydantic-и-какие-параметры-он-поддерживает)

### #FastAPI:
19. [Что такое FastAPI и для каких задач он предназначен?](#19-что-такое-fastapi-и-для-каких-задач-он-предназначен)
20. [Как использовать Depends для внедрения зависимостей в маршруты FastAPI?](#20-как-использовать-depends-для-внедрения-зависимостей-в-маршруты-fastapi)
21. [Чем отличается синхронная и асинхронная зависимость в FastAPI?](#21-чем-отличается-синхронная-и-асинхронная-зависимость-в-fastapi)
22. [Как создать и использовать BackgroundTasks в FastAPI?](#22-как-создать-и-использовать-backgroundtasks-в-fastapi)
23. [Что такое middleware в FastAPI и как его можно добавить в приложение?](#23-что-такое-middleware-в-fastapi-и-как-его-можно-добавить-в-приложение)
24. [Как middleware в FastAPI может влиять на обработку запросов и ответов?](#24-как-middleware-в-fastapi-может-влиять-на-обработку-запросов-и-ответов)
25. [Как использовать Pydantic модели для валидации запросов и ответов в FastAPI?](#25-как-использовать-pydantic-модели-для-валидации-запросов-и-ответов-в-fastapi)
26. [Как в FastAPI работает система маршрутов и как можно задавать параметры в пути?](#26-как-в-fastapi-работает-система-маршрутов-и-как-можно-задавать-параметры-в-пути)
27. [Как управлять состоянием сессии в FastAPI (например, использование state)?](#27-как-управлять-состоянием-сессии-в-fastapi-например-использование-state)
28. [Как использовать декоратор @app.exception_handler для обработки исключений?](#28-как-использовать-декоратор-appexception_handler-для-обработки-исключений)
29. [Что такое lifespan события в FastAPI и как их использовать?](#29-что-такое-lifespan-события-в-fastapi-и-как-их-использовать)
30. [В чем разница между lifespan и событиями startup и shutdown?](#30-в-чем-разница-между-lifespan-и-событиями-startup-и-shutdown)
31. [Как обрабатывать ресурсы и их освобождение в рамках lifespan в FastAPI?](#31-как-обрабатывать-ресурсы-и-их-освобождение-в-рамках-lifespan-в-fastapi)

### 1) Что такое Pydantic и для чего он используется?

* Pydantic — это библиотека Python для парсинга и валидации данных с использованием аннотаций типов. Она позволяет:

Валидировать входные данные (например, JSON, запросы API, данные форм).

Сериализовать данные в Python-объекты (модели).

Генерировать JSON-схемы для API-документации (например, в FastAPI).

Обеспечивать типизацию данных с помощью BaseModel.

* Основные сценарии использования:

Валидация запросов/ответов в веб-фреймворках (FastAPI, Starlette).

Конфигурация приложений (например, через .env).

Работа с ORM (например, SQLAlchemy).

### 2) Как создать базовую модель данных с использованием Pydantic?
```sh
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str | None = None  # Опциональное поле
```
Использование:

```sh
user = User(id=1, name="Alice")
print(user.model_dump())  # {'id': 1, 'name': 'Alice', 'email': None}
```
### 3) Как Pydantic осуществляет валидацию данных?
Pydantic автоматически проверяет типы полей при создании экземпляра модели:

Если тип не совпадает, пытается привести его (например, "123" → 123).

Если приведение невозможно, вызывает ValidationError.

Пример:

```sh
from pydantic import ValidationError

try:
    User(id="not_an_int", name="Alice")
except ValidationError as e:
    print(e.errors())
```
### 4) Чем отличается BaseModel от dataclass в Pydantic?
* BaseModel

Встроенная валидация данных.	

Поддержка alias, json_schema.

Методы model_dump()(в старых версиях - dict()), model_validate().

* dataclass

Нет валидации (только аннотации типов).

Только стандартные dataclass-функции.

Только dataclasses.asdict().
 
Пример dataclass:

```sh
from pydantic.dataclasses import dataclass

@dataclass
class User:
    id: int
    name: str
```
### 5) Как задать типы данных для полей в Pydantic модели?
Используются аннотации типов Python (str, int, List, и т. д.):

```sh
from typing import List, Optional

class Product(BaseModel):
    id: int
    tags: List[str] = []
    price: Optional[float] = None
```
### 6) Как использовать тип constr в Pydantic для ограничения длины строки?
constr (от constrained string) задает ограничения через min_length и max_length:

```sh
from pydantic import BaseModel, constr

class Post(BaseModel):
    title: constr(min_length=1, max_length=100)
```
### 7) Как можно задать значения по умолчанию для полей модели Pydantic?
Через присваивание значения в объявлении класса:

```sh
class User(BaseModel):
    id: int
    role: str = "user"  # Значение по умолчанию
```
### 8) Как определить кастомный валидатор для поля модели в Pydantic?
Используйте декоратор @validator:

```sh
from pydantic import BaseModel, validator

class User(BaseModel):
    age: int

    @validator("age")
    def check_age(cls, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        return value
```
### 9) В чем разница между @validator, @root_validator, @before, @after, @wrap, и @plain валидаторами?
@validator — проверяет отдельное поле.

@root_validator — работает со всей моделью (все поля сразу).

@before — выполняется до стандартной валидации Pydantic.

@after — выполняется после стандартной валидации.

@wrap — оборачивает процесс валидации (например, для логирования).

@plain — простой валидатор без контекста модели.

### 10) Когда следует использовать @before валидатор и какие задачи он решает?
@before полезен для предварительной обработки данных:

```sh
@validator("name", pre=True)
def trim_name(cls, value):
    return value.strip()  # Удаляет пробелы до валидации
```
### 11) Как использовать @after валидатор и в каких случаях он применим?
@after применяется для пост-обработки:

```sh
@validator("password", pre=False)
def hash_password(cls, value):
    return hashlib.sha256(value.encode()).hexdigest()
```
### 12) Что такое @wrap валидатор и как он позволяет обернуть процесс валидации?
@wrap оборачивает весь процесс валидации:

```sh
from pydantic import validator

@validator("*", pre=True, always=True, check_fields=False)
def log_validation(cls, value, field):
    print(f"Validating {field.name}")
    return value
```
### 13) Как работает @plain валидатор и чем он отличается от других типов валидаторов?
@plain — это валидатор без доступа к другим полям модели:

```sh
@validator("email", allow_reuse=True)
def validate_email(value):
    if "@" not in value:
        raise ValueError("Invalid email")
    return value
```
### 14) Как можно использовать вложенные модели в Pydantic?
Просто вложите одну модель в другую:

```sh
class Address(BaseModel):
    city: str

    class User(BaseModel):
        address: Address
```
### 15) Как игнорировать или исключать поля из сериализации в Pydantic модели?
Через exclude в model_dump():

```sh
user.model_dump(exclude={"email"})  # Исключает поле `email`
```
Или в Config:

```sh
class User(BaseModel):
    class Config:
        exclude = {"email"}
```
### 16) Как работают алиасы полей (Field(..., alias='other_name')) в Pydantic?
Позволяют использовать другое имя для поля в JSON:

```sh
from pydantic import Field

class User(BaseModel):
    name: str = Field(..., alias="username")

user = User.parse_raw('{"username": "Alice"}')  # OK
```
### 17) Как использовать Config для настройки поведения модели в Pydantic?
Config позволяет настроить поведение модели:

```sh
class User(BaseModel):
    class Config:
        allow_population_by_field_name = True  # Разрешить заполнение по alias
        extra = "forbid"  # Запретить неизвестные поля
```
### 18) Как работает метод dict() в Pydantic и какие параметры он поддерживает?
Преобразует модель в словарь:

```sh
user = User(id=1, name="Alice")
user.model_dump()  # {'id': 1, 'name': 'Alice'}
```
Параметры:

include — только указанные поля.

exclude — исключить поля.

by_alias — использовать алиасы.

Пример:

```sh
user.model_dump(include={"name"})  # {'name': 'Alice'}
```
### 19) Что такое FastAPI и для каких задач он предназначен?
FastAPI — это современный, быстрый (высокопроизводительный) веб-фреймворк для создания API на Python, основанный на Starlette и Pydantic.

Основные задачи:

Создание RESTful API и веб-приложений.

Автоматическая генерация OpenAPI/Swagger-документации.

Поддержка асинхронных (async/await) и синхронных эндпоинтов.

Интеграция с Pydantic для валидации данных.

Работа с WebSockets, GraphQL, JWT-аутентификацией.

Преимущества:

Высокая производительность (близкая к Node.js и Go).

Автоматическая валидация данных через Pydantic.

Встроенная документация (Swagger UI и ReDoc).

### 20) Как использовать Depends для внедрения зависимостей в маршруты FastAPI?
Depends позволяет внедрять зависимости (например, сервисы, БД-сессии) в эндпоинты.

Пример:

```sh
from fastapi import FastAPI, Depends

app = FastAPI()

def get_db():
    db = "db_connection"
    try:
        yield db
    finally:
        print("Close DB connection")

@app.get("/items/")
async def read_items(db: str = Depends(get_db)):
    return {"db": db}
get_db — это dependency, которая создает и закрывает соединение с БД.
```
Depends(get_db) автоматически вызывает get_db и передает результат в read_items.

### 21) Чем отличается синхронная и асинхронная зависимость в FastAPI?
* Синхронная (def)

Подходит для CPU-интенсивных задач.
  
Блокирует поток при выполнении (если внутри есть I/O-операции).

Может замедлять работу при большом количестве запросов.

* Асинхронная (async def)
  
Не блокирует поток (использует await).

Подходит для I/O-операций (запросы к БД, API).

Эффективно работает с тысячами одновременных запросов.

Пример асинхронной зависимости:

```sh
async def get_async_data():
    data = await fetch_from_db()  # Асинхронный вызов
    return data

@app.get("/data")
async def read_data(data: str = Depends(get_async_data)):
    return {"data": data}
```
### 22) Как создать и использовать BackgroundTasks в FastAPI?
BackgroundTasks позволяет выполнять задачи после отправки ответа клиенту (например, логирование, отправка email).

Пример:

```sh
from fastapi import BackgroundTasks

def log_task(message: str):
    with open("log.txt", "a") as f:
        f.write(message + "\n")

@app.post("/send-notification")
async def send_notification(
    message: str, 
    background_tasks: BackgroundTasks
):
    background_tasks.add_task(log_task, message)
    return {"status": "Message sent"}
log_task выполнится после возврата ответа клиенту.
```
### 23) Что такое middleware в FastAPI и как его можно добавить в приложение?
Middleware — это промежуточный слой, который обрабатывает запросы и ответы до/после основного эндпоинта.

Пример middleware для логирования:

```sh
from fastapi import Request

@app.middleware("http")
async def log_requests(request: Request, call_next):
    print(f"Request: {request.method} {request.url}")
    response = await call_next(request)
    print(f"Response: {response.status_code}")
    return response
call_next передает запрос дальше по цепочке middleware и эндпоинтам.
```
### 24) Как middleware в FastAPI может влиять на обработку запросов и ответов?
Middleware может:

Модифицировать запрос/ответ (например, добавлять заголовки).

Логировать данные.

Обрабатывать ошибки (например, перехватывать 404).

Валидировать аутентификацию (JWT, API-ключи).

Пример добавления CORS:

```sh
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST"],
)
```
### 25) Как использовать Pydantic модели для валидации запросов и ответов в FastAPI?
FastAPI автоматически валидирует данные через Pydantic.

Пример:

```sh
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float

@app.post("/items/")
async def create_item(item: Item):  # Валидация запроса
    return {"item": item}  # Валидация ответа
```
Если name не передать, FastAPI вернет 422 Unprocessable Entity.

### 26) Как в FastAPI работает система маршрутов и как можно задавать параметры в пути?
Маршруты определяются через декораторы (@app.get, @app.post).

Параметры пути (path parameters):

```sh
@app.get("/items/{item_id}")
async def read_item(item_id: int):  # item_id автоматически конвертируется в int
    return {"item_id": item_id}
```
Если передать item_id=abc, FastAPI вернет 422 (ошибка валидации).

Query-параметры:

```sh
@app.get("/items/")
async def read_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}
```
Вызов: /items/?skip=5&limit=20.

### 27) Как управлять состоянием сессии в FastAPI (например, использование state)?
app.state хранит глобальные данные (например, подключение к БД).

Пример:

```sh
app.state.database = "db_connection"

@app.get("/db")
async def get_db(db: str = Depends(lambda: app.state.database)):
    return {"db": db}
```
### 28) Как использовать декоратор @app.exception_handler для обработки исключений?
Позволяет перехватывать исключения и возвращать кастомные ответы.

Пример:

```sh
from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse

@app.exception_handler(HTTPException)
async def custom_http_exception(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail},
    )
```
### 29) Что такое lifespan события в FastAPI и как их использовать?
lifespan позволяет выполнять код при старте и остановке приложения (например, открыть/закрыть соединение с БД).

Пример:

```sh
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Startup: Open DB connection")
    yield
    print("Shutdown: Close DB connection")

app = FastAPI(lifespan=lifespan)
```
### 30) В чем разница между lifespan и событиями startup и shutdown?
* lifespan	
Более гибкий (контекстный менеджер).

Подходит для асинхронных операций.

* startup/shutdown

Простой декоратор.

Работает только с синхронным кодом.


Пример startup/shutdown:

```sh
@app.on_event("startup")
async def startup():
    print("App started")

@app.on_event("shutdown")
async def shutdown():
    print("App stopped")
```
### 31) Как обрабатывать ресурсы и их освобождение в рамках lifespan в FastAPI?
Используйте try/finally или contextlib:

```sh
@asynccontextmanager
async def lifespan(app: FastAPI):
    db = await connect_to_db()
    try:
        yield {"db": db}
    finally:
        await db.close()
```
yield передает данные в приложение.

finally гарантирует освобождение ресурсов.

Итог
FastAPI — мощный фреймворк для создания API с:

Автоматической валидацией (Pydantic).

Асинхронной поддержкой (async/await).

Гибкой системой зависимостей (Depends).

Удобной документацией (Swagger/ReDoc).
