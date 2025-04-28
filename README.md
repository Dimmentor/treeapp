  <h3 align="center">Древовидное меню на Django</h3>
  
### СТЕК:
* Django
* SQLite

### Для запуска необходимо:
* Скачать проект
* Установить зависимости:
  ```sh
  pip install requirements.txt
  ```
* Активировать виртуальное окружение:
  ```sh
  cd venv/Scripts
  activate
  ```
* База данных заполнена категориями и подкатегориями, можно использовать для просмотра её:
    ```sh
    Логин суперюзера: admin
    Пароль суперюзера: admin
    ```
* Либо создать новую БД и суперюзера(миграция уже создана):
    ```sh
    python manage.py migrate
    python manage.py createsuperuser
    Заполнить базу данных любыми категориями и подкатегориями
    ```
  
* Запуск сервера:
    ```sh
    python manage.py runserver
    ```
* Главное меню с категориями и подкатегориями:
    ```sh
    http://127.0.0.1:8000/
    ```
* Админка:
    ```sh
    http://127.0.0.1:8000/admin/
    ```
* Скрины:

  
![Снимок экрана 2025-04-28 103917](https://github.com/user-attachments/assets/f10b7c7e-90e3-4b14-9841-d7fa0e09754d)
![Снимок экрана 2025-04-28 103941](https://github.com/user-attachments/assets/9d5241f3-fdab-4a2f-b909-b744eea92315)
