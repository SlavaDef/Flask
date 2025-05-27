from flask import render_template, Flask
import html
from first.exenge_convector import exchange_converter2



# Створення екземпляру Flask без цього не буде працювати
# контроллер бажано щоб знаходився в папці webapp, в іншому випадку треба додаткові налаштування бо не видно теплейту
app = Flask(__name__)


#@app.route('/')
def entry_page() -> 'html':
    results = exchange_converter2('UAH','USD',4000)
    return render_template('home.html',
                           the_title = 'Welcome to search4letters on the web!', results=results)


@app.route('/')
def entry_page() -> 'html':
    #results = exchange_converter2('UAH','USD',4000)
    return render_template('main.html')




# запуск додатків, виклик методів без принт
if __name__ == '__main__':
    app.run(debug=True)