import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """Configuration settings for backend tests."""
    
    # Base URLs
    BASE_URL = os.getenv("BASE_URL", "https://www.automationexercise.com")
    API_BASE_URL = os.getenv("API_BASE_URL", "https://www.automationexercise.com/api")
    
    # Timeouts
    DEFAULT_TIMEOUT = int(os.getenv("DEFAULT_TIMEOUT", 30))
    
    # API endpoints
    API_ENDPOINTS = {
        "products_list": "productsList",
        "brands_list": "brandsList",
        "search_product": "searchProduct",
        "verify_login": "verifyLogin",
        "create_account": "createAccount",
        "delete_account": "deleteAccount",
        "update_account": "updateAccount",
        "get_user_detail": "getUserDetailByEmail"
    }
