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

    def execute_one(self, query, enable_fetch: bool = True):
        '''
        Executes one query
        '''
        try:
            with self.get_db_connection() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(query)
                    connection.commit()
                    if enable_fetch:
                        response = cursor.fetchall()
                    else:
                        response = None
        except Exception as e:
            raise(e)
        return response

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


class DataBase(DBConnector):
    '''
    Class to handle the companies and employees schema
    '''

    def __init__(self, schema='sandbox'):
        self.schema = schema

    def create_schema(self):
        '''
        Create the schema
        '''
        self.execute_multiple([
            f'''
            DROP SCHEMA IF EXISTS {self.schema} CASCADE;
            ''',
            f'''
            CREATE SCHEMA {self.schema};
            ''',
            f'''
            CREATE TABLE {self.schema}.employee (
                employee_id serial PRIMARY KEY,
                first_name varchar(50) NOT NULL,
                last_name varchar(50) NOT NULL,
                email varchar(50) UNIQUE NOT NULL,
                phone1 varchar(50) NOT NULL,
                phone2 varchar(50) NOT NULL
            );
            ''',
            f'''
            CREATE TABLE {self.schema}.company (
                company_id serial PRIMARY KEY,
                name varchar(50) UNIQUE NOT NULL,
                address varchar(50) NOT NULL,
                city varchar(50) NOT NULL,
                state varchar(50) NOT NULL,
                zip varchar(50) NOT NULL
            );
            ''',
            f'''
            CREATE TABLE {self.schema}.department (
                department_id serial PRIMARY KEY,
                name varchar(50) UNIQUE NOT NULL
            );
            ''',
            f'''
            CREATE TABLE {self.schema}.employee_company(
            id serial PRIMARY KEY,
            employee_id INT NOT NULL,
            company_id INT NOT NULL,
            department_id INT NOT NULL,
            UNIQUE (employee_id, company_id, department_id),
            FOREIGN KEY (employee_id)
                REFERENCES {self.schema}.employee (employee_id),
            FOREIGN KEY (company_id)
                REFERENCES {self.schema}.company (company_id),
            FOREIGN KEY (department_id)
                REFERENCES {self.schema}.department (department_id)
            );
            '''
        ])

    def get_employees_details(self):
        '''
        Returns a list of employees with their details
        '''
        response = self.execute_one(f'''
            SELECT e.*,c.*,d.*
            FROM {self.schema}.employee_company ec
            INNER JOIN {self.schema}.employee e
                on e.employee_id = ec.employee_id
            INNER JOIN {self.schema}.company c
                on c.company_id = ec.company_id
            INNER JOIN {self.schema}.department d
                on d.department_id = ec.department_id;
        ''')
        return response


class Employee(DataBase):
    '''
    This class manage the employee table
    '''
    table = 'employee'

    def __init__(self):
        DataBase.__init__(self)

    def insert(self, first_name: str, last_name: str, email: str, phone1: str, phone2: str) -> int:
        '''
        Inserts an employee into the database and returns the id
        '''
        response = self.execute_one(
            f'''
            INSERT INTO {self.schema}.{self.table}(first_name, last_name, email, phone1, phone2)
            VALUES('{first_name}', '{last_name}',
                   '{email}', '{phone1}', '{phone2}')
            ON CONFLICT(email) DO UPDATE
                SET email = excluded.email
            RETURNING employee_id;
            '''
        )
        return response[0][0]


class Company(DataBase):
    '''
    This class manage the company table
    '''
    table = 'company'

    def __init__(self):
        DataBase.__init__(self)

    def insert(self, name: str, address: str, city: str, state: str, zip_code: str) -> int:
        '''
        Inserts a company into the database and returns the id
        '''
        response = self.execute_one(
            f'''
            INSERT INTO {self.schema}.{self.table}(name, address, city, state, zip)
            VALUES('{name}', '{address}', '{city}', '{state}', '{zip_code}')
            ON CONFLICT(name) DO UPDATE
                SET name=excluded.name
            RETURNING company_id;
            '''
        )
        return response[0][0]


class Department(DataBase):
    ''' *
    This class manage the department table
    '''

    table = 'department'

    def __init__(self):
        DataBase.__init__(self)

    def insert(self, name: str) -> int:
        '''
        Inserts a department into the database and returns the id
        '''
        response = self.execute_one(
            f'''
            INSERT INTO {self.schema}.{self.table}(name)
                VALUES('{name}')
            ON CONFLICT(name) DO UPDATE
                SET name=excluded.name
            RETURNING department_id;
            '''
        )
        return response[0][0]


class CompanyEmployee(DataBase):
    '''
    This class manage the company employee, it manages
    the links between the company, the employee and the department.
    '''
    table = 'employee_company'

    def __init__(self):
        DataBase.__init__(self)

    def insert(self, employee_id: int, company_id: int, department_id: int):
        '''
        Inserts a company employee into the database
        '''
        self.execute_one(
            f'''
            INSERT INTO {self.schema}.{self.table}(
                employee_id, company_id, department_id
            )
            VALUES({employee_id}, {company_id}, {department_id})
            ON CONFLICT(employee_id, company_id, department_id) DO UPDATE
                SET employee_id=excluded.employee_id,
                    company_id=excluded.company_id,
                    department_id=excluded.department_id
            RETURNING id;
            '''
        )
