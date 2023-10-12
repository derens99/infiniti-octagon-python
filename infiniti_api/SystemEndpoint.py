from __future__ import annotations
from typing import Dict, TYPE_CHECKING

# Type Checking
if TYPE_CHECKING:
    from .RWYAPICaller import RWYAPICaller

class SystemEndpoint:
    """
    A class representing the system endpoint of the Infiniti API.

    Attributes:
    -----------
    api_caller : RWYAPICaller
        An instance of the RWYAPICaller class used to make API calls.
    endpoint : str
        The endpoint URL for the system API.
    """

    def __init__(self, api_caller: RWYAPICaller) -> None:
        """
        Initializes a new instance of the SystemEndpoint class.

        Parameters:
        -----------
        api_caller : RWYAPICaller
            An instance of the RWYAPICaller class used to make API calls.
        """
        self.api_caller = api_caller
        self.endpoint = '/api/system'
    
    def get_status(self) -> Dict:
        """
        Returns the status of the system.
        """
        return self.api_caller.get(self.endpoint)
    
    def get_versions(self) -> Dict:
        """
        Returns the versions of the system.
        """
        return self.api_caller.get(self.api_caller._build_path(self.endpoint, 'versions'))
    
    def get_info(self) -> Dict:
        """
        Returns the information of the system.
        """
        return self.api_caller.get(self.api_caller._build_path(self.endpoint, 'info'))
    
    def get_time(self) -> Dict:
        """
        Returns the current time of the system.
        """
        return self.api_caller.get(self.api_caller._build_path(self.endpoint, 'time'))
    
    def set_time(self, timestamp: int) -> Dict:
        """
        Sets the time of the system to the specified timestamp.

        Parameters:
        -----------
        timestamp : int
            The timestamp to set the system time to.
        """
        payload = {'timestamp': timestamp}
        return self.api_caller.post(self.api_caller._build_path(self.endpoint, 'time'), payload=payload)
    
    def get_ethernet(self) -> Dict:
        """
        Returns the ethernet information of the system.
        """
        return self.api_caller.get(self.api_caller._build_path(self.endpoint, 'ethernet'))
    
    def get_accounts(self) -> Dict:
        """
        Returns the accounts of the system.
        """
        return self.api_caller.get(self.api_caller._build_path(self.endpoint, 'accounts'))
    
    def get_account(self, account_name: str) -> Dict:
        """
        Returns the specified account of the system.

        Parameters:
        -----------
        account_name : str
            The name of the account to retrieve.
        """
        return self.api_caller.get(self.api_caller._build_path(self.endpoint, f'accounts/{account_name}'))
    
    def restart_hardware(self) -> Dict:
        """
        Restarts the hardware of the system.
        """
        query_params = {'command': 'hardwareRestart'}
        return self.api_caller.get(self.api_caller._build_path_with_query(self.endpoint, '', query_params))
    
    def restart_software(self) -> Dict:
        """
        Restarts the software of the system.
        """
        query_params = {'command': 'softwareRestart'}
        return self.api_caller.get(self.api_caller._build_path_with_query(self.endpoint, '', query_params))
    
    def get_presets(self) -> Dict:
        """
        Returns the presets of the system.
        """
        return self.api_caller.get(self.api_caller._build_path(self.endpoint, 'presets'))
    
    def get_preset(self, preset_id: int) -> Dict:
        """
        Returns the specified preset of the system.

        Parameters:
        -----------
        preset_id : int
            The ID of the preset to retrieve.
        """
        return self.api_caller.get(self.api_caller._build_path(self.endpoint, f'presets/{preset_id}'))
    
    def delete_preset(self, preset_id: int) -> Dict:
        """
        Deletes the specified preset of the system.

        Parameters:
        -----------
        preset_id : int
            The ID of the preset to delete.
        """
        query_params = {'action': 'clear'}
        return self.api_caller.get(self.api_caller._build_path_with_query(self.endpoint, f'presets/{preset_id}', query_params))
    
    def goto_preset(self, preset_id: int) -> Dict:
        """
        Moves the system to the specified preset.

        Parameters:
        -----------
        preset_id : int
            The ID of the preset to move to.
        """
        query_params = {'action': 'goto'}
        return self.api_caller.get(self.api_caller._build_path_with_query(self.endpoint, f'presets/{preset_id}', query_params))
    
    def stop_preset_move(self) -> Dict:
        """
        Stops the system from moving to a preset.
        """
        query_params = {'command': 'stop'}
        return self.api_caller.get(self.api_caller._build_path_with_query(self.endpoint, 'presets', query_params))
    
    def delete_all_presets(self) -> Dict:
        """
        Deletes all presets of the system.
        """
        query_params = {'command': 'clearAll'}
        return self.api_caller.get(self.api_caller._build_path_with_query(self.endpoint, 'presets', query_params))