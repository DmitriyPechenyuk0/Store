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


