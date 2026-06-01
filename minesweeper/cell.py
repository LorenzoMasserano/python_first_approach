## A sigle cell to compose the game board
## The consept to compose the board is based on the graph theory
##
## The value identify if the cell own a mine(1) or not(0) 
## The node_type, helpe the system to comprehend the cell position and the number of connection
## Neighbors is simply the number of connection
## Flagged identify if the use have flagged this cell
class Cell:
    def __init__(self, value: int, neighbors: [], node_type: int, flagged: bool = False):

        if not isinstance(value, int):
            raise TypeError(f"The value {value} is not a int")
        
        if not value is (0, 1):
            raise IndexError(f"The value {value} is not 0 or 1")

        if not isinstance(neighbors, list):
            raise TypeError(f"The value {value} it is not a list")

        for cell in neighbors:
            if not isinstance(cell, Cell):
                raise TypeError(f"Neighbors list can only contain a Cell type item not {type(cell)}")

        if not isinstance(node_type, int):
            raise TypeError(f"The value {value} it is not a int")

        if not node_type in (0, 1, 2):
            raise IndexError(f"The value {value} is not 0 or 1 or 2")
        
        if node_type == 0 and not len(neighbors) == 3:
            raise IndexError(f"If the cell is a angle, it most have 3 connection")

        if node_type == 1 and not len(neighbors) == 5:
            raise IndexError(f"If the cell is a side, it most have 5 connection")

        if node_type == 2 and not len(neighbors) == 8:
            raise IndexError(f"If the cell is a center, it most have 8 connection")

        if not isinstance(flagged, bool):
            raise TypeError("Flagged can olny be bool type")
  
        self.value = value,
        self.neighbors = neighbors
        self.type = type
        self.type = type

    def numberOfMineInNeighboars(self):
        mine_number = 0
        for cell in self.neighbors:
            if cell.value == 1:
                mine_number += 1
        return mine_number        
 
