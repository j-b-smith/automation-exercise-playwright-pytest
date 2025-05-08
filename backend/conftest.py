import os
import pytest
from dotenv import load_dotenv
from api.api_client import ApiClient
from api.api_methods import ApiMethods

# Load environment variables from .env file
load_dotenv()

@pytest.fixture(scope="session")
def api_base_url():
    """Return API base URL."""
    return os.getenv("API_BASE_URL", "https://www.automationexercise.com/api")

@pytest.fixture(scope="session")
def api_client(api_base_url):
    """Return API client instance."""
    return ApiClient(base_url=api_base_url)

@pytest.fixture(scope="session")
def api_methods(api_client):
    """Return API methods instance."""
    return ApiMethods(api_client=api_client)