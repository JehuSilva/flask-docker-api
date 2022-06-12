import psycopg2
from app.config import Config


class DBConnector(Config):
    '''
    Connects to the postgres database
    '''

    def get_db_connection(self):
        '''
        Returns a connection to the database
        '''
        return psycopg2.connect(
            user=self.db_user,
            host=self.db_host,
            database=self.db_database,
            password=self.db_password,
        )

    def execute_one(self, query):
        '''
        Executes one query
        '''
        try:
            with self.get_db_connection() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(query)
                    connection.commit()
        except Exception as e:
            raise(e)

    def execute_multiple(self, queries: list):
        '''
        Executes multiple queries
        '''
        try:
            with self.get_db_connection() as connection:
                with connection.cursor() as cursor:
                    for query in queries:
                        cursor.execute(query)
                    connection.commit()
        except Exception as e:
            raise(e)


class Employee():
    '''
    This class manage the employee table
    '''

    def __init__(self):
        self.id = None
        self.first_name = None
        self.last_name = None
        self.email = None
        self.phone1 = None
        self.phone2 = None


class Company(DBConnector):
    '''
    This class manage the company table
    '''

    def __init__(self):
        self.id = None
        self.name = None
        self.address = None
        self.city = None
        self.state = None
        self.zip_code = None


class DataBase(DBConnector):
    '''
    Class to handle the companies and employees schema
    '''

    def __init__(self) -> None:
        pass

    def create_schema(self, schema='sandbox'):
        '''
        Create the schema sandbox
        '''
        self.execute_multiple([
            f'''
            DROP SCHEMA IF EXISTS {schema} CASCADE;
            ''',
            f'''
            CREATE SCHEMA {schema};
            ''',
            f'''
            CREATE TABLE {schema}.employee (
                id serial PRIMARY KEY,
                first_name varchar(50) NOT NULL,
                last_name varchar(50) NOT NULL,
                email varchar(50) NOT NULL,
                phone1 varchar(50) NOT NULL,
                phone2 varchar(50)
            );
            ''',
            f'''
            CREATE TABLE {schema}.company (
                id serial PRIMARY KEY,
                name varchar(50) NOT NULL,
                address varchar(50) NOT NULL,
                city varchar(50) NOT NULL,
                state varchar(50) NOT NULL,
                zip_code varchar(50) NOT NULL
            );
            ''',
        ])
