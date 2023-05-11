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

m = [[0] * 6 for x in range(8)]
print(type(m))
for row in m:
    tmp_row = input().split(' ')
    for i in range(len(row)):
        row[i] = int(tmp_row[i])

print(type(m))
x = Carpet("asd" , 0)
m = Carpet.magnify_plan(list(m) , 50)
x.convert_matrix_to_image(m, 'r.png')
