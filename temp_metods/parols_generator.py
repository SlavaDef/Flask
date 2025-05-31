import random
import string


def parols_generator(length):
    parols = []
    for i in range(length):
        parols.append(input(f'Enter the {i+1} parol: '))
    return parols


# Випадкова маленька літера
random_letter = random.choice(string.ascii_lowercase)  # a-z

# Випадкова велика літера
random_upper = random.choice(string.ascii_uppercase)  # A-Z

random_any = random.choice(string.ascii_letters) # a-z, A-Z

random_letter2 = random.choices(string.ascii_lowercase, k=4)

# Отримати рядок з 5 випадкових літер
random_string = ''.join(random.choices(string.ascii_lowercase, k=5))

random_string2 = ''.join(random.choices(string.ascii_letters, k=4))

random_digits = "".join(random.choices(string.digits, k=4))

#print(random_letter2)

def generate_random_password(numb):
    """Генерує випадковий пароль з літер цифр та знаків пунктуації."""
    chars = string.ascii_letters + string.digits + string.punctuation
    print(chars)
    return ''.join(random.choices(chars, k=numb))


def generate_random_password2():
    # Крок 1: створення chars
    chars = string.ascii_letters + string.digits
    print(f"Набір символів: {chars}")  # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789

    # Крок 2: вибір випадкових символів
    random_chars = random.choices(chars, k=12)
    print(f"Список випадкових символів: {random_chars}")  # наприклад: ['K', '2', 'f', 'H', '9', 'a', 'Z', 'x']

    # Крок 3: об'єднання в рядок
    password = ''.join(random_chars)
    print(f"Фінальний пароль: {password}")  # наприклад: K2fH9aZx

    return password


def my_generator(number):
    #return random_string2+random_digits+''.join(random.choices(string.ascii_letters, k=4))
    #return ''.join(random_string2+str(random_digits)+random_string2)
    chars = string.ascii_letters # випадкові літери
    nums = string.digits # випадкові числа
    temp = chars+nums+string.punctuation
    # через .join() виконуємо конкатенацію
    password = ''.join(random.choices(temp, k=number))
    return password


#print(my_generator(16))
print(my_generator(16))
#print(random.choices(string.digits, k=4))
#print(generate_random_password2())

