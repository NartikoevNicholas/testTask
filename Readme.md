Для работы данного скрипта необходимо:
1. https://docs.google.com/spreadsheets/d/1LTejK-Oo7L1bFreBIIcEZnF1W1RCC1s_jos3EuIP0jI/edit#gid=0
Скопировать этот файл в ваш google sheets
2. Создать google приложение подключить driver и sheets api. Создать сервесный аккаунт,
скачать key json, сохранить его под именем service_account.json и закинуть его в корень проекта.
И дать этому пользователю возможность редактировать файл sheets
3. Подключить к postgresql. Подключение происходит в файле settings/config.py необходимо указать:
localhost = ""
user = ""
port = ""
password = ""
db_name = ""[
4. Создать переменные окружения:
HOST = (Хост к базе данных, дефолт localhost(127.0.0.1))
PASSWORD = (Пароль пользователя бд)
CHAT_ID = (имя телеграмм канала, например есть https://t.me/nartikoevtest,
то указываем, CHAT_ID=nartikoevtest)
5. TOKEN = (токен телеграмм бота)
6. Запустить main.py

Ссылка на docker: 
