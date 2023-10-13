# Octagon API Python Wrapper by Infiniti Electro Optics

This Python library provides a seamless wrapper around the Octagon API by Infiniti Electro Optics, facilitating effortless interactions with all their PTZ (Pan-Tilt-Zoom) cameras.

## Features

- Complete Pythonic access to all Octagon API endpoints.
- Simplified methods for interacting with PTZ cameras.
- Built with extensibility and ease-of-use in mind.

## Installation

To install the wrapper, you can use pip: 

TODO - PyPi hosting coming soon

## Quick Start

```python
from infiniti_api.InfinitiAPI import InfinitiAPI

# Initialize the API caller with the base URL
octagon_ip = os.environ.get('OCTAGON_IP')
user = os.environ.get('OCTAGON_USERNAME')
pass = os.environ.get('OCTAGON_PASSWORD')

api = InfinitiAPI(f"https://{octagon_ip}", auth=(user, pass))

# Fetch the zoom and focus values of the visible lens
zoom, focus = api.visible.get_visiblelens()
print(f"Zoom: {zoom}, Focus: {focus}")

# Set the zoom value for the visible lens
api.visible.set_zoom(5)
```
