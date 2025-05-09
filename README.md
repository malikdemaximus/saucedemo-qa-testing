# 🚀 QA Testing Project: Saucedemo  
Проект с примерами тестирования сайта [Saucedemo](https://www.saucedemo.com/).  

## 📂 Структура  
- [Чек-листы](/checklists)  
- [Тест-кейсы](/test_cases)  
- [Баг-репорты](/bug_reports)  
- [Postman-коллекции](/postman_collections)  

## 🛠 Инструменты  
- Ручное тестирование  
- Postman (API)  
- SQL  

## 🔍 Как использовать  
1. Клонируй репозиторий.  
2. Открой файлы с тест-кейсами и баг-репортами.  
3. Запусти Postman-коллекции.  

## 🤖 Автотесты
### Запуск:
```bash
# Установка зависимостей:
pip install -r autotests/requirements.txt

# Запуск всех тестов:
pytest autotests/ --alluredir=allure-results

# Генерация отчёта:
allure serve allure-results
```

### Структура:
- `pages/` – Page Object Model.
- `tests/` – Тесты.
- `utils/` – Логирование.
