# Task_3 — UI-автотесты Stellar Burgers

E2E-тесты для [Stellar Burgers](https://stellarburgers.education-services.ru/) на Selenium + pytest + Allure.

## Структура

- `locators/` — локаторы элементов
- `pages/` — Page Object Model
- `tests/` — тесты по функциональности
- `helpers.py` — API-хелперы и `WebDriverFactory`
- `conftest.py` — фикстуры pytest

## Запуск

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

pytest --alluredir=allure_results
allure serve allure_results
```

## Покрытие

- Восстановление пароля
- Личный кабинет
- Основной функционал
- Лента заказов
