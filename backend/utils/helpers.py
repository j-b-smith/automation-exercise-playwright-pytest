import datetime
from typing import Dict, Any
from faker import Faker

# Initialize Faker
fake = Faker()

def generate_random_string(length: int = 10) -> str:
    """Generate random string."""
    return fake.pystr(min_chars=length, max_chars=length)

def generate_random_email() -> str:
    """Generate random email."""
    return fake.email()

def get_current_date() -> str:
    """Get current date in format DD-MM-YYYY."""
    return datetime.datetime.now().strftime("%d-%m-%Y")

def get_random_number(min_val: int, max_val: int) -> int:
    """Get random number between min and max."""
    return fake.random_int(min=min_val, max=max_val)

def generate_test_user() -> Dict[str, Any]:
    """Generate test user data with field names matching API response structure."""
    first_name = fake.first_name()
    last_name = fake.last_name()
    
    return {
        "name": f"{first_name} {last_name}",
        "email": f"{fake.email()}{str(fake.random_int(min=100, max=1000))}",
        "password": fake.password(length=12),
        "title": fake.random_element(elements=["Mr", "Mrs", "Miss"]),
        "birth_date": str(fake.random_int(min=1, max=28)),
        "birth_month": str(fake.random_int(min=1, max=12)),
        "birth_year": str(fake.random_int(min=1970, max=2000)),
        "firstname": first_name,
        "lastname": last_name,
        "company": fake.company(),
        "address1": fake.street_address(),
        "address2": fake.secondary_address(),
        "country": fake.country(),
        "state": fake.state(),
        "city": fake.city(),
        "zipcode": fake.zipcode(),
        "mobile_number": fake.phone_number()
    }

def generate_payment_details() -> Dict[str, Any]:
    """Generate payment details."""
    return {
        "name_on_card": fake.name(),
        "card_number": fake.credit_card_number(card_type=None),
        "cvc": fake.credit_card_security_code(),
        "expiry_month": str(fake.random_int(min=1, max=12)),
        "expiry_year": str(fake.random_int(min=datetime.datetime.now().year, max=datetime.datetime.now().year + 10))
    }