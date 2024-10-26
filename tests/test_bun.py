import pytest

from Diploma_1.bun import Bun


@pytest.fixture
def bun():
    """Фикстура для создания объекта Bun."""
    return Bun(name="Sesame Bun", price=1.5)

def test_bun_initialization(bun):
    """Тестируем корректную инициализацию."""
    assert bun.name == "Sesame Bun"
    assert bun.price == 1.5

def test_get_name(bun):
    """Тестируем метод get_name."""
    assert bun.get_name() == "Sesame Bun"

def test_get_price(bun):
    """Тестируем метод get_price."""
    assert bun.get_price() == 1.5
