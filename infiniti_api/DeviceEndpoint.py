from __future__ import annotations
from typing import Dict, TYPE_CHECKING

# Type Checking
if TYPE_CHECKING:
    from .RWYAPICaller import RWYAPICaller

class DeviceEndpoint:
    """
    A class representing the device endpoint of the Infiniti API.

    Attributes:
    -----------
    api_caller : RWYAPICaller
        An instance of the RWYAPICaller class used to make API calls.
    endpoint : str
        The endpoint for the device API.
    """

    def __init__(self, api_caller: RWYAPICaller) -> None:
        """
        Initializes a new instance of the DeviceEndpoint class.

        Parameters:
        -----------
        api_caller : RWYAPICaller
            An instance of the RWYAPICaller class used to make API calls.
        """
        self.api_caller = api_caller
        self.endpoint = 'api/devices'

    def get_devices(self) -> Dict:
        """
        Gets a list of all devices.

        Returns:
        --------
        dict
            A dictionary containing information about all devices.
        """
        return self.api_caller.get(self.endpoint)
    
    def get_device_state(self, device_name: str) -> Dict:
        """
        Gets the state of a specific device.

        Parameters:
        -----------
        device_name : str
            The name of the device to get the state of.

        Returns:
        --------
        dict
            A dictionary containing information about the device's state.
        """
        return self.api_caller.get(self.api_caller._build_path(self.endpoint, device_name))
    
    def reinitialize_device(self, device_name: str) -> Dict:
        """
        Reinitializes a specific device.

        Parameters:
        -----------
        device_name : str
            The name of the device to reinitialize.

        Returns:
        --------
        dict
            A dictionary containing information about the reinitialized device.
        """
        query_params = {'command': 'initialize'}
        return self.api_caller.get(self.api_caller._build_path_with_query(self.endpoint, device_name, query_params))
    
    