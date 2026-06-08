from enum import Enum

class CoordinateType(Enum):
    X = 0
    Y = 1
    Z = 2

class Point:

    def __init__(self, coordinate: tuple[float, float, float], connections: list['Point'], char_representation: str = "·"):
        self.coordinate = coordinate
        self.connections = connections
        self.char_rapresentation = char_representation
    
    def __getitem__(self, coordinate_type: CoordinateType) -> float:

        if coordinate_type is CoordinateType.X:
            return self.coordinate[0]
        elif coordinate_type is CoordinateType.Y:
            return self.coordinate[1]
        else:
            return self.coordinate[2]

    def __setitem__(self, coordinate_type: CoordinateType, new_value: float):

        if coordinate_type is CoordinateType.X:
            self.coordinate = (new_value, self.coordinate[1], self.coordinate[2])
        elif coordinate_type is CoordinateType.Y:
            self.coordinate = (self.coordinate[0], new_value, self.coordinate[2])
        else:
            self.coordinate = (self.coordinate[0], self.coordinate[1], new_value)


