"""API methods for Automation Exercise."""
from typing import Dict, Any, Optional
import requests
from api.api_client import ApiClient
from api.api_endpoints import ApiEndpoints

class ApiMethods:
    """API methods class."""
    
    def __init__(self, api_client: ApiClient):
        """Initialize API methods.
        
        Args:
            api_client: API client instance
        """
        self.api_client = api_client
    
    def get_all_products(self) -> requests.Response:
        """Get all products list.
        
        Returns:
            Response from API
        """
        return self.api_client.get(ApiEndpoints.PRODUCTS_LIST)
    
    def get_all_brands(self) -> requests.Response:
        """Get all brands list.
        
        Returns:
            Response from API
        """
        return self.api_client.get(ApiEndpoints.BRANDS_LIST)
    
    def search_product(self, search_term: str) -> requests.Response:
        """Search for products.
        
        Args:
            search_term: Search term
            
        Returns:
            Response from API
        """
        return self.api_client.post(ApiEndpoints.SEARCH_PRODUCT, data={"search_product": search_term})
    
    def verify_login(self, email: str, password: str) -> requests.Response:
        """Verify login credentials.
        
        Args:
            email: Email address
            password: Password
            
        Returns:
            Response from API
        """
        return self.api_client.post(ApiEndpoints.VERIFY_LOGIN, data={"email": email, "password": password})
    
    def create_account(self, user_data: Dict[str, Any]) -> requests.Response:
        """Create user account.
        
        Args:
            user_data: User data
            
        Returns:
            Response from API
        """
        return self.api_client.post(ApiEndpoints.CREATE_ACCOUNT, data=user_data)
    
    def delete_account(self, email: str, password: str) -> requests.Response:
        """Delete user account.
        
        Args:
            email: Email address
            password: Password
            
        Returns:
            Response from API
        """
        return self.api_client.delete(ApiEndpoints.DELETE_ACCOUNT, data={"email": email, "password": password})
    
    def update_account(self, user_data: Dict[str, Any]) -> requests.Response:
        """Update user account.
        
        Args:
            user_data: User data
            
        Returns:
            Response from API
        """
        return self.api_client.put(ApiEndpoints.UPDATE_ACCOUNT, data=user_data)
    
    def get_user_detail(self, email: str) -> requests.Response:
        """Get user detail by email.
        
        Args:
            email: Email address
            
        Returns:
            Response from API
        """
        return self.api_client.get(ApiEndpoints.GET_USER_DETAIL, params={"email": email})
