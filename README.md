# Project name / Назва проекту: Shop<br/>

<br/>This is an electronic store where users can buy products / Це електронний магазин де користувачі можуть купити товари<br/> 
<br/>The project supports and contributes to / Проект підтримує й вносить вклад:<br/>

Dmytro Levkivskyi / Дмитро Левківський - https://github.com/Levkivskiydmitro<br/>
Dmytro Pechenyuk / Дмитро Печенюк - https://github.com/DmitriyPechenyuk0<br/>
Artem Svistun / Артем Свістун - https://github.com/asvistun5<br/>

Shop Project - is a web application for managing an online store. It allows users to browse products, add them to the cart, 
make an order and make a payment  /  це веб-додаток для управління інтернет-магазином. Він дозволяє користувачам переглядати товари, додавати їх у кошик, 
робити замовлення та здійснювати оплату.

# Languages ​​used in this project / Мови які застосовувались у цьому проекті<br/>

<b>python 3.12.3</b> - The main language of the project, used for backend development / Основна мова проекту, використовується для backend розробки<br/>
<b>js 1.0</b> - It is used to create interactive website pages / Використовуєтся для создання інтерактивних сторінок сайту<br/>
<b>html 5</b> - It is used to create templates / Використовуєтся для створення шаблонів <br/>
<b>css 3</b> - It is used to work with styles / Використовуєтся для роботи зі стилями<br/>

# Technologies used in this project / Технології які використовувались у цьому проекті<br/>

<b>flask 3.0.3</b> -  The main module on which the site is written / Основний модуль на якому написан сайт<br/>
<b>flask_sqlalchemy 3.1.1</b> - A module for working with a database / Модуль для роботи з базою даних<br/>
<b>flask_migrate 4.0.7</b> - Database initialization module / Модуль для ініціалізації бази даних<br/>
<b>flask_mail 0.10.0</b> - Module for sending a message to the user's mail / Модуль для відправлення повідомлення на почту користувача<br/>
<b>flask_login 0.6.3</b> - Для реєстрації користувача на сайті / Модуль для реєстрації користувача на сайті<br/>
<b>os</b> - Module for working with the system / Модуль для роботи з системою<br/>
<b>telebot 0.0.5</b> - Module for creating and configuring bot telegrams / Модуль Для створення та налаштування телеграмм бота<br/>
<b>sqlite3</b> - A module for working with a database  / Модуль для роботи с базою данних<br/>
<b>Jinja2 3.1.3</b> - A module for creating templates and blocks / Модуль для створення шаблонів та блоків<br/>
<b>pandas 2.2.2</b> - Module for reading and parsing data from excel tables / Модуль для читання та парсу даних з excel таблиці<br/>
<b>openpyxl 3.1.2</b> - Module for correct reading of excel tables / Модуль для коректного читання excel таблиці<br/>

#  Project structure / Структура проекту:

![alt text]("Image")
image.png 

# home app / Додаток home:

```python
#імпортуємо модуль flask
import flask

#створення додатку
home = flask.Blueprint(
    name='home',
    import_name='home_page',
    template_folder='templates',
    static_folder="../static/home_page"
)

```

# Views.py of our apps / Views.py наших додатків

### home:

```python
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
```

### admin:

```python
import flask
from registration_page.models import User
from shop_page.models import Product
from project.settings import db
import os

def render_admin():

    # Перевірка, чи метод запиту є POST
    if flask.request.method == 'POST':
        try:
            
            if flask.request.form.get('submit-change') != None:
                # Розділяємо значення, отримані з форми
                list_values = flask.request.form.get('submit-change').split('-')
                
                # Отримуємо назву продукту за його ID
                product_name = Product.query.get(int(list_values[1]))
                
                # Зміна зображення продукту
                if list_values[0] == 'image':
                    # os.remove(os.path.abspath(__file__ + f"/../../static/shop_page/img\\{product_name.name}.png"))
                
                    image_save = flask.request.files['image']

                    image_save.save(os.path.abspath(__file__ + f"/../../static/shop_page/img/{product_name.name}.png"))
                
                # Зміна назіви продукту
                elif list_values[0] == 'name':

                    get_name = flask.request.form.get('name')
                    
                    absolute_path = os.path.abspath(__file__ + f"/../../static/shop_page/img/")

                    os.rename(src= absolute_path + f'/{product_name.name}.png', dst= absolute_path + f'//{get_name}.png')
                    
                    # Змінюємо назву продукту в базі даних
                    product_name.name = get_name
                    
                    # Зберігаємо зміни в базі даних
                    db.session.commit()
            pass
        except Exception as e:
            print(f"{e}")

    # Відображення шаблону admin.html з передачею списку користувачів і продуктів
    return flask.render_template(template_name_or_list='admin.html', login = User.query.all(), products = Product.query.all())
```

### authorization:

```python
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
```

### cart:

```python
import flask, flask_login, flask_mail #імпортування модулів flask'у 
from registration_page.models import User #імпортуванння моделі користувача для взаємодіЇ з таблицею данних
from project.flask_mail import mail #імпортуємо з проекту наше повідомлення

#Функція відображення сторінки cart.html 

def render_cart():
    if flask.request.method == 'POST':
         if flask.request.form["form-order"]:
            text_message = flask_mail.Message(
                subject = flask.request.form["message"],
                recipients = [flask_login.current_user.email],
                sender= flask_login.current_user.login
            )
            print("success")
            #Надсилаємо повідомлення
            mail.send(text_message)

    #Використовуємо функцію render_template для ренедеру шаблону 
    return flask.render_template(template_name_or_list="cart.html", login=User.query.all())
```

### shop:

```python
#імпортация всіх модулів
import flask, os, pandas
from project.settings import db
from shop_page.models import Product
from registration_page.models import User

#Функція відображення сторінки shop.html 

def render_shop():

    if Product.query.count() >= 3:
        return flask.render_template(template_name_or_list= "shop.html", login = User.query.all(), products = Product.query.all())
    
    else:
        path = os.path.abspath(__file__ + '/../Product.xlsx')

        data = pandas.read_excel(path, header = None, names =['name', 'discount', 'price', 'count'])

        for row in data.iterrows():

            row = row[1]

            product = Product(
                name = row['name'],
                discount = row['discount'],
                price = row['price'],
                count = row['count']
            )
            db.session.add(product)
        db.session.commit()

        login = User.query.all()
        products = Product.query.all()
        
        #Рендер сторінки
        return flask.render_template(template_name_or_list= "shop.html", login = login, products = products)
```

### registration:

```python
import flask
from .models import User, db

def render_register():
    is_admin = False
    is_registered = False
    if flask.request.method == 'POST':

        user = User(
            login = flask.request.form['login'],
            email = flask.request.form['email'],
            password = flask.request.form['password'],
            is_admin = False
        )
        try:

            db.session.add(user)
            db.session.commit()
            is_registered = True
            
            return flask.redirect('/registration_next')

        except Exception as e:
            is_registered = False
            return f"{e}" 
           

              
    
    return flask.render_template(template_name_or_list="registration.html", is_registered = is_registered)

def render_register_next():


    return flask.render_template(template_name_or_list="registration_next.html")
```

