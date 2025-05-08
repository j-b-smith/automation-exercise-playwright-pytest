# tests/users/test_user_api.py
import pytest
from http import HTTPStatus
from data.test_data import TestData
from api.api_endpoints import ApiEndpoints

class TestUsers:
    """Test operations for user accounts."""
    
    def test_create_user(self, api_methods):
        """
        API 11: POST To Create/Register User Account
        
        API URL: https://automationexercise.com/api/createAccount
        Request Method: POST
        Request Parameters: name, email, password, title, birth_date, birth_month, birth_year, firstname, lastname, company, address1, address2, country, zipcode, state, city, mobile_number
        Response Code: 201
        Response Message: User created!
        """
        user_data = TestData.get_dynamic_user()
        
        create_response = api_methods.create_account(user_data)
        
        assert create_response.status_code == HTTPStatus.OK, \
            f"Expected HTTP status code 200 OK, got {create_response.status_code}. Response: {create_response.text}"
        
        assert create_response.response_code == HTTPStatus.CREATED, \
            f"Expected response code 201 CREATED, got {create_response.response_code}. Response: {create_response.json()}"
        
        assert create_response.json()["message"] == "User created!", \
            f"Expected message 'User created!', got '{create_response.json().get('message', 'No message')}'."
    
    def test_read_user(self, api_methods):
        """
        API 14: GET user account detail by email
        
        API URL: https://automationexercise.com/api/getUserDetailByEmail
        Request Method: GET
        Request Parameters: email
        Response Code: 200
        Response JSON: User Detail
        """
        user_data = TestData.get_dynamic_user()
        create_response = api_methods.create_account(user_data)
        
        assert create_response.status_code == HTTPStatus.OK, \
            f"Setup failed: Could not create test user. Status: {create_response.status_code}, Response: {create_response.text}"
        
        get_response = api_methods.get_user_detail(user_data["email"])
        
        assert get_response.status_code == HTTPStatus.OK, \
            f"Expected HTTP status code 200 OK, got {get_response.status_code}. Response: {get_response.text}"
        
        assert get_response.response_code == HTTPStatus.OK, \
            f"Expected response code 200 OK, got {get_response.response_code}. Response: {get_response.json()}"
        
        get_data = get_response.json()
        assert "user" in get_data, \
            f"Expected 'user' field in response, got keys: {list(get_data.keys())}"
        
        retrieved_user = get_data["user"]
        for field, value in user_data.items():
            if field != "password" and field in retrieved_user:
                assert str(retrieved_user[field]) == str(value), \
                    f"Field '{field}' mismatch: expected '{value}', got '{retrieved_user[field]}'"
    
    def test_update_user(self, api_methods):
        """
        API 13: PUT METHOD To Update User Account
        
        API URL: https://automationexercise.com/api/updateAccount
        Request Method: PUT
        Request Parameters: name, email, password, title, birth_date, birth_month, birth_year, firstname, lastname, company, address1, address2, country, zipcode, state, city, mobile_number
        Response Code: 200
        Response Message: User updated!
        """
        original_user = TestData.get_dynamic_user()
        create_response = api_methods.create_account(original_user)
        
        assert create_response.status_code == HTTPStatus.OK, \
            f"Setup failed: Could not create test user. Status: {create_response.status_code}, Response: {create_response.text}"
        
        updated_user = TestData.get_dynamic_user()
        updated_user["email"] = original_user["email"]
        updated_user["password"] = original_user["password"]
        
        update_response = api_methods.update_account(updated_user)
        
        assert update_response.status_code == HTTPStatus.OK, \
            f"Expected HTTP status code 200 OK, got {update_response.status_code}. Response: {update_response.text}"
        
        assert update_response.response_code == HTTPStatus.OK, \
            f"Expected response code 200 OK, got {update_response.response_code}. Response: {update_response.json()}"
        
        assert update_response.json()["message"] == "User updated!", \
            f"Expected message 'User updated!', got '{update_response.json().get('message', 'No message')}'."
        
        get_response = api_methods.get_user_detail(original_user["email"])
        
        assert get_response.status_code == HTTPStatus.OK, \
            f"Expected HTTP status code 200 OK, got {get_response.status_code}. Response: {get_response.text}"
        
        retrieved_user = get_response.json()["user"]
        for field, value in updated_user.items():
            if field != "password" and field in retrieved_user:
                assert str(retrieved_user[field]) == str(value), \
                    f"Field '{field}' mismatch after update: expected '{value}', got '{retrieved_user[field]}'"
    
    def test_delete_user(self, api_methods):
        """
        API 12: DELETE METHOD To Delete User Account
        
        API URL: https://automationexercise.com/api/deleteAccount
        Request Method: DELETE
        Request Parameters: email, password
        Response Code: 200
        Response Message: Account deleted!
        """
        user_data = TestData.get_dynamic_user()
        create_response = api_methods.create_account(user_data)
        
        assert create_response.status_code == HTTPStatus.OK, \
            f"Setup failed: Could not create test user. Status: {create_response.status_code}, Response: {create_response.text}"
        
        delete_response = api_methods.delete_account(user_data["email"], user_data["password"])
        
        assert delete_response.status_code == HTTPStatus.OK, \
            f"Expected HTTP status code 200 OK, got {delete_response.status_code}. Response: {delete_response.text}"
        
        assert delete_response.response_code == HTTPStatus.OK, \
            f"Expected response code 200 OK, got {delete_response.response_code}. Response: {delete_response.json()}"
        
        assert delete_response.json()["message"] == "Account deleted!", \
            f"Expected message 'Account deleted!', got '{delete_response.json().get('message', 'No message')}'."
        
        get_response = api_methods.get_user_detail(user_data["email"])
        
        assert get_response.response_code == HTTPStatus.NOT_FOUND, \
            f"Expected response code 404 NOT_FOUND, got {get_response.response_code}. Response: {get_response.json()}"
    
    def test_create_user_with_existing_email(self, api_methods):
        """Test creating a user with an email that already exists."""
        user_data = TestData.get_dynamic_user()
        create_response = api_methods.create_account(user_data)
        
        assert create_response.status_code == HTTPStatus.OK, \
            f"Setup failed: Could not create test user. Status: {create_response.status_code}, Response: {create_response.text}"
        
        second_user = TestData.get_dynamic_user()
        second_user["email"] = user_data["email"]
        
        duplicate_response = api_methods.create_account(second_user)
        
        assert duplicate_response.status_code == HTTPStatus.OK, \
            f"Expected HTTP status code 200 OK, got {duplicate_response.status_code}. Response: {duplicate_response.text}"
        
        assert duplicate_response.response_code in [HTTPStatus.BAD_REQUEST, HTTPStatus.CONFLICT], \
            f"Expected response code 400 or 409, got {duplicate_response.response_code}. Response: {duplicate_response.json()}"
        
        error_message = duplicate_response.json().get("message", "")
        assert "exist" in error_message.lower(), \
            f"Expected error message about existing email, got: '{error_message}'"
    
    def test_verify_login_with_valid_credentials(self, api_methods):
        """
        API 7: POST To Verify Login with valid details
        
        API URL: https://automationexercise.com/api/verifyLogin
        Request Method: POST
        Request Parameters: email, password
        Response Code: 200
        Response Message: User exists!
        """
        user_data = TestData.get_dynamic_user()
        create_response = api_methods.create_account(user_data)
        
        assert create_response.status_code == HTTPStatus.OK, \
            f"Setup failed: Could not create test user. Status: {create_response.status_code}, Response: {create_response.text}"
        
        login_response = api_methods.verify_login(user_data["email"], user_data["password"])
        
        assert login_response.status_code == HTTPStatus.OK, \
            f"Expected HTTP status code 200 OK, got {login_response.status_code}. Response: {login_response.text}"
        
        assert login_response.response_code == HTTPStatus.OK, \
            f"Expected response code 200 OK, got {login_response.response_code}. Response: {login_response.json()}"
        
        assert login_response.json()["message"] == "User exists!", \
            f"Expected message 'User exists!', got '{login_response.json().get('message', 'No message')}'."
    
    def test_verify_login_with_invalid_credentials(self, api_methods):
        """
        API 10: POST To Verify Login with invalid details
        
        API URL: https://automationexercise.com/api/verifyLogin
        Request Method: POST
        Request Parameters: email, password (invalid values)
        Response Code: 404
        Response Message: User not found!
        """
        email = f"nonexistent_{TestData.get_dynamic_user()['email']}"
        password = "invalidPassword123"
        
        login_response = api_methods.verify_login(email, password)
        
        assert login_response.status_code == HTTPStatus.OK, \
            f"Expected HTTP status code 200 OK, got {login_response.status_code}. Response: {login_response.text}"
        
        assert login_response.response_code == HTTPStatus.NOT_FOUND, \
            f"Expected response code 404 NOT_FOUND, got {login_response.response_code}. Response: {login_response.json()}"
        
        assert login_response.json()["message"] == "User not found!", \
            f"Expected message 'User not found!', got '{login_response.json().get('message', 'No message')}'."
    
    def test_verify_login_without_email_parameter(self, api_client):
        """
        API 8: POST To Verify Login without email parameter
        
        API URL: https://automationexercise.com/api/verifyLogin
        Request Method: POST
        Request Parameter: password
        Response Code: 400
        Response Message: Bad request, email or password parameter is missing in POST request.
        """
        response = api_client.post(ApiEndpoints.VERIFY_LOGIN, data={"password": "password123"})
        
        assert response.status_code == HTTPStatus.OK, \
            f"Expected status code 200, but got {response.status_code}"
        
        assert response.response_code == HTTPStatus.BAD_REQUEST, \
            f"Expected response code 400, but got {response.response_code}"
        
        expected_msg = "Bad request, email or password parameter is missing in POST request"
        assert expected_msg in response.json().get("message", ""), \
            f"Expected error message '{expected_msg}', but got '{response.json()}'"
    
    def test_delete_method_on_verify_login(self, api_client):
        """
        API 9: DELETE To Verify Login
        
        API URL: https://automationexercise.com/api/verifyLogin
        Request Method: DELETE
        Response Code: 405
        Response Message: This request method is not supported.
        """
        response = api_client.delete(ApiEndpoints.VERIFY_LOGIN)
        
        assert response.status_code == HTTPStatus.OK, \
            f"Expected status code 200 OK, but got {response.status_code}"
        
        response_data = response.json()
        
        assert response_data["responseCode"] == HTTPStatus.METHOD_NOT_ALLOWED, \
            f"Expected response code 405, but got {response_data['responseCode']}"
        
        assert response_data["message"] == "This request method is not supported.", \
            f"Expected error message 'This request method is not supported', but got '{response_data['message']}"
    
    def test_create_user_without_required_parameters(self, api_client):
        """Test creating user without required parameters."""
        incomplete_data = {
            "name": "Test User",
        }
        
        response = api_client.post(ApiEndpoints.CREATE_ACCOUNT, data=incomplete_data)
        
        assert response.status_code == HTTPStatus.OK, \
            f"Expected status code 200, but got {response.status_code}"
        
        assert response.response_code == HTTPStatus.BAD_REQUEST, \
            f"Expected response code 400, but got {response.response_code}"
        
        assert "missing" in response.json().get("message", "").lower(), \
            f"Expected error message about missing parameters, got: '{response.json()}'"
    
    def test_update_user_without_required_parameters(self, api_client):
        """Test updating user without required parameters."""
        incomplete_data = {
            "name": "Updated User",
        }
        
        response = api_client.put(ApiEndpoints.UPDATE_ACCOUNT, data=incomplete_data)
        
        assert response.status_code == HTTPStatus.OK, \
            f"Expected status code 200, but got {response.status_code}"
        
        assert response.response_code == HTTPStatus.BAD_REQUEST, \
            f"Expected response code 400, but got {response.response_code}"
        
        assert "missing" in response.json().get("message", "").lower() or "not found" in response.json().get("message", "").lower(), \
            f"Expected error message about missing parameters or user not found, got: '{response.json()}'"
    
    def test_delete_user_without_required_parameters(self, api_client):
        """Test deleting user without required parameters."""
        incomplete_data = {
            "email": "test@example.com",
        }
        
        response = api_client.delete(ApiEndpoints.DELETE_ACCOUNT, data=incomplete_data)
        
        assert response.status_code == HTTPStatus.OK, \
            f"Expected status code 200, but got {response.status_code}"
        
        assert response.response_code == HTTPStatus.BAD_REQUEST, \
            f"Expected response code 400, but got {response.response_code}"
        
        assert "missing" in response.json().get("message", "").lower() or "password incorrect" in response.json().get("message", "").lower(), \
            f"Expected error message about missing parameters or password incorrect, got: '{response.json()}'"
    
    def test_get_user_without_email_parameter(self, api_client):
        """Test getting user details without email parameter."""
        response = api_client.get(ApiEndpoints.GET_USER_DETAIL)
        
        assert response.status_code == HTTPStatus.OK, \
            f"Expected status code 200, but got {response.status_code}"
        
        assert response.response_code == HTTPStatus.BAD_REQUEST, \
            f"Expected response code 400, but got {response.response_code}"
        
        assert "missing" in response.json().get("message", "").lower(), \
            f"Expected error message about missing email parameter, got: '{response.json()}'"
    
    def test_create_user_with_invalid_email_format(self, api_methods):
        """Test user creation with invalid email format."""
        user_data = TestData.get_dynamic_user()
        user_data["email"] = "invalid_email_format"
        
        create_response = api_methods.create_account(user_data)
        
        assert create_response.status_code == HTTPStatus.OK, \
            f"Expected HTTP status code 200 OK, got {create_response.status_code}. Response: {create_response.text}"
        
        assert create_response.response_code == HTTPStatus.BAD_REQUEST, \
            f"Expected response code 400 BAD_REQUEST for invalid email, got {create_response.response_code}. Response: {create_response.json()}"
        
        error_message = create_response.json().get("message", "").lower()
        assert "invalid" in error_message or "email" in error_message, \
            f"Expected error message about invalid email, got: '{create_response.json()}'"
    
    def test_update_nonexistent_user(self, api_methods):
        """Test updating a user that doesn't exist."""
        nonexistent_user = TestData.get_dynamic_user()
        nonexistent_user["email"] = f"nonexistent_{TestData.get_dynamic_user()['email']}"
        
        update_response = api_methods.update_account(nonexistent_user)
        
        assert update_response.status_code == HTTPStatus.OK, \
            f"Expected HTTP status code 200 OK, got {update_response.status_code}. Response: {update_response.text}"
        
        assert update_response.response_code == HTTPStatus.NOT_FOUND, \
            f"Expected response code 404 NOT_FOUND, got {update_response.response_code}. Response: {update_response.json()}"
        
        error_message = update_response.json().get("message", "").lower()
        assert "not found" in error_message or "doesn't exist" in error_message, \
            f"Expected error message about user not found, got: '{update_response.json()}'"
    
    def test_delete_nonexistent_user(self, api_methods):
        """Test deleting a user that doesn't exist."""
        nonexistent_email = f"nonexistent_{TestData.get_dynamic_user()['email']}"
        
        delete_response = api_methods.delete_account(nonexistent_email, "password123")
        
        assert delete_response.status_code == HTTPStatus.OK, \
            f"Expected HTTP status code 200 OK, got {delete_response.status_code}. Response: {delete_response.text}"
        
        assert delete_response.response_code == HTTPStatus.NOT_FOUND, \
            f"Expected response code 404 NOT_FOUND, got {delete_response.response_code}. Response: {delete_response.json()}"
        
        error_message = delete_response.json().get("message", "").lower()
        assert "not found" in error_message or "doesn't exist" in error_message, \
            f"Expected error message about user not found, got: '{delete_response.json()}'"