import os
import random
import string

from flask import render_template, Flask, request, session, flash, redirect, url_for
import html
from service.exenge_servise import exchange_converter
from service.number_cods_service import find_code_by_country, find_country_by_code
from service.parol_generator import generate_random_password
from service.blog_service_db import insert_post, get_post, create_table, delete_post, insert_data, \
    update_post, select_all_posts, update_database_schema, check_table_structure
from service.photo_saver import save_image, UPLOAD_FOLDER
from datetime import datetime

# Створення екземпляру Flask без цього не буде працювати
# контроллер бажано щоб знаходився в папці webapp, в іншому випадку треба додаткові налаштування бо не видно теплейту

app = Flask(__name__)
app.static_folder = 'static'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Обмеження розміру файлу (16MB)


app.secret_key = os.urandom(24) # без ключа сесії не працюють

 # Debug - Image path: None

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
        return render_template('create_post.html')
    title = str(request.form['title'])
    some_text = str(request.form['some_text'])
    author = str(request.form['author'])
    date = datetime.now().strftime('%d-%m-%Y %H:%M')

    image_path = None
    if 'image' in request.files:
        file = request.files['image']
        if file.filename != '':
            image_path = save_image(file)
            print(f"Saved image path: {image_path}")  # Для відладки

    try:
        insert_post(title, some_text, author, date, image_path)
        #return render_template('create_post.html', results="Пост успішно створено!")
        flash('Пост успішно створено!', 'success')  # Додаємо flash-повідомлення
        return redirect(url_for('blog_all_page'))  # Переадресація на метод в контроллері

    except Exception as e:
        print(f"Помилка при вставці: {str(e)}")
        # return render_template('create_post.html', results=f"Помилка: {str(e)}")
        flash(f"Помилка: {str(e)}", 'danger')  # Додаємо flash-повідомлення про помилку
        return redirect(url_for('blog_all_page'))




@app.route('/all_posts', methods = ['GET'])
def blog_all_page() -> 'html':
    results = select_all_posts()
    return render_template('all_posts.html',results=results)


@app.route('/delete/<int:post_id>', methods = ['POST'])
def delete_post_route(post_id):
    try:
        delete_post(post_id)
        flash('Пост успішно видалено', 'success')
    except Exception as e:
        flash(f'Помилка при видаленні поста: {str(e)}', 'error')
    return redirect(url_for('blog_all_page'))



@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update_post_route(post_id):
    if request.method == 'POST':

        try:
            title = request.form.get('title')
            some_text = request.form.get('some_text')
            author = request.form.get('author')  # отримуємо значення з форми

            # Обробка зображення
            image_path = None
            if 'image' in request.files and request.files['image'].filename != '':
                # Якщо нове фото не завантажене, передаємо None,
                # і функція update_post збереже існуюче

                file = request.files['image']
                image_path = save_image(file)

            # Викликаємо update_post з правильним порядком аргументів
            success = update_post(
                post_id=post_id,
                title=title,
                content=some_text,
                author=author,  # переконайтесь що це значення не None
                image_path=image_path
            )

            if success:
                flash('Пост успішно відредаговано', 'success')
            return redirect(url_for('blog_all_page'))

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
    #check_table_structure()
    #update_database_schema()
    #create_table()
    #insert_data()
    app.run(debug=True)