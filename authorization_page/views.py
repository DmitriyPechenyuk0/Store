#імпортация всіх модулів
import flask, flask_login
from project import login_manager
from registration_page.models import User

#Функція відображення сторінки auth.html 
def render_authorization_page():
    #Перевірка, чи метод запиту є POST
    if flask.request.method == "POST":
        #Перебираємо усіх користувачів з таким же логіном, як у формі
        for user in User.query.filter_by(login = flask.request.form['login']):
            #Перевірка, чи пароль співпадає
            if user.password == flask.request.form['password']:
                #Використовуємо flask_login для входу користувача
                flask_login.login_user(user)
                return flask.redirect('/home_user')
        return flask.redirect('/authorization_next')
    return flask.render_template('auth.html', is_auth = flask_login.current_user.is_authenticated)


#Функція відображення сторінки auth_register.html 
def render_authorization_next():
    return flask.render_template(template_name_or_list="auth_register.html")