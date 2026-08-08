# Sprint_6 — UI-тесты «Яндекс.Самоката»

Проект покрывает автотестами раздел «Вопросы о важном», позитивный сценарий заказа
самоката с двух точек входа и переходы по логотипам в шапке сайта.
Архитектура тестов — Page Object Model, отчётность — Allure.

## Структура

```
Sprint_6/
├── locators/     # локаторы элементов, по одному модулю на страницу
├── pages/        # Page Object классы
├── tests/        # тесты
├── conftest.py   # фикстура браузера Firefox
├── data.py       # тестовые данные и константы
└── pytest.ini    # настройки pytest и Allure
```

## Запуск

Требуются Python 3.10+ и Mozilla Firefox.

```bash
python -m venv .venv
source .venv/Scripts/activate     # Windows (Git Bash)
pip install -r requirements.txt
pytest
```

Selenium Manager автоматически подбирает `geckodriver`.
По умолчанию Firefox запускается с интерфейсом, для headless-режима:

```bash
HEADLESS=1 pytest
```

## Allure-отчёт

Результаты прогона складываются в `allure-results` (настроено в `pytest.ini`).

```bash
allure generate allure-results -o allure-report --clean
allure open allure-report
```

Быстрый просмотр без сохранения отчёта: `allure serve allure-results`.

## Покрытые сценарии

| Файл | Что проверяется |
| --- | --- |
| `tests/test_faq.py` | 8 параметризованных тестов: раскрытие каждого вопроса FAQ и текст ответа |
| `tests/test_order.py` | 2 параметризованных теста: полный флоу заказа с кнопок вверху и внизу страницы |
| `tests/test_navigation.py` | переход на главную по логотипу «Самоката» и на Дзен по логотипу Яндекса |
