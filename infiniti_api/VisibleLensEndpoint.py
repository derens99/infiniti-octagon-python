from __future__ import annotations
from typing import Tuple, Dict, TYPE_CHECKING

# Type Checking
if TYPE_CHECKING:
    from .RWYAPICaller import RWYAPICaller

class VisibleLensEndpoint:
    """
    A class representing the visible lens endpoint of the Infiniti API.

    Attributes:
    -----------
    api_caller : RWYAPICaller
        An instance of the RWYAPICaller class used to make API calls.
    endpoint : str
        The endpoint for the visible lens API.
    """
    
    def __init__(self, api_caller: RWYAPICaller) -> None:
        """
        Initializes a new instance of the VisibleLensEndpoint class.

        Parameters:
        -----------
        api_caller : RWYAPICaller
            An instance of the RWYAPICaller class used to make API calls.
        """
        self.api_caller = api_caller
        self.endpoint = "api/devices/visible"

    def get_visiblelens(self) -> Tuple[float, float]:
        """
        Gets the zoom and focus values of the visible lens.

        Returns:
        --------
        tuple
            A tuple containing zoom and focus values.
        """
        resp = self.api_caller.get(
            self.api_caller._build_path(self.endpoint, "position")
        )
        return resp["zoom"], resp["focus"]

    def set_zoom(self, zoom: int):
        """
        Sets the zoom value of the visible lens.

        Parameters:
        -----------
        zoom : int
            The zoom value to set.

        Returns:
        --------
        bool
            True if the API call was successful, False otherwise.
        """
        data = {"zoom": zoom}
        return self.api_caller.post(
            self.api_caller._build_path(self.endpoint, "position"), data
        ) is None
            

    def set_visiblelens(self, zoom: int, focus: int) -> bool:
        """
        Sets the zoom and focus values of the visible lens.

        Parameters:
        -----------
        zoom : int
            The zoom value to set.
        focus : int
            The focus value to set.

        Returns:
        --------
        bool
            True if the API call was successful, False otherwise.
        """
        data = {"zoom": zoom, "focus": focus}
        return self.api_caller.post(
            self.api_caller._build_path(self.endpoint, "position"), data
        ) is None

    def set_color(self, mode: str) -> bool:
        """
        Sets the color mode of the visible lens.

        Parameters:
        -----------
        mode : str
            The color mode to set. Must be one of "day", "night", or "autoColor".

        Returns:
        --------
        bool
            True if the API call was successful, False otherwise.

        Raises:
        -------
        ValueError
            If an invalid color mode is provided.
        """
        valid_modes = ["day", "night", "autoColor"]
        if mode not in valid_modes:
            raise ValueError("Invalid mode. Valid modes are: {}".format(valid_modes))
        query_params = {"command": mode}
        return self.api_caller.get(
            self.api_caller._build_path_with_query(self.endpoint, None, query_params)
        ) is None

    def run_backfocus(self) -> bool:
        """
        Runs the backfocus routine on the visible lens.

        Returns:
        --------
        dict
            The response from the API call.
        """
        query_params = {"command": "backfocus"}
        return self.api_caller.get(
            self.api_caller._build_path_with_query(self.endpoint, None, query_params)
        ) is None

    def set_digitalzoom(self, mode: str) -> bool:
        """
        Sets the digital zoom mode of the visible lens.

        Parameters:
        -----------
        mode : str
            The digital zoom mode to set.

        Returns:
        --------
        bool
            True if the API call was successful, False otherwise.
        """
        query_params = {"command": "digitialZoom", "mode": mode}
        return self.api_caller.get(
            self.api_caller._build_path_with_query(self.endpoint, None, query_params)
        ) is None

    def set_digital_stabilization(self, enable: bool) -> bool:
        """
        Sets the digital stabilization mode of the visible lens.

        Parameters:
        -----------
        enable : bool
            Whether to enable or disable digital stabilization.

        Returns:
        --------
        bool
            True if the API call was successful, False otherwise.
        """
        query_params = {"command": "stabilization", "enable": enable}
        return self.api_caller.get(
            self.api_caller._build_path_with_query(self.endpoint, None, query_params)
        ) is None

    def move_lens(self, zoom_move) -> bool:
        """
        Moves the visible lens in the specified direction.

        Parameters:
        -----------
        zoom_move : str
            The direction to move the lens. Must be one of "zoomTele", "zoomWide", "focusFar", or "focusNear".

        Returns:
        --------
        bool
            True if the API call was successful, False otherwise.

        Raises:
        -------
        ValueError
            If an invalid zoom move is provided.
        """
        valid_zooms = ["zoomTele", "zoomWide", "focusFar", "focusNear"]

        if zoom_move not in valid_zooms:
            raise ValueError(
                "Invalid zoom move. Valid zooms are: {}".format(valid_zooms)
            )
        query_params = {"command": zoom_move}
        return self.api_caller.get(
            self.api_caller._build_path_with_query(self.endpoint, None, query_params)
        ) is None

    def stop_lens(self) -> bool:
        """
        Stops the movement of the visible lens.

        Returns:
        --------
        bool
            True if the API call was successful, False otherwise.
        """
        query_params = {"command": "stop"}
        return self.api_caller.get(
            self.api_caller._build_path_with_query(self.endpoint, None, query_params)
        ) is None

    def set_fogfilter(self, state: bool) -> bool:
        """
        Sets the fog filter state of the visible lens.

        Parameters:
        -----------
        state : bool
            Whether to enable or disable the fog filter.

        Returns:
        --------
        bool
            True if the API call was successful, False otherwise.
        """
        query_params = {"command": "fogFilter", "state": state}
        return self.api_caller.get(
            self.api_caller._build_path_with_query(self.endpoint, None, query_params)
        ) is None

    def set_autofocus_mode(self, enable: bool) -> bool: 
        """
        Sets the autofocus mode of the visible lens.

        Parameters:
        -----------
        enable : bool
            Whether to enable or disable autofocus.

        Returns:
        --------
        bool
            True if the API call was successful, False otherwise.
        """
        query_params = {"command": "zoomTriggerAutofocus", "enable": enable}
        return self.api_caller.get(
            self.api_caller._build_path_with_query(self.endpoint, None, query_params)
        ) is None

    def autofocus(self) -> bool:
        """
        Runs the autofocus routine on the visible lens.

        Returns:
        --------
        bool
            True if the API call was successful, False otherwise.
        """
        query_params = {"command": "autofocus"}
        return self.api_caller.get(
            self.api_caller._build_path_with_query(self.endpoint, None, query_params)
        ) is None

    def set_heatwave_intensity(self, mode) -> bool:
        """
        Sets the heatwave intensity mode of the visible lens.

        Parameters:
        -----------
        mode : str
            The heatwave intensity mode to set. Must be one of "Low", "Medium", or "High".

        Returns:
        --------
        bool
            True if the API call was successful, False otherwise.

        Raises:
        -------
        ValueError
            If an invalid heatwave intensity mode is provided.
        """
        valid_modes = ["Low", "Medium", "High"]
        if mode not in valid_modes:
            raise ValueError("Invalid mode. Valid modes are: {}".format(valid_modes))
        query_params = {"command": "heatwaveIntensityMode", "mode": mode}
        return self.api_caller.get(
            self.api_caller._build_path_with_query(self.endpoint, None, query_params)
        ) is None

    def get_config(self) -> Dict:
        """
        Gets the current configuration of the visible lens.

        Returns:
        --------
        dict
            The current configuration of the visible lens.
        """
        url = self.api_caller._build_path(self.endpoint, "config")
        data = self.api_caller.get(url)
        return data

    def set_config(self):
        """
        Sets the configuration of the visible lens to default values.

        Returns:
        --------
        bool
            True if the API call was successful, False otherwise.
        """
        data = {
            "2dnr": 55,
            "3dnr": 55,
            "autofocusMode": "ZOOM_TRIGGER",
            "colorMode": "AUTO",
            "focusMode": "DISABLED",
            "focusSpeed": 4,
            "fogFilter": False,
            "gamma": 8,
            "heatWaveMode": "OFF",
            "processingMode": "WDR",
            "sharpening": 5,
            "stabilizing": True,
            "zoomSpeed": 1,
        }
        
        return self.api_caller.post(self.api_caller._build_path(self.endpoint, "config"), data)

    def zoomTele(self):
        """
        Moves the visible lens to the telephoto position.

        Returns:
        --------
        bool
            True if the API call was successful, False otherwise.
        """
        return self.move_lens("zoomTele")

    def zoomWide(self):
        """
        Moves the visible lens to the wide angle position.

        Returns:
        --------
        bool
            True if the API call was successful, False otherwise.
        """
        return self.move_lens("zoomWide")

    def focusFar(self):
        """
        Moves the visible lens to the far focus position.

        Returns:
        --------
        bool
            True if the API call was successful, False otherwise.
        """
        return self.move_lens("focusFar")

    def focusNear(self):
        """
        Moves the visible lens to the near focus position.

        Returns:
        --------
        bool
            True if the API call was successful, False otherwise.
        """
        return self.move_lens("focusNear")
    def continuous_zoom(self, speed: int):
        if speed > 0:
            return self.zoomTele()
        elif speed < 0:
            return self.zoomWide()
        else:
            return self.stop_lens()
