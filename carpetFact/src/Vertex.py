#from Carpet import CarpetClass
from Shape import Shape
#from MyEdge import EdgeClass

class Vertex:
    node = Shape
    linked_vertices = dict
    vertex_code = str


    def __init__(self, type , color):
        #self.vertex_code =
        self.linked_vertices = dict()
        shp = Shape(type, color)
        self.node = shp


    def add_link(self, u , e):
        self.linked_vertices[u] = e
