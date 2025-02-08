## Diploma project. Task 1: Unit-tests

### Autotests to check application for burger ordering in Stellar Burgers https://stellarburgers.nomoreparties.site/

### Реализованные сценарии

Unit-tests convering classes `Bun`, `Burger`, `Ingredient`, `Database`

Coverage percentage = 100% (report: `htmlcov/index.html`)

### Project structure

- `praktikum` - folder containing the application code
- `tests` - folder with tests divided by classes: `bun_test.py`, `burger_test.py`, etc

### How to launch tests

**Requirements installation**

> `$ pip install -r requirements.txt`

**Launching autotests and creation of an HTML-report and coverage report**

>  `$ pytest --cov=praktikum --cov-report=html`
