import requests



def get_exchange_rates() -> str:
    url = "https://api.exchangerate.host/live?access_key=23142100ca89470941e805a448582c9c&currencies=USD,EUR,GBP,PLN,MXN&format=1"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
    #     print(data)
        return data


    else:
        return f"Помилка запиту: {response.status_code}"


def get_exchange_rates2(base='USD'):
    url = ('https://api.exchangerate.host/live?access_key='
           '23142100ca89470941e805a448582c9c&currencies=USD,EUR,GBP,PLN,UAH,JPY,TRY,TWD,AED,MXN,KRW,CNY,CAD,KZT,EGP,DKK,BRL&format=1')

    response = requests.get(url)
    data = response.json()

    if data['success']:
        rates = data['quotes']
        # перетворення типу: 'USDEUR' -> 'EUR': 0.88 заміна USD на пробіл
        di =  {k.replace(base, ''): v for k, v in rates.items()}
        return {currency: round(1 / rate, 4) for currency, rate in di.items()}
    else:
        raise Exception("Помилка отримання даних")



