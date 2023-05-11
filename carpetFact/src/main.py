import random

from Carpet import Carpet
from Shape import Shape
from MyGraph import Graph
from Vertex import Vertex
from MyEdge import EdgeClass
# vertices = list()
# tmp_list = ["morabaa" , "mostatil" , "mosalas"]
# tmp2_list = ["red" , "green" , "blue" , "yellow"]
# for i in range(10):
#
#     vertices.append(Vertex(random.choice(tmp_list) , random.choice(tmp2_list)))
#
#
# G = Graph()
# G.vertices = vertices
# G.add_edge(vertices[0] , vertices[2])
# G.add_edge(vertices[1] , vertices[5])
# G.add_edge(vertices[1] , vertices[2])
# G.add_edge(vertices[2] , vertices[5])
# G.add_edge(vertices[0] , vertices[1])
#
# m = [[0] * 6 for x in range(8)]
# for row in m:
#     tmp_row = input().split(' ')
#     for i in range(len(row)):
#         row[i] = int(tmp_row[i])
#
# x = Carpet("asd" , 0)
# #m = x.magnify_plan(list(m) , 50)
# x.convert_matrix_to_image(m, 'r.png')
# x.show_layout()

c1 = Carpet(0)
c2 = Carpet(0)
c3 = Carpet(0)
c4 = Carpet(0)
c5 = Carpet(0)
c6 = Carpet(0)
c7 = Carpet(0)


m1 = [
[0, 0, 1, 0, 0, 1],
[0, 1, 1, 1, 0, 1],
[0, 1, 0, 1, 0, 0],
[1, 0, 1, 0, 1, 0],
[1, 0, 1, 1, 1, 1],
[0, 1, 0, 0, 1, 1],
[1, 0, 1, 1, 1, 1],
[0, 1, 0, 0, 1, 1]
]

m2 = [
[1, 0, 1, 0, 1, 1],
[1, 1, 1, 0, 1, 0],
[0, 1, 1, 0, 0, 1],
[0, 1, 1, 1, 1, 0],
[0, 0, 0, 1, 0, 1],
[0, 1, 0, 1, 0, 1],
[0, 0, 0, 1, 0, 1],
[0, 1, 0, 1, 0, 1]
]
m3 = [
[1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1],
[1, 1, 0, 0, 1, 1],
[1, 1, 0, 0, 1, 1],
[1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1]
]
m4 = [
[3, 3, 3, 3, 3, 3],
[3, 3, 3, 3, 3, 3],
[3, 3, 3, 3, 3, 3],
[3, 3, 0, 0, 3, 3],
[3, 3, 0, 0, 3, 3],
[3, 3, 3, 3, 3, 3],
[3, 3, 3, 3, 3, 3],
[3, 3, 3, 3, 3, 3]
]
m5 = [
[1, 0, 1, 0, 1, 1],
[1, 1, 1, 0, 1, 0],
[0, 1, 1, 0, 0, 1],
[0, 1, 1, 1, 1, 0],
[0, 0, 0, 1, 0, 1],
[0, 1, 0, 1, 0, 1],
[0, 0, 0, 1, 0, 1],
[0, 1, 0, 1, 0, 1]
]
m6 = [
[1, 0, 1, 0, 1, 1],
[1, 1, 1, 0, 1, 0],
[0, 1, 1, 0, 0, 1],
[0, 1, 1, 1, 1, 0],
[0, 0, 0, 1, 0, 1],
[0, 1, 0, 1, 0, 1],
[0, 0, 0, 1, 0, 1],
[0, 1, 0, 1, 0, 1]
]
m7 = [
[2, 2, 2, 2, 2, 2],
[2, 2, 2, 2, 2, 2],
[2, 2, 2, 2, 2, 2],
[2, 2, 0, 4, 2, 2],
[2, 2, 0, 0, 2, 3],
[2, 2, 2, 2, 2, 3],
[2, 2, 2, 2, 2, 3],
[2, 4, 3, 3, 3, 3]
]

m_in = [
[2, 2, 2, 2, 2, 2],
[2, 2, 2, 2, 2, 2],
[2, 2, 2, 2, 2, 2],
[2, 2, 0, 0, 2, 2],
[2, 2, 0, 0, 2, 2],
[2, 2, 2, 2, 2, 2],
[2, 2, 2, 2, 2, 2],
[2, 2, 2, 2, 2, 2]
]
c_in = Carpet(0)
c_in.set_layout(m_in , 'Pictures/input.png')

c1.set_layout(m1, 'Pictures/p1.png')
c2.set_layout(m2, 'Pictures/p2.png')
c3.set_layout(m3, 'Pictures/p3.png')
c4.set_layout(m4, 'Pictures/p4.png')
c5.set_layout(m5, 'Pictures/p5.png')
c6.set_layout(m6, 'Pictures/p6.png')
c7.set_layout(m7, 'Pictures/p7.png')
l = list()
l.append(c1)
l.append(c2)
l.append(c3)
l.append(c4)
l.append(c5)
l.append(c6)
l.append(c7)
r = Carpet.search(c_in , l)

#c_in.show_layout()
r[0].carpet.show_layout()
r[1].carpet.show_layout()
r[2].carpet.show_layout()

print(r)

