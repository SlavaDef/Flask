import sqlite3
from datetime import datetime

from blog.db_connector.con_sqlite import UseDatabase

db = UseDatabase(database='your_blog.db')

def create_table():
    try:
        with db as cursor:

            cursor.execute("""CREATE TABLE IF NOT EXISTS posts (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                title TEXT NOT NULL,
                                content TEXT NOT NULL,
                                author TEXT NOT NULL,
                                date TEXT NOT NULL,
                                image_path TEXT
                            )""")

            print('Table created successfully')

    except Exception as e:
        print(f'Error creating table: {e}')


def update_database_schema():
    try:
        with db as cursor:
            # Перевіряємо чи існує стовпець image_path
            cursor.execute("PRAGMA table_info(posts)")
            columns = [column[1] for column in cursor.fetchall()]

            if 'image_path' not in columns:
                # Додаємо новий стовпець
                cursor.execute("ALTER TABLE posts ADD COLUMN image_path TEXT")
                print('Таблицю успішно оновлено')
    except Exception as e:
        print(f'Помилка при оновленні таблиці: {e}')


def show_tables():
    with db as cursor:
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        print(tables)


def show_columns():
    with db as cursor:
        cursor.execute("PRAGMA table_info(posts);")
        columns = cursor.fetchall()
        print(columns)


def insert_data():
    with db as cursor:
        cursor.execute("""INSERT INTO posts (title, content, author, date) VALUES (?, ?, ?, ?)""",
                       ('First Post', 'This is the first post', 'John Doe', '2023-01-01'))
        cursor.execute("""INSERT INTO posts (title, content, author, date) VALUES (?, ?, ?, ?)""",
                       ('Second Post', 'This is the second post', 'Jane Doe', '2023-01-02'))
        cursor.execute("""INSERT INTO posts (title, content, author, date) VALUES (?, ?, ?, ?)""",
                       ('Third Post', 'This is the third post', 'John Doe', '2023-01-03'))
        cursor.execute("""INSERT INTO posts (title, content, author, date) VALUES (?, ?, ?, ?)""",
                       ('Fourth Post', 'This is the fourth post', 'Jane Doe', '2023-01-04'))


def insert_post(title, content, author,  date=None, image_path=None):
    if date is None:
        date = datetime.now().strftime('%d-%m-%Y %H:%M')

    try:
        with db as cursor:
            cursor.execute("""INSERT INTO posts (title, content, author, date, image_path) VALUES (?, ?, ?, ?, ?)""",
                           (title, content, author, date, image_path))

    except Exception as e:
         print(f'Error inserting post: {e}')
         raise


def delete_all_data():
    with db as cursor:
        cursor.execute("DELETE FROM posts")


def delete_post(post_id):
    try:
        with db as cursor:

            cursor.execute("DELETE FROM posts WHERE id = ?", (post_id,))
    except sqlite3.Error as e:
            raise Exception(f"Помилка бази даних: {str(e)}")



def update_post(post_id, title, content, author, image_path=None, date=None):

    if date is None:
        date = datetime.now().strftime('%Y-%m-%d')
    try:
        with db as cursor:
            # Якщо нове фото не завантажене, зберігаємо існуюче
            if image_path is None:
                cursor.execute('SELECT image_path FROM posts WHERE id = ?', (post_id,))
                result = cursor.fetchone()
                if result:
                    image_path = result[0]

            cursor.execute('''
               UPDATE posts 
               SET title = ?, content = ?, author = ?, date = ?, image_path = ? 
               WHERE id = ?
           ''', (title, content, author, date, image_path, post_id))
        return cursor.rowcount > 0 # Оновлення успішне

    except Exception as e:
        raise Exception(f"Помилка бази даних: {str(e)}")




def get_post(post_id):
    try:
        with db as cursor:
            cursor.execute("SELECT * FROM posts WHERE id = ?", (post_id,))
            post = cursor.fetchone()
            return post if post else None
    except Exception as e:
        print(f'Error getting post: {e}')
        raise



def select_all_posts():
    with db as cursor:
        cursor.execute("SELECT * FROM posts")
        posts = cursor.fetchall()
        return posts
        #for post in posts: print(post)


def check_table_structure():
    with db as cursor:
        cursor.execute("PRAGMA table_info(posts)")
        columns = cursor.fetchall()
        print("Структура таблиці:")
        for column in columns:
            print(column)



#if __name__ == '__main__':
   # create_table()
   # show_tables()
    #select_data()