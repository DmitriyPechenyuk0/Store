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
                
                print(list_values)
                # Зміна зображення продукту
                if list_values[0] == 'image':
                    os.remove(os.path.abspath(__file__ + f"/../../../static/shop_page/img\\Iphone.jpg"))
                
                    image_save = flask.request.files['image']

                    image_save.save(os.path.abspath(__file__ + f"/../../../static/shop_page/img/Iphone.jpg"))
                
                # Зміна назіви продукту
                elif list_values[0] == 'name':



                    get_name = flask.request.form.get('name')
                    
                    absolute_path = os.path.abspath(__file__ + f"/../../static/shop_page/img/")

                    os.rename(src= absolute_path + f'/{product_name.name}.png', dst= absolute_path + f'//{get_name}.png')
                    
                    # Змінюємо назву продукту в базі даних
                    product_name.name = get_name

                    # Зберігаємо зміни в базі даних
                    db.session.commit()
                    
                elif list_values[0] == 'price':

                    product_name.price = flask.request.form.get('price')

                    # Зберігаємо зміни в базі даних
                    db.session.commit()
            
            if flask.request.form.get('submit-new-change') != None:
                
                new_product = Product(
                    name = flask.request.form['name'],
                    discount = flask.request.form['discount'],
                    price = flask.request.form['price'],
                    count = flask.request.form['count']
                )             

                db.session.add(new_product)
                db.session.commit()   

            # pass
        except Exception as e:
            print(f"{e}")

    # Відображення шаблону admin.html з передачею списку користувачів і продуктів
    return flask.render_template(template_name_or_list='admin.html', login = User.query.all(), products = Product.query.all())
