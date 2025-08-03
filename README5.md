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

#### Используется для определения структуры данных и валидации. Она позволяет объявлять модели данных с помощью аннотаций типов Python, что обеспечивает автоматическую проверку входящих данных на соответствие этим моделям и их преобразование в нужный формат.

* Определение моделей данных:
Pydantic позволяет создавать классы-модели, которые описывают структуру данных, используемых в API. Например, можно определить модель для данных пользователя с полями id, name, email и указать типы этих полей (например, id - целое число, name - строка, email - строка). 

* Валидация данных:
Когда FastAPI получает данные в запросе, Pydantic автоматически проверяет, соответствуют ли эти данные объявленным моделям. Если данные не соответствуют, Pydantic выдаст ошибку, указывающую на несоответствие. 

* Сериализация данных:
Pydantic также может преобразовывать данные из одного формата в другой. Например, если в ответе API требуется вернуть данные в формате JSON, Pydantic автоматически сериализует данные из моделей в JSON. 

* Автоматическая документация

#### Основные сценарии использования:

* Валидация запросов/ответов в веб-фреймворках (FastAPI, Starlette).

* Конфигурация приложений (например, через .env).

* Работа с ORM (например, SQLAlchemy).

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

* Если тип не совпадает, пытается привести его (например, "123" → 123).

* Если приведение невозможно, вызывает ValidationError.

Пример:

```sh
from pydantic import ValidationError

try:
    User(id="not_an_int", name="Alice")
except ValidationError as e:
    print(e.errors())
```
### 4) Чем отличается BaseModel от dataclass в Pydantic?
#### BaseModel

* Встроенная валидация данных.	

* Поддержка alias, json_schema.

* Методы model_dump(), dict(), model_validate().

#### dataclass

* Нет валидации (только аннотации типов).

* Только стандартные dataclass-функции.

* Только dataclasses.asdict().
 
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
* Через присваивание значения в объявлении класса:

```sh
class User(BaseModel):
    id: int
    role: str = "user"  # Значение по умолчанию
```

* В Pydantic значения по умолчанию для полей модели задаются с помощью параметра default в функции Field или с помощью default_factory для динамически генерируемых значений.
```sh
from pydantic import BaseModel, Field
import uuid

class Item(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    name: str = "Item"
    price: float = 0.0
```
### 8) Как определить кастомный валидатор для поля модели в Pydantic?
Для создания кастомного валидатора поля модели в Pydantic используется декоратор @field_validator, который применяется к функции, выполняющей валидацию. Эта функция принимает значение поля в качестве аргумента и может возвращать измененное значение или возбуждать исключение ValueError при ошибке валидации. 

```sh
from pydantic import BaseModel, field_validator, ValidationError

class Item(BaseModel):
    price: float
    quantity: int

    @field_validator('price')
    def price_must_be_positive(cls, value):
        if value <= 0:
            raise ValueError('Цена должна быть положительной')
        return value

    @field_validator('quantity')
    def quantity_must_be_positive(cls, value):
        if value <= 0:
            raise ValueError('Количество должно быть положительным')
        return value

# Пример использования
try:
    item = Item(price=10.5, quantity=5)
    print(item)

    item = Item(price=-5.0, quantity=2)
    print(item) # Этот код не выполнится, т.к. выше будет исключение
except ValidationError as e:
    print(e)
```
### 9) В чем разница между @validator, @root_validator, @before, @after, @wrap, и @plain валидаторами?
@validator — проверяет отдельное поле.

@root_validator — работает со всей моделью (все поля сразу).

#### pydantic.functional_validators:

* Before валидаторы запускаются перед внутренним анализом и проверкой Pydantic (например, приведение str к int ). Они более гибкие, чем валидаторы After , поскольку они могут изменять необработанные входные данные, но им также приходится иметь дело с необработанными входными данными, которые теоретически могут быть любым произвольным объектом.

* After валидаторы выполняют внутренний анализ Pydantic. Они, как правило, более типобезопасны и, следовательно, их легче реализовать.

* Wrap являются наиболее гибкими из всех. Вы можете запустить код до или после того, как Pydantic и другие валидаторы сделают свое дело, или вы можете немедленно прекратить проверку, как при успешном значении, так и при ошибке.

* Plain валидаторы похожи на валидатор mode='before' но они немедленно прекращают проверку, дальнейшие валидаторы не вызываются, и Pydantic не выполняет никакой внутренней проверки.


### 10) Когда следует использовать @before валидатор и какие задачи он решает?
BeforeValidator используется для применения функции валидации перед основной проверкой поля. Это полезно, когда нужно преобразовать или нормализовать значение перед его проверкой.

Пример использования:
```sh
from pydantic import BaseModel, functional_validators as fv

def normalize_phone(phone: str) -> str:
    return phone.replace("-", "").replace(" ", "")

class Contact(BaseModel):
    phone: str = fv.BeforeValidator(normalize_phone)
```
В этом примере normalize_phone удаляет дефисы и пробелы из номера телефона. BeforeValidator применяется к полю phone, чтобы нормализовать значение перед его проверкой.

### 11) Как использовать @after валидатор и в каких случаях он применим?
AfterValidator используется для применения функции валидации после основной проверки поля. Это полезно для дополнительной обработки или проверки значения после его успешной проверки.

```sh
from pydantic import BaseModel, functional_validators as fv

def validate_length(value: str) -> str:
    if len(value) < 5:
        raise ValueError("Value must be at least 5 characters long")
    return value

class Message(BaseModel):
    content: str = fv.AfterValidator(validate_length)
```
Здесь validate_length проверяет, что длина значения content не менее 5 символов. AfterValidator применяется к полю content, чтобы дополнительно проверить длину значения после его основной проверки.

### 12) Что такое @wrap валидатор и как он позволяет обернуть процесс валидации?
WrapValidator используется для создания валидатора, который оборачивает функцию валидации вокруг поля. Это позволяет применять пользовательские функции валидации к значениям полей.

```sh
from pydantic import BaseModel, functional_validators as fv

def validate_age(age: int) -> int:
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

class Person(BaseModel):
    name: str
    age: int = fv.WrapValidator(validate_age)
```
В этом примере validate_age — это функция, которая проверяет, что возраст не является отрицательным. WrapValidator применяется к полю age, чтобы автоматически вызывать validate_age при проверке значения поля.
### 13) Как работает @plain валидатор и чем он отличается от других типов валидаторов?
PlainValidator используется для создания простого валидатора, который применяет функцию валидации к значению поля без дополнительных параметров.

```sh
from pydantic import BaseModel, functional_validators as fv

def validate_email(email: str) -> str:
    if "@" not in email:
        raise ValueError("Email must contain '@'")
    return email

class User(BaseModel):
    email: str = fv.PlainValidator(validate_email)
```
Здесь validate_email проверяет, что адрес электронной почты содержит символ @. PlainValidator применяется к полю email, чтобы автоматически вызывать validate_email.

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
* allow_mutation: если установлено значение False, делает модель неизменяемой после создания. По умолчанию True.

* extra: определяет, как модель должна обрабатывать дополнительные (не определённые в модели) поля при валидации. Возможные значения:

Extra.forbid: запрещает дополнительные поля (по умолчанию).

Extra.ignore: игнорирует дополнительные поля.

Extra.allow: позволяет дополнительные поля.

* validate_assignment: если установлено значение True, включает проверку значений при присваивании новых значений атрибутам модели. По умолчанию False.

* orm_mode: если установлено значение True, позволяет использовать модели Pydantic с ORM (Object-Relational Mapping) библиотеками, такими как SQLAlchemy. По умолчанию False.

* populate_by_name: если установлено значение True, позволяет устанавливать значения полей модели, используя имена полей, а не атрибуты. По умолчанию False.

* arbitrary_types_allowed: если установлено значение True, позволяет использовать типы данных, которые не являются подклассами BaseModel или встроенных типов данных Python. По умолчанию False.

* json_encoders: словарь, который определяет пользовательские функции кодирования для определённых типов данных при сериализации в JSON.

* frozen: если установлено значение True, делает модель неизменяемой после создания. Эквивалентно allow_mutation=False.

### 18) Как работает метод dict() в Pydantic и какие параметры он поддерживает?
Метод dict() в Pydantic используется для преобразования модели в обычный словарь Python. Это может быть полезно при необходимости работы с данными вне контекста Pydantic или при сериализации данных.

exclude (опциональный): позволяет исключить определённые поля из словаря. Принимает либо набор имён полей (в виде строк), либо словарь, где ключами являются имена полей, а значениями — булевы значения (если значение True, поле будет исключено).

include (опциональный): позволяет включить только определённые поля в словарь. Работает аналогично параметру exclude, но, наоборот, включает только указанные поля.

by_alias (опциональный, булев тип): если установлен в True, использует псевдонимы полей (aliases) вместо их имён при преобразовании в словарь.

skip_defaults (опциональный, булев тип): если установлен в True, исключает поля со значениями по умолчанию из словаря.

skip_none (опциональный, булев тип): если установлен в True, исключает поля со значением None из словаря.

```sh
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str
    age: int = 30  # значение по умолчанию

user = User(id=1, name="John Doe", email="john.doe@example.com")

# Преобразование модели в словарь без параметров
user_dict = user.dict()
print(user_dict)  # {'id': 1, 'name': 'John Doe', 'email': 'john.doe@example.com', 'age': 30}

user_dict_exclude = user.dict(exclude={'age': True})
print(user_dict_exclude)
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
```
get_db — это dependency, которая создает и закрывает соединение с БД.

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

def send_email(email: str):
    print(f"Sending email to {email}")

@app.post("/send-email/")
async def send_email_background(background_tasks: BackgroundTasks, email: str):
    background_tasks.add_task(send_email, email)
    return {"message": "Email will be sent in the background"}
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

В FastAPI есть несколько типов middleware, которые можно использовать для обработки запросов и ответов. Некоторые из них применяются по умолчанию, а другие можно добавить вручную.

По умолчанию в FastAPI применяются следующие middleware:

* CorrelationIdMiddleware (если явно не отключено) — добавляет уникальный идентификатор корреляции в заголовки запроса и ответа, что полезно для отслеживания запросов в логах.
* TrustedHostMiddleware — проверяет, что хост, с которого поступает запрос, доверенный, и отклоняет запросы с недоверенных хостов.
* HTTPSRedirectMiddleware — перенаправляет HTTP-запросы на HTTPS, если приложение настроено на работу с HTTPS.
* ExceptionHandlerMiddleware — обрабатывает исключения, возникающие в процессе обработки запросов, и возвращает соответствующие ответы об ошибках.
* CORS middleware (Cross-Origin Resource Sharing) — позволяет управлять доступом к ресурсам приложения с разных источников, предотвращая запросы с небезопасных доменов.
* BodyMiddleware — обрабатывает тело запроса, преобразуя его в нужный формат (например, JSON).
* Также можно добавить пользовательские middleware для реализации специфических функций, таких как логирование, аутентификация, авторизация и т. д. Для этого нужно создать класс, наследующий от BaseHTTPMiddleware, и определить методы для обработки запросов и ответов.
* Затем этот класс нужно зарегистрировать в приложении FastAPI с помощью метода add_middleware.


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
В FastAPI состояние сессии можно управлять через использование объекта state в объекте запроса (Request). FastAPI предоставляет возможность хранить и получать доступ к состоянию в объекте запроса, что удобно для обмена данными между промежуточным ПО и обработчиками запросов. 
Как это работает:
1. Доступ к объекту state:
Объект state доступен внутри обработчиков запросов через request.state. Он представляет собой словарь, в котором можно хранить любые данные.
2. Инициализация state:
state обычно инициализируется в промежуточном ПО (middleware) или при создании приложения. Например, в промежуточном ПО можно установить начальное значение для state.
3. Использование state:
В обработчиках запросов вы можете получить доступ к данным, сохраненным в state, и использовать их для различных целей, таких как хранение информации о пользователе, сессии или других данных, связанных с запросом. 

Пример:

```sh
from fastapi import FastAPI, Request

app = FastAPI()

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    """
    Пример промежуточного ПО для инициализации state.
    """
    request.state.user_id = 123  # Инициализация user_id в state
    response = await call_next(request)
    return response

@app.get("/")
async def read_root(request: Request):
    """
    Обработчик запроса для получения user_id из state.
    """
    user_id = request.state.user_id
    return {"user_id": user_id}
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
from fastapi import FastAPI

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Код, который нужно выполнить при запуске приложения
    print("Приложение стартует...")
    # Подключение к базе данных (пример)
    # db_connection = await connect_to_db()
    yield
    # Код, который нужно выполнить при остановке приложения
    print("Приложение завершает работу...")
    # Закрытие соединения с базой данных (пример)
    # await db_connection.close()

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def read_root():
    return {"message": "Hello World"}
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
