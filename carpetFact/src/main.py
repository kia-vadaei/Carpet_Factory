import random

from Carpet import Carpet
from Shape import Shape
from MyGraph import Graph
from Vertex import Vertex
from MyEdge import EdgeClass
vertices = list()
tmp_list = ["morabaa" , "mostatil" , "mosalas"]
tmp2_list = ["red" , "green" , "blue" , "yellow"]
for i in range(10):

    vertices.append(Vertex(random.choice(tmp_list) , random.choice(tmp2_list)))


G = Graph()
G.vertices = vertices
G.add_edge(vertices[0] , vertices[2])
G.add_edge(vertices[1] , vertices[5])
G.add_edge(vertices[1] , vertices[2])
G.add_edge(vertices[2] , vertices[5])
G.add_edge(vertices[0] , vertices[1])



x = Carpet("asd" , 0)


