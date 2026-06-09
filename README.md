# 3x-ui CLI Interface

Небольшое консольное приложение для взаимодействия с панелью **3x-ui** через API.

## Установка и запуск

### 1. Клонирование репозитория

```bash
git clone git@github.com:Kukaracka/3x-ui-cli-interface.git
cd 3x-cli-interface
```

### 2. Настройка переменных окружения

Создайте файл `.env` на основе шаблона:

```bash
cp .env.example .env
```

Заполните файл своими данными для доступа к панели **3x-ui**.

### 3. Создание виртуального окружения

```bash
python -m venv .venv
```

Активируйте окружение:

**Windows**

```bat
.venv\Scripts\activate.bat
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

### 4. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 5. Запуск приложения

```bash
python -m main
```

## Требования

* Python 3.10+
* Доступ к панели 3x-ui
* Корректно заполненный файл `.env`

## Структура запуска

```text
git clone
    ↓
настройка .env
    ↓
создание venv
    ↓
установка зависимостей
    ↓
запуск приложения
```
