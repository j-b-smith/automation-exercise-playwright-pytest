"""Test data for backend API tests."""
import datetime
from faker import Faker
from utils.helpers import generate_test_user, generate_payment_details

# Initialize Faker
fake = Faker()

class TestData:
    """Test data class."""
    
    # Fixed user data for authentication
    FIXED_USER = {
        "email": "test@example.com",
        "password": "password123",
        "name": "Test User"
    }
    
    # Dynamic user data that will be regenerated when imported
    TEST_USER = generate_test_user()
    
    # Invalid user data
    INVALID_USER = {
        "email": "invalid@example.com",
        "password": "invalidpassword"
    }
    
    # Product search data
    PRODUCT_SEARCH = {
        "valid_product": fake.random_element(elements=["top", "dress", "tshirt", "jeans"]),
        "invalid_product": f"invalid{fake.pystr(min_chars=8, max_chars=12)}"
    }
    
    # Payment details
    PAYMENT_DETAILS = generate_payment_details()
    
    @staticmethod
    def get_dynamic_user():
        """Generate a fresh user for tests requiring unique users.
        
        Returns:
            Newly generated user data
        """
        return generate_test_user()
