import unittest

from utils.search import find

# приклад з класом і юніт_тестами
class TestFind(unittest.TestCase):

    def test_find(self):
        # Викликаємо метод
        result = find('santabarbara', 'ab')

        # Перевіряємо результати
        expected = ['a', 'b']
        self.assertEqual(result, expected)


    def test_empty(self):
        # Викликаємо метод
        result = find('go up', ' ')

        # Перевіряємо результати
        expected = [' ']
        self.assertEqual(result, expected)

    def test_latin(self):
        # Викликаємо метод
        result = find('привіт', 'і')

        # Перевіряємо результати
        expected = ['і']
        self.assertEqual(result, expected)


    def test_no_matches(self):
        # Викликаємо метод
        result = find('bobbi vachington', 'x')

        # Перевіряємо результати
        expected = []
        self.assertEqual(result, expected)


    def test_with_numbers(self):
        # Викликаємо метод
        result = find('bobbi8 vachington12', '18')

        # Перевіряємо результати
        expected = ['1','8']
        self.assertEqual(result, expected)