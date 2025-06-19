import pymysql

from blog.db_connector.conection import UseDatabase
from blog.db_connector.creatung_table_db import create_db_and_table

db_config_ex = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': '1234',
    'database': 'my_blog',  # назва бази даних в якій вже створюємо таблиці
    'port': 3306,  # стандартний порт MySQL
    'charset': 'utf8mb4'
}



#create_db_and_table('my_blog')

with UseDatabase(**db_config_ex) as cursor:
    try:
        cursor.execute("""
        CREATE TABLE blog_example (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        content TEXT NOT NULL,
        image_path VARCHAR(255),
        video_path VARCHAR(255),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)""")

        print('Table created successfully')

    except pymysql.err.InternalError as e:
        print(f'Error: {e}')


def create_blog_example(title, content, image_path, video_path):
    """Створення блогу в базі даних"""
    with UseDatabase(**db_config_ex) as cursor:
        try:
            cursor.execute("""
            INSERT INTO blog_example (title, content, image_path, video_path)
            VALUES (%s, %s, %s, %s)""", (title, content, image_path, video_path))


            print('Blog created successfully')
        except pymysql.err.InternalError as e:
            print(f'Error: {e}')


