'''
This script will load all the employees from the sample_data.csv file
and register them in the database using the API.
'''
import requests
import pandas


def register(employee: dict = {}):
    '''
    Register employees in the database using the API.

    Params
    ----------
        employee: dict with the employee data

    Returns
    ----------
        message str: The success message or error message.
    '''
    params = {
        'first_name': employee['first_name'],
        'last_name': employee['last_name'],
        'email': employee['email'],
        'phone1': employee['phone1'],
        'phone2': employee['phone2'],
        'company_name': employee['company_name'],
        'address': employee['address'],
        'city': employee['city'],
        'state': employee['state'],
        'zip': employee['zip'],
        'department': employee['department'],
    }
    try:
        # Make a post request to the API
        response = requests.post(
            'http://flask_app:5000/registry', params=params
        )
        if response.status_code == 200:
            print(
                'Successfully registered employee '
                '{first_name} {last_name}'.format(**employee)
            )
        else:
            print(
                'Could not register employee '
                '{first_name} {last_name}'.format(**employee)
            )
    except Exception as e:
        print('Failed request: {}'.format(e))


if __name__ == '__main__':
    # Read dataset as pandas dataframe
    dataframe = pandas.read_csv('dataset/sample_data.csv')

    # Convert dataframe to list of dicts
    data = dataframe.to_dict('records')

    # Loop through the list of dicts
    for employee in data:
        # Register the employee
        register(employee)
