# конвертер валют
from first.ipi import get_exchange_rates2

#rates = {
  #  'USD': 1.0,
  #  'EUR': 1.08,
  # 'UAH': 0.025,
  #  'GBP': 1.26,
  #  'PLN': 0.24,
  #  "None":0 }

rates = get_exchange_rates2('USD') #  данні отримуємо по ip у словник
#print("Поточні курси:", rates)  # подивимось що містить словник
rates['USD'] = 1.0
#print("Після додавання USD:", rates)

#rates['USD'] = 1.0

def exchange_converter() :

    print('Конвертер валют, введіть тільки валюту, у форматі USD, EUR, UAH, GBP, PLN:')

    while True:
        one = input('From: ').upper()
        if one == 'EXIT': break

        two = input('To: ').upper()
        if one == 'EXIT': break

        try:

            count = float(input('Ведіть суму: '))
            res = rates[one]/rates[two]*count
            print(f"{count} {one} = {res:.2f} {two}")
            #return f"{count} {one} = {res:.2f} {two}"  # використовуємо f-string для форматування

        except KeyError:
            print('Невідома валюта')
            #return str(rates['None'])

        except ValueError:
            print('Некоректна сума')
            #return str(rates['None'])

        except Exception as e:
            print(f"Помилка при отриманні курсів валют: {e}")
            return

def exchange_converter2(one,two,count) :

   # print('Конвертер валют, введіть тільки валюту, у форматі USD, EUR, UAH, GBP, PLN:')

   # while True:


        try:


            res = rates[one]/rates[two]*count
            #print(f"{count} {one} = {res:.2f} {two}")
            return f"{count} {one} = {res:.2f} {two}"  # використовуємо f-string для форматування

        except KeyError:
           # print('Невідома валюта')
            return str(rates['None'])

        except ValueError:
            #print('Некоректна сума')
            return str(rates['None'])

        except Exception as e:
            #print(f"Помилка при отриманні курсів валют: {e}")
            return e

#if __name__ == '__main__':
 #  exchange_converter()


#print(rates)