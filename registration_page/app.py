import flask

registration = flask.Blueprint(
    name="registration",
    import_name="registration_page",
    template_folder="templates",
    static_folder="../static/registration_page"
)