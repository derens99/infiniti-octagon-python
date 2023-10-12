import os
import dotenv
dotenv.load_dotenv()

from .RWYAPICaller import RWYAPICaller
from .SystemEndpoint import SystemEndpoint
from .DeviceEndpoint import DeviceEndpoint
from .PanTiltEndpoint import PanTiltEndpoint
from .VisibleLensEndpoint import VisibleLensEndpoint

class InfinitiAPI:
    """
    A class representing the Infiniti API.

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

    def __init__(self, base_url, auth=None):
        self.api_caller = RWYAPICaller(base_url, auth)
        self.system = SystemEndpoint(self.api_caller)
        self.device = DeviceEndpoint(self.api_caller)
        self.pantilt = PanTiltEndpoint(self.api_caller)
        self.visible = VisibleLensEndpoint(self.api_caller)

if __name__ == '__main__':
    api = InfinitiAPI(os.environ.get('host'), auth=(os.environ.get('user'), os.environ.get('password')))
    print(api.system.get_versions())
    api.api_caller.session.close()