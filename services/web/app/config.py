import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config():
    '''
    Credentials for the database
    '''
    db_user = os.getenv('POSTGRES_USER')
    db_host = os.getenv('POSTGRES_HOST')
    db_database = os.getenv('POSTGRES_DB')
    db_password = os.getenv('POSTGRES_PASSWORD')
    db_port = int(os.getenv('POSTGRES_PORT'))
