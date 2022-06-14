from app import app
from app.models import DataBase
from flask.cli import FlaskGroup

# Initialize Flask app with Flask-CLI
cli = FlaskGroup(app)


@cli.command('migrate')
def migrate():
    '''
    This method is a mechanism to create
    the schema and tables.
    '''
    db = DataBase()
    db.create_schema()


if __name__ == "__main__":
    cli()
