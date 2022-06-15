DROP SCHEMA IF EXISTS directory CASCADE;

CREATE SCHEMA directory;

CREATE TABLE directory.employee (
    employee_id serial PRIMARY KEY,
    first_name varchar(50) NOT NULL,
    last_name varchar(50) NOT NULL,
    email varchar(50) UNIQUE NOT NULL,
    phone1 varchar(50) NOT NULL,
    phone2 varchar(50)
);

CREATE TABLE directory.company (
    company_id serial PRIMARY KEY,
    name varchar(50) UNIQUE NOT NULL,
    address varchar(50) NOT NULL,
    city varchar(50) NOT NULL,
    state varchar(50) NOT NULL,
    zip varchar(50) NOT NULL
);

CREATE TABLE directory.department (
    department_id serial PRIMARY KEY,
    name varchar(50) UNIQUE NOT NULL
);

CREATE TABLE directory.employee_company(
    id serial PRIMARY KEY,
    employee_id INT NOT NULL,
    company_id INT NOT NULL,
    department_id INT NOT NULL,
UNIQUE (employee_id, company_id, department_id),
FOREIGN KEY (employee_id)
    REFERENCES directory.employee (employee_id),
FOREIGN KEY (company_id)
    REFERENCES directory.company (company_id),
FOREIGN KEY (department_id)
    REFERENCES directory.department (department_id)
);