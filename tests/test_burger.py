import unittest
from unittest.mock import Mock

from Diploma_1.bun import Bun
from Diploma_1.burger import Burger
from Diploma_1.ingredient import Ingredient


class TestBurger(unittest.TestCase):
    def setUp(self):
        """Подготовка тестового окружения перед каждым тестом."""
        self.burger = Burger()

        # Мокаем объект Bun
        self.bun = Mock(spec=Bun)
        self.bun.get_price.return_value = 2.5  # Установите цену булочки
        self.bun.get_name.return_value = "Sesame Bun"

        # Мокаем ингредиенты
        self.ingredient1 = Mock(spec=Ingredient)
        self.ingredient1.get_price.return_value = 1.0
        self.ingredient1.get_name.return_value = "Cheese"
        self.ingredient1.get_type.return_value = "cheese"

        self.ingredient2 = Mock(spec=Ingredient)
        self.ingredient2.get_price.return_value = 1.5
        self.ingredient2.get_name.return_value = "Tomato"
        self.ingredient2.get_type.return_value = "vegetable"

    def test_set_buns(self):
        """Тест установки булочек."""
        self.burger.set_buns(self.bun)
        self.assertEqual(self.burger.bun, self.bun)

    def test_add_ingredient(self):
        """Тест добавления ингредиента."""
        self.burger.add_ingredient(self.ingredient1)
        self.assertIn(self.ingredient1, self.burger.ingredients)

    def test_remove_ingredient(self):
        """Тест удаления ингредиента по индексу."""
        self.burger.add_ingredient(self.ingredient1)
        self.burger.remove_ingredient(0)
        self.assertNotIn(self.ingredient1, self.burger.ingredients)

    def test_move_ingredient(self):
        """Тест перемещения ингредиента в новый индекс."""
        self.burger.add_ingredient(self.ingredient1)
        self.burger.add_ingredient(self.ingredient2)
        self.burger.move_ingredient(0, 1)
        self.assertEqual(self.burger.ingredients[1], self.ingredient1)

    def test_get_price(self):
        """Тест вычисления полной цены бургера."""
        self.burger.set_buns(self.bun)
        self.burger.add_ingredient(self.ingredient1)
        self.burger.add_ingredient(self.ingredient2)
        expected_price = 2.5 * 2 + 1.0 + 1.5  # Цена за две булочки и ингредиенты
        self.assertEqual(self.burger.get_price(), expected_price)

    def test_get_receipt(self):
        """Тест получения чека с информацией о бургере."""
        self.burger.set_buns(self.bun)
        self.burger.add_ingredient(self.ingredient1)
        self.burger.add_ingredient(self.ingredient2)

        expected_receipt = (
            "(==== Sesame Bun ====)\n"
            "= cheese Cheese =\n"
            "= vegetable Tomato =\n"
            "(==== Sesame Bun ====)\n\n"
            "Price: 7.5"
        )

        self.assertEqual(self.burger.get_receipt(), expected_receipt)

