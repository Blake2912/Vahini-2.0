from dataclasses import dataclass

@dataclass
class Coordinates:
    """
    This is the data class that will store the vehicle location and help in easy access
    """
    point_name: str
    point_coordinate : tuple