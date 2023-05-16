#from Carpet import CarpetClass
from Shape import Shape
#from MyEdge import EdgeClass

class Vertex:

    is_department = bool
    name = str
    linked_vertices = dict

    def __init__(self, name, is_department):
        self.name = name
        self.is_department = is_department
        self.linked_vertices = dict()

    def add_link(self, u , e):
        self.linked_vertices[u] = e
