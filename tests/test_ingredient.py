import pytest

from Diploma_1.ingredient import Ingredient


@pytest.fixture
def ingredient():
    """Фикстура для создания объекта Ingredient."""
    return Ingredient(ingredient_type="Filling", name="Cheese", price=1.5)

def test_initialization(ingredient):
    """Тест инициализации ингредиента."""
    assert ingredient.type == "Filling"
    assert ingredient.name == "Cheese"
    assert ingredient.price == 1.5

def test_get_price(ingredient):
    """Тест получения цены ингредиента."""
    assert ingredient.get_price() == 1.5

def test_get_name(ingredient):
    """Тест получения имени ингредиента."""
    assert ingredient.get_name() == "Cheese"

def test_get_type(ingredient):
    """Тест получения типа ингредиента."""
    assert ingredient.get_type() == "Filling"
