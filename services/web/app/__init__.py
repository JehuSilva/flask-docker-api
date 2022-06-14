'''
Database model definition
'''

import os

from flask import Flask, jsonify, request
from app.models import Employee, Company, Department, CompanyEmployee

app = Flask(__name__)


@ app.route("/")
def hello_world():
    return jsonify(hello="hello from flask")


@app.route("/registry", methods=["POST"])
def create_registry():
    '''
    This method creates one registry in the database
    '''
    # Instantiate the model
    employee = Employee()
    company = Company()
    department = Department()
    employee_company = CompanyEmployee()

    # Retrieve the data from the request
    try:
        first_name = request.args.get('first_name')
        last_name = request.args.get('last_name')
        email = request.args.get('email')
        phone1 = request.args.get('phone1')
        phone2 = request.args.get('phone2')
        company_name = request.args.get('company_name')
        address = request.args.get('address')
        city = request.args.get('city')
        state = request.args.get('state')
        zip_code = request.args.get('zip')
        department_name = request.args.get('department')
    except Exception as e:
        return jsonify({'message': 'Bad parameters', 'error': str(e)}), 400

    try:
        employee_id = employee.insert(
            first_name, last_name, email, phone1, phone2
        )
        company_id = company.insert(
            company_name, address, city, state, zip_code
        )
        department_id = department.insert(department_name)
        employee_company.insert(employee_id, company_id, department_id)

    except Exception as e:
        return jsonify({'message': f'Error creating registry', 'error': str(e)}), 500

    return jsonify({'message': 'Registry created successfully'}), 200
