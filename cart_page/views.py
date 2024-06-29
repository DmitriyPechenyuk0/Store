import flask, flask_login, flask_mail #імпортування модулів flask'у 
from registration_page.models import User #імпортуванння моделі користувача для взаємодіЇ з таблицею данних
from project.flask_config import mail #імпортуємо з проекту наше повідомлення
from .models import Order #імпортуванння моделі заказа для взаємодіЇ з таблицею данних
# from bot_app.main import bot
from shop_page.models import Product
from project.settings import db

#Функція відображення сторінки cart.html 

def render_cart():

    if flask.request.method == 'POST':

        order = Order(
            username = flask.request.form['name'],
            surname = flask.request.form['surname'],
            phone = flask.request.form['phone'],
            email = flask.request.form['email'],
            city = flask.request.form['city'],
            poshta = flask.request.form['poshta'],
            wishes = flask.request.form['wishes']
        )

        try:

            text_message = flask_mail.Message(
                subject='Order',
                recipients=[''],
                sender=("")
            )

            mail.send(text_message)

            db.session.add(order)
            db.session.commit()

            return flask.redirect("/cart_process")
        except Exception as e:
            print(f"Error sending email: {e}")

    return flask.render_template(template_name_or_list="cart.html", login=User.query.all(), products = Product.query.all())

def render_cart_process():
    if flask.request.method == 'POST':
        print("canceled")
    return flask.render_template(template_name_or_list="cart_process.html", login=User.query.all(), products = Product.query.all())