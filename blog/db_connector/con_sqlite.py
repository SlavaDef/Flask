# конекшн для sqlite3 який використовуємо для загального блог шоу

import sqlite3



class UseDatabase:
    def __init__(self, **config):
        self.config = config
        self.conn = None
        self.cursor = None


    def __enter__(self): # авто визов у блоці with
        try:
            self.conn = sqlite3.connect(**self.config)
            self.cursor = self.conn.cursor()
            return self.cursor
        except sqlite3.Error as e:
            raise Exception(f"Помилка бази даних: {e}")



    def __exit__(self, exc_type, exc_value, exc_trace):
        try:
            if self.cursor:
                self.cursor.close()
            if self.conn:
                if exc_type is None:
                    self.conn.commit()
                else:
                    self.conn.rollback()
                self.conn.close()

        except sqlite3.Error as e:
            # Можна або залогувати помилку, або підняти новий виняток
            raise Exception(f"Помилка при закритті з'єднання з БД: {e}")


    def init_db(self):
        with self as cursor:
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS blogs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title varchar(255),
                    text TEXT
                )
            ''')
