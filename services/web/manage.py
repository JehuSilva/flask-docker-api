from flask.cli import FlaskGroup

from app import app
from app.models import DataBase

cli = FlaskGroup(app)


@cli.command('migrate')
def migrate():
    '''
    This method migrate the schema
    '''
    db = DataBase()
    db.create_schema()


if __name__ == "__main__":
    cli()
