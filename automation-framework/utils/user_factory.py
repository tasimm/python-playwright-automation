from faker import Faker

fake = Faker()

def generate_user():
    return {
        "name": fake.name(),
        "email": fake.email(),
        "password": fake.password(length=10),
    }