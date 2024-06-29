#імпортация всіх модулів
import flask, os, pandas
from project.settings import db
from shop_page.models import Product
from registration_page.models import User

#Функція відображення сторінки shop.html 

def render_shop():
    print(Product.query.count())
    if Product.query.count() >= 4:
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
        