from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

class NameForm(FlaskForm):
    username = StringField('Ваше ім\'я:')
    submit = SubmitField('Відправити')

class AgeForm(FlaskForm):
    birth_year = IntegerField('Рік народження:')
    submit = SubmitField('Відправити')

@app.route('/')
def index():
    """
    Функція обробляє кореневий маршрут ("/") та повертає просту НТМЛ сторінку з двома посиланнями: на ім'я та вік
    """
    greet_with_links = """<h1>Home</h1>
    <p><a href="/name">Введіть своє ім'я</a></p>
    <p><a href="/age">Введіть рік народження</a></p>"""
    return greet_with_links

@app.route('/name', methods=['GET', 'POST'])
def name():
    """
    Функція обробляє маршрут (name) , перенаправляє імя на greet, якщо POST запрос, якщо GET запрос -name.html
    """
    form = NameForm()
    if form.validate_on_submit():
        username = form.username.data
        return redirect(url_for('greet', username=username))
    return render_template('name.html', form=form)

@app.route('/greet/<username>')
def greet(username):
    """
    Функція обробляє маршрут "/greet/<username>". Приймає ім'я користувача як параметр
    """
    return render_template('greet.html', username=username)

@app.route('/age', methods=['GET', 'POST'])
def age():
    """
    Функція обробляє маршрут "/age"  обслуговує як GET, POST запити.
    При GET-запиті - age.html з екземпляром класу AgeForm.
    При POST-запиті якщо успішно, розраховує вік користувача на основі року народження та повертає повідомлення з віком.
    Якщо форма не проходить- 'age.html'
    """
    form = AgeForm()
    if form.validate_on_submit():
        birth_year = form.birth_year.data
        age = datetime.now().year - birth_year
        return f'Вам {age} років'
    return render_template('age.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
