class Point:
    def __init__(self, coordinate: tuple[int, int, int], connections: list['Point'], char_representation: str = "·"):
        self.coordinate = coordinate
        self.connections = connections
        self.char_rapresentation = char_representation
        
