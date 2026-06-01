## A sigle cell to compose the game board
## The consept to compose the board is based on the graph theory
##
## The value identify if the cell own a mine(1) or not(0) 
## The node_type, helpe the system to comprehend the cell position and the number of connection
## Neighbors is simply the number of connection
## Flagged identify if the use have flagged this cell
## Position is the coordinate of cell in the game board
## State indicate the actual state of cell, it can be cover(0), empty(1), with_number(2)
class Cell:
    def __init__(self, 
                 position: tuple[int, int],
                 node_type: int,
                 neighbors: list['Cell'], 
                 flagged: bool = False, 
                 value: int = 0, 
                 state: tuple[int, int] = (0, 0)):
 
        if not value in (0, 1):
            raise IndexError(f"The value {value} is not 0 or 1")

        for cell in neighbors:
            if not isinstance(cell, Cell):
                raise TypeError(f"Neighbors list can only contain a Cell type item not {type(cell)}")

        if not node_type in (0, 1, 2):
            raise IndexError(f"The value {value} is not 0 or 1 or 2")
        
        self.value = value
        self.neighbors = neighbors
        self.node_type = node_type
        self.position = position
        self.flagged = flagged
        self.state = state

    def numberOfMineInNeighboars(self) -> int:
        mine_number = 0
        for cell in self.neighbors:
            if cell.value == 1:
                mine_number += 1
        return mine_number
