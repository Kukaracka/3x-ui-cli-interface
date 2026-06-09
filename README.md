## Небольшой скрипт для взаимодействия с 3x-ui панелью через api. 

### Локальный запуск

Склонировать репозиторий

`git clone git@github.com:Kukaracka/3x-ui-cli-interface.git`

Перейти в папку 

`cd 3x-cli-interface`

Создать файл .env

`cp ./.env.example ./.env`

И заполнить его вашими данными с доступом в 3x-ui панель

Создать виртуальное окружение python и активировать

`python -m venv .venv`

Windows:

`.venv\Scripts\activate.bat`

Linux:

`source .venv/bin/activate`

Установить зависимости 

`pip install -r requirements.txt`

Запустить консольное приложение 

`python -m main`



