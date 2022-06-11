from flask.cli import FlaskGroup

from app import app, db, Register

cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("seed_db")
def seed_db():
    db.session.add(Register(
        name="John Doe",
        address="123 Main St",
        city="Anytown",
        state="CA",
        zip_code="90210",
        phone1="555-555-1234",
        phone2="555-555-1235",
        email="john_doe@email.com",
        department="Sales"
    ))
    db.session.commit()


if __name__ == "__main__":
    cli()
