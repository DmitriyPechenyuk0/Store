import home_page, registration_page, authorization_page, shop_page, cart_page, admin_page
from .settings import project



home_page.home.add_url_rule('/', view_func=home_page.render_home, methods=['POST', 'GET'])
home_page.home.add_url_rule('/home_user', view_func=home_page.render_home_user, methods = ['POST', 'GET'])

registration_page.registration.add_url_rule('/registration', view_func=registration_page.render_register, methods=['POST', 'GET'])
registration_page.registration.add_url_rule('/registration_next', view_func=registration_page.render_register_next, methods=['POST', 'GET'])

authorization_page.auth.add_url_rule('/authorization', view_func=authorization_page.render_authorization_page, methods=['POST', 'GET'])
authorization_page.auth.add_url_rule('/authorization_next', view_func=authorization_page.render_authorization_next, methods=['POST', 'GET'])

shop_page.shop.add_url_rule('/shop', view_func=shop_page.render_shop, methods = ['POST', 'GET'])
# shop_page.shop.add_url_rule('/shop_next', view_func=shop_page.render_shop_next, methods = ['POST', 'GET'])

cart_page.cart.add_url_rule('/cart', view_func=cart_page.render_cart, methods=['POST', 'GET'])
cart_page.cart.add_url_rule('/cart_process', view_func=cart_page.render_cart_process, methods=['POST', 'GET'])
# cart_page.basket.add_url_rule('/basket', view_func=cart_page.render_cart, methods=['POST', 'GET'])

admin_page.admin.add_url_rule('/admin', view_func=admin_page.render_admin, methods=['POST', 'GET'])

project.register_blueprint(blueprint=registration_page.registration)

project.register_blueprint(blueprint=authorization_page.auth)

project.register_blueprint(blueprint=home_page.home)


project.register_blueprint(blueprint=cart_page.cart)

project.register_blueprint(blueprint=shop_page.shop)

project.register_blueprint(blueprint=admin_page.admin)