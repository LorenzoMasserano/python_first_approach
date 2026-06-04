from node import Node

class Edge:
    def __init__(self, value: int | None, node: Node):
        self.value = value
        self.node = node
