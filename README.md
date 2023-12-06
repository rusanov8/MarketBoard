# MarketBoard

MarketBoard - это проект доски объявлений с использованием технологии контейнеризации Docker.

## Установка и Запуск

### Без использования Docker

1. Убедитесь, что у вас установлен Python 3.x.

2. Клонируйте репозиторий:

    ```bash
    git https://github.com/rusanov8/MarketBoard.git
    ```

3. Перейдите в директорию проекта:

    ```bash
    cd MarketBoard
    ```

4. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

5. Создайте файл `.env` и настройте переменные окружения:

    ```env
    SECRET_KEY=your_secret_key

    # База данных
    DB_NAME=your_db_name
    DB_USER=your_db_user
    DB_PASSWORD=your_db_password
    DB_HOST=your_db_host
    ```

6. Примените миграции:

    ```bash
    python manage.py migrate
    ```

7. Запустите сервер:

    ```bash
    python manage.py runserver
    ```

8. Откройте http://localhost:8000 в вашем браузере.

### Используя Docker

1. Создайте файл `.env.docker` на основе `.env.docker.example` и настройте переменные окружения для базы данных.

2. Запустите приложение с помощью Docker Compose:

    ```bash
    docker-compose up --build
    ```

3. Откройте http://localhost:8000 в вашем браузере.

## Использование

После установки приложения вы можете создавать или обновлять объявления. Используйте веб-интерфейс или API для взаимодействия с приложением.