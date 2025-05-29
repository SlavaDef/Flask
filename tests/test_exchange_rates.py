import unittest
from unittest.mock import patch

from service.exenge_servise import get_exchange_rates


class TestExchangeRates(unittest.TestCase):


    @patch('requests.get')
    def test_successful_exchange_rates(self, mock_get):
        # Підготовка тестових даних
        mock_response = {
            'success': True,
            'quotes': {
                'USDEUR': 0.85,
                'USDGBP': 0.73,
                'USDUAH': 37.5
            }
        }
        # Налаштовуємо мок
        mock_get.return_value.json.return_value = mock_response

        # Викликаємо метод
        result = get_exchange_rates()

        # Перевіряємо результати
        expected = {
            'EUR': round(1 / 0.85, 4),
            'GBP': round(1 / 0.73, 4),
            'UAH': round(1 / 37.5, 4)
        }
        self.assertEqual(result, expected)

    @patch('requests.get')
    def test_failed_exchange_rates(self, mock_get):
        # Підготовка даних для невдалого запиту
        mock_response = {
            'success': False
        }
        mock_get.return_value.json.return_value = mock_response

        # Перевіряємо, що виникає виняток
        with self.assertRaises(Exception) as context:
            get_exchange_rates()

        self.assertEqual(str(context.exception), "Помилка отримання даних")

    @patch('requests.get')
    def test_exchange_rates_with_different_base(self, mock_get):
        # Тест з іншою базовою валютою
        mock_response = {
            'success': True,
            'quotes': {
                'EURUSD': 1.18,
                'EURGBP': 0.86
            }
        }
        mock_get.return_value.json.return_value = mock_response

        result = get_exchange_rates(base='EUR')

        expected = {
            'USD': round(1 / 1.18, 4),
            'GBP': round(1 / 0.86, 4)
        }
        self.assertEqual(result, expected)



if __name__ == '__main__':
    unittest.main()



# 1. Використання декоратора `@patch`:
  #  - Мокуємо `requests.get` щоб не робити реальні HTTP-запити
  #  - Мок автоматично передається як аргумент у тестовий метод

# 2. Три тестових випадки:
  #  - Успішне отримання курсів валют
  #  - Помилка при отриманні даних
  #  - Тест з іншою базовою валютою

# 3. Структура кожного тесту:
  #  - Підготовка тестових даних (arrange)
  #  - Виконання методу (act)
  #  - Перевірка результатів (assert)
