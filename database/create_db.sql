-- This script is used to generate the schema in a PostgreSQL database.

DROP SCHEMA IF EXISTS sandbox CASCADE;

CREATE SCHEMA sandbox;

CREATE TABLE sandbox.employee (
    employee_id serial PRIMARY KEY,
    first_name varchar(50) NOT NULL,
    last_name varchar(50) NOT NULL,
    email varchar(50) UNIQUE NOT NULL,
    phone1 varchar(50) NOT NULL,
    phone2 varchar(50) NOT NULL
);

CREATE TABLE sandbox.company (
    company_id serial PRIMARY KEY,
    name varchar(50) UNIQUE NOT NULL,
    address varchar(50) NOT NULL,
    city varchar(50) NOT NULL,
    state varchar(50) NOT NULL,
    zip varchar(50) NOT NULL
);

CREATE TABLE sandbox.department (
    department_id serial PRIMARY KEY,
    name varchar(50) UNIQUE NOT NULL
);

CREATE TABLE sandbox.employee_company(
    id serial PRIMARY KEY,
    employee_id INT NOT NULL,
    company_id INT NOT NULL,
    department_id INT NOT NULL,
UNIQUE (employee_id, company_id, department_id),
FOREIGN KEY (employee_id)
    REFERENCES sandbox.employee (employee_id),
FOREIGN KEY (company_id)
    REFERENCES sandbox.company (company_id),
FOREIGN KEY (department_id)
    REFERENCES sandbox.department (department_id)
);