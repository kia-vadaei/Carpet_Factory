#import Carpet
from Vertex import Vertex
class EdgeClass:
    start = Vertex
    end = Vertex
    element = int
    def __init__(self , s = Vertex , e = Vertex , element = -1):
        self.start = s
        self.end = e
        self.element = element

    def setElement(self , e):
        self.element = e
