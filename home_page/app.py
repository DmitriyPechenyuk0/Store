#імпортуємо модуль flask
import flask

#створення додатку
home = flask.Blueprint(
    name='home',
    import_name='home_page',
    template_folder='templates',
    static_folder="../static/home_page"
)
