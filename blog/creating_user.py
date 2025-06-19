import hashlib
import re
from typing import Tuple

from blog.db_connector.conection import UseDatabase
from blog.db_connector.creatung_table_db import db_config


def validate_email(email: str) -> bool:
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))


def create_user(username: str, email: str, password: str) -> Tuple[bool, str]:
    # Валідація даних
    if len(username) < 3:
        return False, "Ім'я користувача має бути довшим за 2 символи"

    if len(password) < 8:
        return False, "Пароль має бути довшим за 7 символів"

    if not validate_email(email):
        return False, "Неправильний формат email"

    try:
        with UseDatabase(**db_config) as cursor:
            # Перевірка на унікальність email
            cursor.execute("SELECT id FROM users WHERE email = %s", (email,))
            if cursor.fetchone():
                return False, "Користувач з таким email вже існує"

            # Хешування пароля
            password_hash = hashlib.sha256(password.encode()).hexdigest()

            # Створення користувача
            cursor.execute("""
                INSERT INTO users (username, email, password_hash)
                VALUES (%s, %s, %s)
            """, (username, email, password_hash))

            return True, "Користувач успішно створений"

    except Exception as e:
        return False, f"Помилка при створенні користувача: {e}"


success, message = create_user(
    username="john_doe2",
    email="john@exampl.com",
    password="secure_pas5555"
)
print(message)

# 1 = secure_password123
# 2 = secure_pas5555


#with UseDatabase(**db_config) as cursor:
  #  cursor.execute("SELECT * FROM users")
    #print(cursor.fetchall())