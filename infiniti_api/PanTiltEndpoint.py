from __future__ import annotations
from typing import Tuple, Dict, TYPE_CHECKING

# Type Checking
if TYPE_CHECKING:
    from .RWYAPICaller import RWYAPICaller

class PanTiltEndpoint:
    """
    This class represents the Pan-Tilt endpoint of the Infiniti API.
    It provides methods to control the pan-tilt camera, get its status, and get its configuration.
    """

    def __init__(self, api_caller : RWYAPICaller) -> None:
        """
        Initializes a new instance of the PanTiltEndpoint class.

        Parameters:
        api_caller (RWYAPICaller): The RWYAPICaller instance to use for API calls.
        """
        self.api_caller = api_caller
        self.endpoint = 'api/devices/pantilt'

    def get_status(self) -> Dict:
        """
        Gets the status of the pan-tilt camera.

        Returns:
        Dict: A dictionary containing the status of the pan-tilt camera.
        """
        return self.api_caller.get(self.endpoint)
    
    def get_position(self) -> Tuple[float, float]:
        """
        Gets the current position of the pan-tilt camera.

        Returns:
        Tuple[float, float]: A tuple containing the pan and tilt angles of the camera.
        """
        data = self.api_caller.get(self.api_caller._build_path(self.endpoint, 'position'))
        return data['pan'], data['tilt']
    
    def set_position(self, pan: int, tilt: int) -> None:
        """
        Sets the position of the pan-tilt camera.

        Parameters:
        pan (int): The pan angle to set.
        tilt (int): The tilt angle to set.
        """
        data = {
            "pan": pan,
            "tilt": tilt
        }

        return self.api_caller.post(self.api_caller._build_path(self.endpoint, 'position'), payload=data)

    def relative_move(self, move_direction: str, speed: int = None, pan_speed : int = None, tilt_speed: int = None) -> Dict:
        """
        Moves the pan-tilt camera relative to its current position.

        Parameters:
        move_direction (str): The direction to move the camera in. Can be 'up', 'down', 'left', or 'right'.
        speed (int): The speed to move the camera at. If not provided, pan_speed and tilt_speed must be provided instead.
        pan_speed (int): The speed to move the camera's pan axis at.
        tilt_speed (int): The speed to move the camera's tilt axis at.

        Returns:
        Dict: A dictionary containing the response from the API.
        """
        query_params = {
            'command': 'move',
            'direction': move_direction
        }

        if speed is not None:
            query_params['speed'] = str(speed)
        else:
            query_params['panSpeed'] = str(pan_speed)
            query_params['tiltSpeed'] = str(tilt_speed)

        response = self.api_caller.get(self.api_caller._build_path_with_query(self.endpoint, None, query_params))
        return response
    
    def continuous_move(self, pan_speed: int, tilt_speed: int) -> Dict:
        """
        Moves the pan-tilt camera continuously at the given speeds.

        Parameters:
        pan_speed (int): The speed to move the camera's pan axis at.
        tilt_speed (int): The speed to move the camera's tilt axis at.

        Returns:
        Dict: A dictionary containing the response from the API.
        """
        pan_direction = 'right' if pan_speed > 0 else 'left' if pan_speed < 0 else None
        tilt_direction = 'up' if tilt_speed > 0 else 'down' if tilt_speed < 0 else None

        if pan_direction is None and tilt_direction is None:
            self.stop()
        else:
            move_direction = ''
            query_params = {
                'command': 'move'
            }

            if tilt_direction:
                move_direction += tilt_direction

            if pan_direction:
                move_direction += pan_direction
            
            query_params['direction'] = move_direction

            if pan_speed == 0 or tilt_speed == 0:
                query_params['speed'] = str(max(abs(pan_speed), abs(tilt_speed)))
            else:
                query_params['panSpeed'] = str(abs(pan_speed))
                query_params['tiltSpeed'] = str(abs(tilt_speed))

            response = self.api_caller.get(self.api_caller._build_path_with_query(self.endpoint, None, query_params))

            return response
    
    def stop(self) -> Dict:
        """
        Stops the pan-tilt camera.

        Returns:
        Dict: A dictionary containing the response from the API.
        """
        query_params = {'command': 'stop'}
        return self.api_caller.get(self.api_caller._build_path_with_query(self.endpoint, None, query_params))
    
    def home(self) -> Dict:
        """
        Homes the pan-tilt camera.

        Returns:
        Dict: A dictionary containing the response from the API.
        """
        query_params = {'command': 'home'}
        return self.api_caller.get(self.api_caller._build_path_with_query(self.endpoint, None, query_params))
    
    def get_config(self) -> Dict:
        """
        Gets the configuration of the pan-tilt camera.

        Returns:
        Dict: A dictionary containing the configuration of the pan-tilt camera.
        """
        url = self.api_caller._build_path(self.endpoint, 'config')
        return self.api_caller.get(url)
    
    def get_gyrostatus(self) -> Dict:
        """
        Gets the gyro status of the pan-tilt camera.

        Returns:
        Dict: A dictionary containing the gyro status of the pan-tilt camera.
        """
        return self.api_caller.get(self.api_caller._build_path(self.endpoint, 'gyro'))
    
    def set_gyrostatus(self, status) -> Dict:
        """
        Sets the gyro status of the pan-tilt camera.

        Parameters:
        status (bool): The status to set the gyro to.

        Returns:
        Dict: A dictionary containing the response from the API.
        """
        query_params = {'enable': status}
        return self.api_caller.get(self.api_caller._build_path_with_query(self.endpoint, 'gyro', query_params))
    
    def get_ethernet_config(self) -> Dict:
        """
        Gets the ethernet configuration of the pan-tilt camera.

        Returns:
        Dict: A dictionary containing the ethernet configuration of the pan-tilt camera.
        """
        return self.api_caller.get(self.api_caller._build_path(self.endpoint, 'ethernet'))