from enum import Enum
from data_structures.edge import Edge
from data_structures.node import Node

class NodeType(Enum):
        PREVIOUS = 0
        NEXT = 1

class LinkedList:
    def __init__(self, elements = []):
        self.__head = self.__instatiate(elements)     

    def __iter__(self):
        current_node = self.__head
        while current_node is not None:
            yield current_node.value
            current_node = self.__get_next(current_node)

    def __next__(self):
        if self._current_iter_node is None:
            raise StopIteration
        
        value = self._current_iter_node.value
        self._current_iter_node = self.__get_next(self._current_iter_node)
        return value        

    def __instatiate(self, elements = []) -> Node | None:
    
        head = None 

        for index, item in enumerate(elements):
            if index == 0:
                head = Node(
                    value= item,
                    edges= []
                )
            else:
                if head != None:
                    node = self.get_last(head)
                    new_node = Node(
                        value= item,
                        edges= []
                    )
                    node = self.__connect_node(node, new_node)
                
        return head
    
    def get_last(self, node: Node) -> Node:
        for edge in node.edges:
                if edge.value == 1:
                    return self.get_last(edge.node)
        
        return node

    def __get_next(self, node: Node) -> Node | None:
        for edge in node.edges:
            if edge.value == 1:
                return edge.node
        return None

    def __connect_node(self, base_node: Node, node_to_connect: Node) -> Node:

        edge_next = Edge(
            value= NodeType.NEXT.value,
            node= node_to_connect
        )

        edge_previous = Edge(
            value= NodeType.PREVIOUS.value,
            node= base_node
        )

        base_node.edges.append(edge_next)
        node_to_connect.edges.append(edge_previous)

        return base_node 

    def add(self, new_element):
        
        if self.__head != None:
            new_node = Node(
                value= new_element,
                edges = []
            )
            self.__connect_node(self.__head, new_node)
        else:
            self.__head = self.__instatiate([new_element])

    def adds(self, new_elements: list):

        for e in new_elements:
            self.add(e)

    def get_by_index(self, index: int):

        if self.__head != None:
            current_node = self.__head
            for _ in range(index):
                current_node = self.__get_next(current_node)
                if current_node == None:
                    raise IndexError("Index out of range")
        else:
            raise IndexError("Head is None")

        return current_node.value
        
