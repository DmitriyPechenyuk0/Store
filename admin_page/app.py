import flask

admin = flask.Blueprint(
    name='admin',
    import_name='admin_page',
    template_folder="templates",
    static_folder="../static/admin_page"
)