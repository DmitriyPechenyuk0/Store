import flask_mail
from .settings import project



project.config["MAIL_SERVER"] = "smtp.gmail.com"
project.config["PORT"] = 587
project.config["MAIL_USE_TLS"] = True
project.config["MAIL_DEBUG"] = True
project.config["MAIL_USERNAME"] = ""
project.config["MAIL_PASSWORD"] = ""
project.config['MAIL_DEFAULT_SENDER'] = ''

mail = flask_mail.Mail(project)
mail.init_app(project)