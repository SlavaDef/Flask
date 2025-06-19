import os
import random
import string

from flask import render_template, Flask, request, session, flash, redirect, url_for
import html
from service.exenge_servise import exchange_converter
from service.number_cods_service import find_code_by_country, find_country_by_code
from service.parol_generator import generate_random_password
from service.blog_service_db import select_data, insert_post, get_post, create_table, delete_post, insert_data, \
    update_post

# Створення екземпляру Flask без цього не буде працювати
# контроллер бажано щоб знаходився в папці webapp, в іншому випадку треба додаткові налаштування бо не видно теплейту

app = Flask(__name__)

app.secret_key = os.urandom(24) # без ключа сесії не працюють



@app.route('/')
def entry_page() -> 'html':
    return render_template('main2.html')


@app.route('/exchange', methods = ['POST','GET'])
def second_page() -> 'html':
    if request.method == 'GET':
        return render_template('main.html')
    from_currency = str(request.form['from_currency'])
    to_currency = str(request.form['to_currency'])
    amount = int(request.form['amount'])
    results = str(exchange_converter(from_currency,to_currency,amount))
    return render_template('exchange_rates.html', results=results)



@app.route('/generator', methods = ['POST','GET'])
def generator() -> 'html':
    if request.method == 'GET':
        return render_template('generator.html')
    number = int(request.form['numb'])
    res = generate_random_password(number)
    return render_template('generator.html', res=res)


@app.route('/generator2', methods=['POST','GET'])
def generate_password():
    if request.method == 'GET':
        return render_template('generator2.html')
    length = int(request.form.get('numb', 12))
    password_type = request.form.get('passwordType', 'all')
    use_uppercase = request.form.get('uppercase') == 'on'
    use_special = request.form.get('special') == 'on'

    # Базовий набір символів
    lowercase = string.ascii_lowercase
    digits = string.digits
    uppercase = string.ascii_uppercase if use_uppercase else ''
    special_chars = string.punctuation if use_special else ''

    # Вибір символів залежно від типу паролю
    if password_type == 'numbers':
        chars = digits
    elif password_type == 'alphanumeric':
        chars = lowercase + digits + uppercase
    else:  # all
        chars = lowercase + digits + uppercase + special_chars

    # Генерація паролю
    password = ''.join(random.choice(chars) for _ in range(length))

    return render_template('generator2.html', res=password)



@app.route('/guess', methods=['GET', 'POST'])
def guess():
    if request.method == 'GET':
        # Створюємо нову гру
        session['number'] = random.randint(1, 10)
        session['attempts'] = 0
        return render_template('guess_number.html')

    # POST запит
    if 'number' not in session:
        session['number'] = random.randint(1, 10)
        session['attempts'] = 0

    user_guess = int(request.form.get('guess', 0))
    session['attempts'] += 1

    if user_guess == session['number']:
        result = f"Ви виграли! Число було {session['number']}"
        # Скидаємо гру
        session.pop('number')
        session.pop('attempts')
    elif session['attempts'] >= 3:
        result = f"Ви програли! Число було {session['number']}"
        # Скидаємо гру
        session.pop('number')
        session.pop('attempts')
    else:
        attempts_left = 3 - session['attempts']
        result = f"Спробуйте ще раз! Залишилось спроб: {attempts_left}"

    return render_template('guess_number.html', res=result)



@app.route('/code', methods=['GET', 'POST'])
def country_code():
    if request.method == 'GET':
        return render_template('country_cods.html')

    country = request.form.get('country', '').strip()
    cod = request.form.get('cod', '').strip()

    res_country = None
    res_cod = None

    if country and not cod:  # якщо введена тільки країна
        res_country = find_code_by_country(country)
    elif cod and not country:  # якщо введений тільки код
        res_cod = find_country_by_code(cod)
    else:
        return render_template('country_cods.html',
                               error="Будь ласка, заповніть тільки одне поле")

    return render_template('country_cods.html', res_cod=res_cod, res_country=res_country)


@app.route('/blog2')
def blog_main_page() -> 'html':
    return render_template('blog_main.html')


@app.route('/blog', methods = ['POST','GET'])
def blog_page() -> 'html':
    if request.method == 'GET':
        return render_template('post.html')
    title = str(request.form['title'])
    some_text = str(request.form['some_text'])
    autor = str(request.form['autor'])
    insert_post(title, some_text, autor)
    return render_template('post.html')



@app.route('/all_posts', methods = ['GET'])
def blog_all_page() -> 'html':
    results = select_data()
    return render_template('all_posts.html',results=results)


@app.route('/delete/<int:post_id>', methods = ['POST'])
def delete_post_route(post_id):
    try:
        delete_post(post_id)
        flash('Пост успішно видалено', 'success')
    except Exception as e:
        flash(f'Помилка при видаленні поста: {str(e)}', 'error')
    return redirect(url_for('blog_all_page'))


@app.route('/update/<int:post_id>', methods = ['POST'])
def update_post_route(post_id):
    title = str(request.form['title'])
    some_text = str(request.form['some_text'])
    autor = str(request.form['autor'])
    try:
        update_post(post_id, title, some_text, autor)
        flash('Пост успішно відредаговано', 'success')
    except Exception as e:
        flash(f'Помилка при редагуванні поста: {str(e)}', 'error')
    return redirect(url_for('blog_all_page'))



@app.route('/post/<int:post_id>')
def post_detail(post_id):
    post = get_post(post_id)
    if post is None:
        return "Пост не найден", 404
    return render_template('post_detail.html', post=post)




# запуск додатків, виклик методів без принт
if __name__ == '__main__':
    #create_table()
    #insert_data()
    app.run(debug=True)