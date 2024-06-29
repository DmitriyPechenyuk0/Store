#імпортування модулів
import flask, flask_sqlalchemy, flask_sqlalchemy.query
from project.settings import db
from registration_page.models import User

#Функція відображення сторінки home.html 
def render_home():
    return flask.render_template(template_name_or_list='home.html')

#Функція відображення сторінки home_user_page.html 
def render_home_user():
    return flask.render_template(template_name_or_list='home_user_page.html', login=User.query.all())