from flask import render_template, Flask, request
import html

from service.exenge_servise import exchange_converter

# Створення екземпляру Flask без цього не буде працювати
# контроллер бажано щоб знаходився в папці webapp, в іншому випадку треба додаткові налаштування бо не видно теплейту
app = Flask(__name__)


@app.route('/')
def entry_page() -> 'html':
    return render_template('main.html')



@app.route('/res', methods = ['POST'])
def second_page() -> 'html':
    from_currency = str(request.form['from_currency'])
    to_currency = str(request.form['to_currency'])
    amount = int(request.form['amount'])
    results = str(exchange_converter(from_currency,to_currency,amount))
    return render_template('main.html', results=results)




# запуск додатків, виклик методів без принт
if __name__ == '__main__':
    app.run(debug=True)