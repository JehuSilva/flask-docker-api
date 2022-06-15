'''
Database model definition
'''
from flask import Flask, jsonify, request
from app.models import Employee, Company, Department, CompanyEmployee

app = Flask(__name__)


@ app.route("/")
def hello_world():
    return jsonify(message="Welcome to the Register API. Xal Digital"), 200


@app.route("/registry/list", methods=["GET"])
def list_registry():
    '''
    List all employees with details
    '''
    employee = Employee()
    employees_details = employee.get_employees_details()
    employees = [{
        "employee_id": employee_detail[0],
        "first_name": employee_detail[1],
        "last_name": employee_detail[2],
        "email": employee_detail[3],
        "phone1": employee_detail[4],
        "phone2": employee_detail[5],
        "company_id": employee_detail[6],
        "company_name": employee_detail[7],
        "address": employee_detail[8],
        "city": employee_detail[9],
        "state": employee_detail[10],
        "zip": employee_detail[11],
        "department_id": employee_detail[12],
        "department": employee_detail[13]
    } for employee_detail in employees_details]
    return jsonify(employees=employees), 200


@app.route("/registry", methods=["POST"])
def create_registry():
    '''
    This method creates one registry in the database
    '''
    # Instantiate the model tables
    employee = Employee()
    company = Company()
    department = Department()
    employee_company = CompanyEmployee()

    # Retrieve the data from the request
    try:
        first_name = request.args.get('first_name', None)
        last_name = request.args.get('last_name', None)
        email = request.args.get('email', None)
        phone1 = request.args.get('phone1', None)
        phone2 = request.args.get('phone2', None)
        company_name = request.args.get('company_name', None)
        address = request.args.get('address', None)
        city = request.args.get('city', None)
        state = request.args.get('state', None)
        zip_code = request.args.get('zip', None)
        department_name = request.args.get('department', None)
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
        return jsonify({'message': 'Error creating registry', 'error': str(e)}), 500

    return jsonify({'message': 'Registry created successfully'}), 200
