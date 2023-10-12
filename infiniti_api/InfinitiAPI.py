import os
import dotenv
dotenv.load_dotenv()

from typing import Tuple

from .RWYAPICaller import RWYAPICaller
from .SystemEndpoint import SystemEndpoint
from .DeviceEndpoint import DeviceEndpoint
from .PanTiltEndpoint import PanTiltEndpoint
from .VisibleLensEndpoint import VisibleLensEndpoint

class InfinitiAPI:
    """
    A class representing the Infiniti API.

    This class provides a consolidated interface for interacting with various endpoints
    of the Infiniti Electro Optics' Octagon API. It initializes different endpoints like system,
    device, pantilt, and visible lens, offering a streamlined API interaction experience.

    Attributes:
    -----------
    api_caller : RWYAPICaller
        An instance of the RWYAPICaller class.
    system : SystemEndpoint
        An instance of the SystemEndpoint class.
    device : DeviceEndpoint
        An instance of the DeviceEndpoint class.
    pantilt : PanTiltEndpoint
        An instance of the PanTiltEndpoint class.
    visible : VisibleLensEndpoint
        An instance of the VisibleLensEndpoint class.
    """

    def __init__(self, base_url: str, auth: Tuple[str, str]) -> None:
        """
        Initializes a new instance of the InfinitiAPI class.

        Parameters:
        -----------
        base_url : str
            The base URL of the Infiniti Electro Optics' Octagon API.
        auth : Tuple[str, str]
            A tuple containing the username and password for authentication.

        Attributes Initialized:
        -----------------------
        api_caller : RWYAPICaller
            A helper to make raw API calls.
        system : SystemEndpoint
            Endpoint object to interact with system-related functionalities.
        device : DeviceEndpoint
            Endpoint object to interact with device-related functionalities.
        pantilt : PanTiltEndpoint
            Endpoint object to interact with pan-tilt functionalities.
        visible : VisibleLensEndpoint
            Endpoint object to interact with visible lens functionalities.
        """
        self.api_caller = RWYAPICaller(base_url, auth)
        self.system = SystemEndpoint(self.api_caller)
        self.device = DeviceEndpoint(self.api_caller)
        self.pantilt = PanTiltEndpoint(self.api_caller)
        self.visible = VisibleLensEndpoint(self.api_caller)

if __name__ == '__main__':
    # Instantiate the InfinitiAPI using environment variables for host and authentication
    api = InfinitiAPI(os.environ.get('host'), auth=(os.environ.get('user'), os.environ.get('password')))

    # Fetch and print system versions using the instantiated API
    print(api.system.get_versions())

    # Close the API caller's session
    api.api_caller.session.close()
