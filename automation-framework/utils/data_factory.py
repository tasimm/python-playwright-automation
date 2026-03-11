import uuid

def generate_unique_email():
    return f"user_{uuid.uuid4()}@test.com"