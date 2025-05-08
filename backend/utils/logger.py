import os
import json
import logging
import datetime
from typing import Dict, Any, Optional, Union

class ApiLogger:
    """API Logger for requests and responses."""
    
    def __init__(self, log_dir: str = "logs", log_level: int = logging.INFO):
        self.log_dir = log_dir
        self.log_level = log_level
        self.logger = logging.getLogger("api_logger")
        self.logger.setLevel(log_level)
        
        os.makedirs(log_dir, exist_ok=True)
        
        requests_log_file = os.path.join(log_dir, f"api_requests_{datetime.datetime.now().strftime('%Y%m%d')}.log")
        self.request_handler = logging.FileHandler(requests_log_file)
        self.request_handler.setLevel(log_level)
        
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.request_handler.setFormatter(formatter)
        
        self.logger.addHandler(self.request_handler)
        
        console_handler = logging.StreamHandler()
        console_handler.setLevel(log_level)
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)
    
    def log_request(self, method: str, url: str, headers: Optional[Dict[str, str]] = None, 
                   params: Optional[Dict[str, Any]] = None, data: Optional[Dict[str, Any]] = None,
                   json_data: Optional[Dict[str, Any]] = None) -> None:
        request_info = {
            "method": method,
            "url": url,
            "headers": headers,
            "params": params,
            "data": data,
            "json": json_data
        }
        
        request_info = {k: v for k, v in request_info.items() if v is not None}
        
        try:
            request_str = json.dumps(request_info, indent=2, ensure_ascii=False)
            self.logger.info(f"API Request:\n{request_str}")
        except Exception as e:
            self.logger.error(f"Error logging request: {e}")
            self.logger.info(f"API Request: {request_info}")
    
    def log_response(self, status_code: int, url: str, headers: Optional[Dict[str, str]] = None, 
                    response_text: Optional[str] = None,
                    response_json: Optional[Dict[str, Any]] = None) -> None:
        response_info = {
            "url": url,
            "status_code": status_code,
            "headers": headers
        }
        
        if response_json is not None:
            response_info["json"] = response_json
        elif response_text is not None:
            response_info["text"] = response_text
        
        try:
            response_str = json.dumps(response_info, indent=2, ensure_ascii=False)
            self.logger.info(f"API Response:\n{response_str}")
        except Exception as e:
            self.logger.error(f"Error logging response: {e}")
            self.logger.info(f"API Response: {response_info}")
    
    def log_error(self, error: Exception, url: Optional[str] = None) -> None:
        error_info = {
            "url": url,
            "error": str(error),
            "error_type": type(error).__name__
        }
        
        try:
            error_str = json.dumps(error_info, indent=2, ensure_ascii=False)
            self.logger.error(f"API Error:\n{error_str}")
        except Exception as e:
            self.logger.error(f"Error logging error: {e}")
            self.logger.error(f"API Error: {error_info}")

# Create a singleton instance
api_logger = ApiLogger()