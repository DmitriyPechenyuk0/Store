import flask

cart = flask.Blueprint(
    name='cart',
    import_name='cart_page',
    template_folder='templates',
    static_folder="../static/cart_page"
)