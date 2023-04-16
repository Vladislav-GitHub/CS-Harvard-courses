import os
import sqlite3
from flask import Flask, Markup, flash, redirect, render_template, make_response, escape, url_for, request, session
from flask_session import Session
from tempfile import mkdtemp # This module creates temporary files and directories
from werkzeug.utils import secure_filename

import pickle
import numpy as np


# Configure application
app = Flask(__name__)

# Set the secret key
app.secret_key = os.urandom(24)

# Reload templates when they are changed.
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Markup('<strong>Hello, %s!</strong>') % '<blink>hacker</blink>'
# Markup.escape('<blink>hacker</blink>')
# Markup('<em>Marked up</em> &raquo; HTML').striptags() # это всё для экранирования escape-последовательностей

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route('/') # декоратор route(), чтобы сказать Flask, какой из URL должен запускать нашу функцию
def index():
    ''' Get data from user '''

    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    flash('You were successfully logged in')
    return 'You are not logged in'
    # username = request.cookies.get('username') # instead of cookies[key]
    # # Чтобы не получить в случае отсутствия cookie ошибку KeyError
    # # используйте cookies.get(key) вместо cookies[key]
    # resp = make_response(render_template(...))
    # resp.set_cookie('username', 'the username')
    # return resp
    # return 'Index page'


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''
        # if valid_login(request.form['username'],
        #                request.form['password']):
        #                return log_the_user_in(request.form['username'])
        # else:
        #     error = 'Invalid username/password'
    # следущий код выполняется при методе запроса GET
    # или при признании полномочий недействительными
    # return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    # удалить из сессии имя пользователя, если оно там есть
    session.pop('username', None)
    return redirect(url_for('index'))


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    flash('You were successfully logged in')
    return render_template('hello.html', name=name)
    # return '<h1>Hello World!</h1>'


@app.route('/user/<username>') # <variable_name>
def show_user_profile(username):
    '''Show user's profile'''
    return 'User: %s' % username


@app.route('/post/<int:post_id>') # <converter:variable_name>
def show_post(post_id):
    '''Show the message with id, where id is integer'''
    return 'Post: %d' % post_id


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('var/www/uploads/' + secure_filename(f.filename)) # instead of 'var/www/uploads/uploaded_file.txt'


@app.errorhandler(404)
def not_found():
    return render_template('error.html'), 404


# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     print(url_for('login', username='John Snow'))

# def function_1():
#     ...


# def function_2():
#     ...


# def function_n():
#     ...


if __name__ == "__main__": # сервер запустится только при непосредственном вызове скрипта
                           # из интерпретатора Python, а не при его импортировании в качестве модуля
    app.run(host='0.0.0.0') # для запуска локального сервера с нашим приложением, мы используем функцию run()