from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from edge import Edge

class Node:
    def __init__(self, value, edges: list["Edge"]):

        self.value = value
        self.edges = edges


