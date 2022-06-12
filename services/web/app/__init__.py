from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object("app.config.Config")
db = SQLAlchemy(app)


class Register(db.Model):
    __tablename__ = "register"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)
    company_name = db.Column(db.String(128), nullable=False)
    address = db.Column(db.String(128), nullable=False)
    city = db.Column(db.String(128), nullable=False)
    state = db.Column(db.String(128), nullable=False)
    zip_code = db.Column(db.String(128), nullable=False)
    phone1 = db.Column(db.String(128), nullable=False)
    phone2 = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    department = db.Column(db.String(128), nullable=False)

    def __init__(self, first_name, last_name, company_name, address, city, state, zip_code, phone1, phone2, email, department):
        self.first_name = first_name
        self.last_name = last_name
        self.company_name = company_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone1 = phone1
        self.phone2 = phone2
        self.email = email
        self.department = department


@app.route("/")
def hello_world():
    return jsonify(hello="hello from flask")
