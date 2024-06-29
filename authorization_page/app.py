import flask

auth = flask.Blueprint(
    name="auth",
    import_name="authorization_page",
    template_folder="templates",
    static_folder="../static/authorization_page"
)