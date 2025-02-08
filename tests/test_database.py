import pytest

from Diploma_1.database import Database
from Diploma_1.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture
def db():
    """Фикстура для создания объекта базы данных."""
    return Database()


@pytest.mark.parametrize("name, price", [
    ("black bun", 100),
    ("white bun", 200),
    ("red bun", 300),
])
def test_available_buns(db, name, price):
    """Тест метода available_buns() с параметризацией."""
    buns = db.available_buns()
    matching_bun = next(bun for bun in buns if bun.get_name() == name)

    assert matching_bun.get_price() == price


@pytest.mark.parametrize("name, ingredient_type, price", [
    ("hot sauce", INGREDIENT_TYPE_SAUCE, 100),
    ("sour cream", INGREDIENT_TYPE_SAUCE, 200),
    ("chili sauce", INGREDIENT_TYPE_SAUCE, 300),
    ("cutlet", INGREDIENT_TYPE_FILLING, 100),
    ("dinosaur", INGREDIENT_TYPE_FILLING, 200),
    ("sausage", INGREDIENT_TYPE_FILLING, 300),
])
def test_available_ingredients(db, name, ingredient_type, price):
    """Тест метода available_ingredients() с параметризацией."""
    ingredients = db.available_ingredients()
    matching_ingredient = next(ingredient for ingredient in ingredients if ingredient.get_name() == name)

    assert matching_ingredient.get_type() == ingredient_type
    assert matching_ingredient.get_price() == price
