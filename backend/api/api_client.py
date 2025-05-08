# api/api_client.py
import requests
import json
import logging
from typing import Dict, Any, Optional, Union
from utils.logger import api_logger

class ApiClient:
    """Base API client for making HTTP requests."""
    
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = requests.Session()
        self.logger = logging.getLogger(__name__)
        self._setup_logging()
    
    def _setup_logging(self):
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)
        self.logger.setLevel(logging.INFO)
    
    def _process_response(self, response: requests.Response) -> requests.Response:
        """Extract responseCode from the response if available."""
        try:
            data = response.json()
            if "responseCode" in data:
                response.response_code = data["responseCode"]
                self.logger.info(f"Response contains responseCode: {response.response_code}")
        except (ValueError, KeyError, AttributeError):
            # If cannot parse JSON or no responseCode, don't set response_code
            pass
        
        return response
    
    def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> requests.Response:
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        
        api_logger.log_request(
            method="GET",
            url=url,
            params=params
        )
        
        try:
            response = self.session.get(url, params=params)
            
            try:
                response_json = response.json()
                api_logger.log_response(
                    status_code=response.status_code,
                    url=url,
                    headers=dict(response.headers),
                    response_json=response_json
                )
            except ValueError:
                api_logger.log_response(
                    status_code=response.status_code,
                    url=url,
                    headers=dict(response.headers),
                    response_text=response.text
                )
            
            response = self._process_response(response)
            return response
        except Exception as e:
            api_logger.log_error(e, url)
            raise
    
    def post(self, endpoint: str, data: Optional[Dict[str, Any]] = None, json_data: Optional[Dict[str, Any]] = None) -> requests.Response:
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        
        api_logger.log_request(
            method="POST",
            url=url,
            data=data,
            json_data=json_data
        )
        
        try:
            response = self.session.post(url, data=data, json=json_data)
            
            try:
                response_json = response.json()
                api_logger.log_response(
                    status_code=response.status_code,
                    url=url,
                    headers=dict(response.headers),
                    response_json=response_json
                )
            except ValueError:
                api_logger.log_response(
                    status_code=response.status_code,
                    url=url,
                    headers=dict(response.headers),
                    response_text=response.text
                )
            
            response = self._process_response(response)
            return response
        except Exception as e:
            api_logger.log_error(e, url)
            raise
    
    def put(self, endpoint: str, data: Optional[Dict[str, Any]] = None, json_data: Optional[Dict[str, Any]] = None) -> requests.Response:
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        
        api_logger.log_request(
            method="PUT",
            url=url,
            data=data,
            json_data=json_data
        )
        
        try:
            response = self.session.put(url, data=data, json=json_data)
            
            try:
                response_json = response.json()
                api_logger.log_response(
                    status_code=response.status_code,
                    url=url,
                    headers=dict(response.headers),
                    response_json=response_json
                )
            except ValueError:
                api_logger.log_response(
                    status_code=response.status_code,
                    url=url,
                    headers=dict(response.headers),
                    response_text=response.text
                )
            
            response = self._process_response(response)
            return response
        except Exception as e:
            api_logger.log_error(e, url)
            raise
    
    def delete(self, endpoint: str, data: Optional[Dict[str, Any]] = None) -> requests.Response:
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        
        api_logger.log_request(
            method="DELETE",
            url=url,
            data=data
        )
        
        try:
            response = self.session.delete(url, data=data)
            
            try:
                response_json = response.json()
                api_logger.log_response(
                    status_code=response.status_code,
                    url=url,
                    headers=dict(response.headers),
                    response_json=response_json
                )
            except ValueError:
                api_logger.log_response(
                    status_code=response.status_code,
                    url=url,
                    headers=dict(response.headers),
                    response_text=response.text
                )
            
            response = self._process_response(response)
            return response
        except Exception as e:
            api_logger.log_error(e, url)
            raise