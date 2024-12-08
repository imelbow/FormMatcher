# Form Template Detection Service / Сервис определения шаблонов форм

**Select language / Выберите язык:**

- [English](#form-template-detection-service)
- [Русский](#сервис-определения-шаблонов-форм)

---

## Form Template Detection Service

A service for detecting form templates based on field types. The API accepts form data and determines the corresponding template or the types of all fields if no template is found.

### Functionality

- Detecting form templates based on provided fields
- Automatically detecting field types
- Supported data formats:
  - application/json
  - multipart/form-data
  - application/x-www-form-urlencoded

### Requirements

- Docker
- Docker Compose

### Quick Start

1. Clone the repository:
```bash
git clone https://github.com/imelbow/FormMatcher.git
cd FormMatcher
```

2. Copy the sample configuration file `config.yaml.sample` to `config.yaml`:
```bash
cp config.yaml.sample config.yaml
```
In the `config.yaml` file, replace the `dsn` value with:
```bash
mongodb://admin:password@mongodb:27017/forms_db?authSource=admin
```

3. Copy the `.env.sample` file to `.env`:
```bash
cp .env.sample .env
```
Replace the data in `.env`:
```bash
MONGODB_URL=mongodb://admin:password@mongodb:27017/forms_db?authSource=admin
MONGO_INITDB_ROOT_USERNAME=admin
MONGO_INITDB_ROOT_PASSWORD=password
```

4. Start the services:
```bash
docker-compose up -d
```

The service will be available at: http://localhost:8000

### API Documentation

After starting the service, the documentation will be available at the following addresses:
- Swagger UI: http://localhost:8000/docs
- Redoc: http://localhost:8000/redoc

#### Example Requests

1. Detect Contact Form Template:
```bash
curl -X POST http://localhost:8000/get_form \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "phone": "+7 999 999 99 99"
  }'
```

2. Detect Registration Form Template:
```bash
curl -X POST http://localhost:8000/get_form \
  -H "Content-Type: application/json" \
  -d '{
    "user_email": "test@example.com",
    "birth_date": "2024-01-01",
    "phone_number": "+7 999 999 99 99"
  }'
```

### Testing

To run tests:

```bash
# Inside the container
docker-compose exec app pytest

# Or locally after installing dependencies
pip install -r requirements.txt
pytest
```

### Supported Field Types

- email: Email address validation
- phone: Phone number validation (supports international formats)
- date: Supports dd.mm.yyyy and yyyy-mm-dd formats
- text: Text fields without special validation

### Configuration

Form templates are configured in the `config.yaml` file. A sample configuration is available in `config.yaml.sample`:

```yaml
mongodb:
  dsn: mongodb://root:example@mongodb:27017/forms_db?authSource=admin
  templates:
    - name: Contact form
      fields:
        email: email
        phone: phone
    - name: Registration
      fields:
        user_email: email
        birth_date: date
        phone_number: phone
```

---

## Сервис определения шаблонов форм

Сервис для определения шаблонов форм на основе типов полей. API принимает данные формы и определяет соответствующий шаблон или типы всех полей, если шаблон не найден.

### Функциональность

- Определение шаблона формы по переданным полям
- Автоматическое определение типов полей
- Поддержка форматов данных:
  - application/json
  - multipart/form-data
  - application/x-www-form-urlencoded

### Требования

- Docker
- Docker Compose

### Быстрый старт

1. Клонируйте репозиторий:
```bash
git clone https://github.com/imelbow/FormMatcher.git
cd FormMatcher
```

2. Скопируйте пример конфигурационного файла `config.yaml.sample` в `config.yaml`:
```bash
cp config.yaml.sample config.yaml
```
В файле `config.yaml` замените значение `dsn` на:
```bash
mongodb://admin:password@mongodb:27017/forms_db?authSource=admin
```

3. Скопируйте файл `.env.sample` в `.env`:
```bash
cp .env.sample .env
```
Замените данные в файле `.env`:
```bash
MONGODB_URL=mongodb://admin:password@mongodb:27017/forms_db?authSource=admin
MONGO_INITDB_ROOT_USERNAME=admin
MONGO_INITDB_ROOT_PASSWORD=password
```

4. Запустите сервисы:
```bash
docker-compose up -d
```

Сервис будет доступен по адресу: http://localhost:8000

### API Документация

После запуска сервиса документация доступна по следующим адресам:
- Swagger UI: http://localhost:8000/docs
- Redoc: http://localhost:8000/redoc

#### Примеры запросов

1. Определение шаблона контактной формы:
```bash
curl -X POST http://localhost:8000/get_form \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "phone": "+7 999 999 99 99"
  }'
```

2. Определение шаблона формы регистрации:
```bash
curl -X POST http://localhost:8000/get_form \
  -H "Content-Type: application/json" \
  -d '{
    "user_email": "test@example.com",
    "birth_date": "2024-01-01",
    "phone_number": "+7 999 999 99 99"
  }'
```

### Тестирование

Для запуска тестов выполните:

```bash
# Внутри контейнера
docker-compose exec app pytest

# Или локально после установки зависимостей
pip install -r requirements.txt
pytest
```

### Поддерживаемые типы полей

- email: Проверка корректности email адреса
- phone: Проверка телефонных номеров (поддержка международного формата)
- date: Поддержка форматов dd.mm.yyyy и yyyy-mm-dd
- text: Текстовые поля без специальной валидации

### Конфигурация

Шаблоны форм настраиваются в файле `config.yaml`. Пример конфигурации доступен в `config.yaml.sample`:

```yaml
mongodb:
  dsn: mongodb://root:example@mongodb:27017/forms_db?authSource=admin
  templates:
    - name: Contact form
      fields:
        email: email
        phone: phone
    - name: Registration
      fields:
        user_email: email
        birth_date: date
        phone_number: phone
```