import flask, flask_sqlalchemy, flask_migrate, os

project = flask.Flask(
    import_name="project",
    template_folder="templates",
    static_folder='/static/',
    instance_path= os.path.abspath(__file__ + '/..')

)

project.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

db = flask_sqlalchemy.SQLAlchemy(app = project)

migrate = flask_migrate.Migrate(app = project, db = db)