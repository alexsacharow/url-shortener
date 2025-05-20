Минималистичный сервис для сокращения длинных URL-адресов, написанный на
Python с использованием Flask.

# Особенности

- Преобразует длинные URL в короткие коды
- Проверяет валидность URL (требует корректного домена верхнего уровня)
- Принудительно использует HTTPS для всех ссылок
- Простое хранение данных в JSON-файле
- Кастомная страница 404

# Требования

- Python 3.10+
- Flask
- Полный список зависимостей в `requirements.txt`{.verbatim}

# Установка

1.  Клонируйте репозиторий:

    ``` {.bash org-language="sh"}
    git clone https://github.com/вашusername/url-shortener.git
    cd url-shortener
    ```

2.  Установите зависимости:

    ``` {.bash org-language="sh"}
    pip install -r requirements.txt
    ```

# Использование

1.  Запустите приложение:

    ``` {.bash org-language="sh"}
    flask app.py --reload
    ```

2.  Откройте веб-интерфейс по адресу `http://localhost:5000`{.verbatim}

3.  Введите URL в форму для сокращения

# Структура проекта

    .
    ├── app.py               # Основной код приложения
    ├── tlds_list.py         # Список валидных TLD
    ├── urls.json            # Хранилище сокращенных URL
    ├── templates/
    │   ├── index.html       # Шаблон главной страницы
    │   └── 404.html         # Шаблон страницы 404
    └── requirements.txt     # Зависимости

# Конфигурация

Настройки в `app.py`{.verbatim}:

- `BASE_DOMAIN`{.verbatim}: Публичный домен (по умолчанию:
  `http://127.0.0.1:5000`{.verbatim})
- `DATA_FILE`{.verbatim}: Путь к файлу хранилища (по умолчанию:
  `urls.json`{.verbatim})

# Лицензия

MIT License
