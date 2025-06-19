import pymysql

from blog.db_connector.conection import UseDatabase


db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': '1234',
    'database': 'user_blog',  # назва бази даних в якій вже створюємо таблиці
    'port': 3306,  # стандартний порт MySQL
    'charset': 'utf8mb4'
}



# створення бд та таблиці з налаштуваннями для адмін користувача root + пароль
def create_db_and_table(db_name):

        # Підключення до MySQL сервера
        try:
            # Спочатку створюємо базу даних
            with pymysql.connect(host='127.0.0.1',user='root',password='1234') as connection:
                with connection.cursor() as cursor:
                    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
                connection.commit()
                print("База даних створена успішно")

        except Exception as e:
            print(f"Помилка: {e}")



with UseDatabase(**db_config) as cursor:
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        for table in tables:
            print(table[0])



#create_db_and_table('user_blog')