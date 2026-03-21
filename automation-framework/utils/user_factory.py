from faker import Faker

fake = Faker()

def generate_user():
    return {
        "name": fake.name(),
        "email": fake.unique.email(),
        "password": fake.password(length=10),

        "first_name": fake.first_name(),
        "last_name": fake.last_name(),

        "address": fake.street_address(),
        "country": "United States",  # keep stable for dropdown

        "state": fake.state(),
        "city": fake.city(),
        "zipcode": fake.zipcode(),

        "mobile_number": fake.msisdn()[:10],

        # dropdown-safe values (strings)
        "day": str(fake.random_int(min=1, max=28)),
        "month": str(fake.random_int(min=1, max=12)),
        "year": str(fake.random_int(min=1980, max=2000)),
    }