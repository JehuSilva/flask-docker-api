# Register API Reference

In this section, we will describe the API endpoints and how to use them.

## Current available endpoints 
- [/registry/](#registry): Register a new employee
- [/registry/list](#registry-list): Get all registred employees

## Register an employee <a name = "registry"></a>
```http
POST /registry
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `first_name` | `string` | **Required**. First of the employee |
| `last_name` | `string` | **Required**. Last of the employee |
| `company_name` | `string` | **Required**. Company of the employee |
| `address` | `string` | **Optional**. Company address |
| `city` | `string` | **Optional**. Company city |
| `state` | `string` | **Optional**. Company state |
| `email` | `string` | **Required**. Employee email |
| `phone1` | `string` | **Required**. Employee phone1 |
| `phone2` | `string` | **Optional**. Employee phone2 |
| `zip` | `string` | **Optional**. Company zip code |
| `department` | `string` | **Required**. Departament of the employee |

Bash example:
```bash
curl --location --request POST 'http://localhost:5000/registry?first_name=Jehu&last_name=Silva&email=ijehusa@gmail.com&phone1=9512465454&phone2=5545465156&company_name=Coca-Cola&address=Eje Central 654, Coyoacan&city=Ciudad de Mexico&state=Ciudad de Mexico&zip=56424&department=Marketing'
```

Returns:
```json
{
    "message": "Registry created successfully"
}
```


## Get all registred employees <a name = "registry-list"></a>

```http
GET /registry/list
```

It doesnt't have any parameter so far.

Bash example:
```bash
curl --location --request GET 'http://localhost:5000/registry/list'
```
Returns:
```json
{
    "employees": [
        {
            "address": "6649 N Blue Gum St",
            "city": "New Orleans",
            "company_id": 1,
            "company_name": "Benton, John B Jr",
            "department": "Sales",
            "department_id": 1,
            "email": "jbutt@gmail.com",
            "employee_id": 1,
            "first_name": "James",
            "last_name": "Butt",
            "phone1": "504-621-8927",
            "phone2": "504-845-1427",
            "state": "LA",
            "zip": "70116"
        },
        ...
    ]
}
```

## TODO

Include the documentation for the API endpoints for DELETE, PUT AND PATCH.


