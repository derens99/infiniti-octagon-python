import requests
from urllib.parse import urljoin
import logging

class RWYAPICaller:
    def __init__(self, base_url, auth=None):
        """
        Initialize API caller python object

        Args:
            base_url (str): The base URL of the API
            auth (tuple): Optional, a tuple containing the username and password for basic authentication
        """
        self.base_url = base_url
        self.session = requests.Session()
        if auth:
            self.session.auth = auth
        
    def _send_request(self, method, endpoint, payload=None, headers=None):
        """
        Helper method to send a request to the API

        Args:
            method (str): The HTTP method for the request (e.g., 'GET', 'POST', etc.)
            endpoint (str): The API endpoint (path)
            payload (dict): Optional, data to send in the request body (for POST, PUT, PATCH requests)
            headers (dict): Optional, headers to include in the request

        Returns:
            dict: The parsed JSON response, or None if the request failed
        """
        url = urljoin(self.base_url, endpoint)
        try:
            response = self.session.request(method, url, json=payload, headers=headers)
            response.raise_for_status()
            json_data = response.json()
            
            # Check if the response is a dictionary and contains 'data' key
            if isinstance(json_data, dict) and 'data' in json_data:
                return json_data['data']
            else:
                # Log an error or warning indicating unexpected JSON format
                logging.warning(f"Unexpected JSON format: {json_data}")
                return None
        except requests.exceptions.RequestException as e:
            print(e)
            logging.error(e)
            return None
    
    def get(self, endpoint, headers=None):
        """
        Send a GET request to the API

        Args:
            endpoint (str): The API endpoint (path)
            headers (dict): Optional, headers to include in the request

        Returns:
            dict: The parsed JSON response, or None if the request failed
        """
        return self._send_request('GET', endpoint, headers=headers)
    
    def post(self, endpoint, payload, headers=None):
        """
        Send a POST request to the API

        Args:
            endpoint (str): The API endpoint (path)
            payload (dict): The data to send in the request body
            headers (dict): Optional, headers to include in the request

        Returns:
            dict: The parsed JSON response, or None if the request failed
        """
        return self._send_request('POST', endpoint, payload, headers)
    
    def _build_path(self, endpoint, sub_path):
        if sub_path is None:
            return f"{self.base_url}/{endpoint}"
        return f"{self.base_url}/{endpoint}/{sub_path}"
    
    def _build_path_with_query(self, endpoint, sub_path, query_params):
        path = self._build_path(endpoint, sub_path)
        if query_params:
            query_string = "&".join([f"{key}={value}" for key, value in query_params.items()])
            path = f"{path}?{query_string}"
        print(path)
        return path

