import string
import random


def generate_random_password(numb: int=12) -> str:
    """Генерує випадковий пароль з літер цифр та знаків пунктуації."""
    try:
            if not isinstance(numb, int):
                 return 'error, enter only numbers'
            if numb < 8:
                 return 'error, password length must be at least 8 characters'
            if numb > 128:
                 return 'error, password length must be less than 128 characters'
            chars = string.ascii_letters + string.digits + string.punctuation
            return ''.join(random.choices(chars, k=numb))

    except Exception as e:
        return str(e)


print(generate_random_password())