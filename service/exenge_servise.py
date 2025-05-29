import requests
from utils.config_manager import config



# обект класу ConfigManager викликає свій метод api_url який повертає url
url = config.api_url


def exchange_converter(one, two, count) -> str:
    # метод отримує словник курсів валют і далі вже конвертує валюту
    try:

        rates = get_exchange_rates('USD')
        rates['USD'] = 1.0

        res = rates[one.upper()] / rates[two.upper()] * count
        # використовуємо f-string для форматування{res:.2f} 2_знаки після коми
        return f"{count} {one.upper()} = {res:.2f} {two.upper()}"

    except KeyError:
        return 'error, no such currency'

    except ValueError:
        return 'error, no such value'

    except Exception as e:
        return str(e)



def get_exchange_rates(base='USD') -> dict:
    # робимо словник з курсами валют
    response = requests.get(url)
    data = response.json()

    if data['success']:
        rates2 = data['quotes']
        # перетворення типу: 'USDEUR' -> 'EUR': 0.88 заміна USD на пробіл
        di =  {k.replace(base, ''): v for k, v in rates2.items()}
        return {currency: round(1 / rate, 4) for currency, rate in di.items()}
    else:
        raise Exception("Помилка отримання даних")