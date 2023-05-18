import os
import random
import time

from Carpet import Carpet
from LeastColor import AdjacencyGraph
from CityMap import CityMap, InterSection
from Shape import Shape
from MyGraph import Graph
from Vertex import Vertex
from MyEdge import EdgeClass
import matplotlib.pyplot as plt
import colorama
from colorama import Fore
from colorama import Back

#os.system('cls')
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

# c1 = Carpet(0)
# c2 = Carpet(0)
# c3 = Carpet(0)
# c4 = Carpet(0)
# c5 = Carpet(0)
# c6 = Carpet(0)
# c7 = Carpet(0)
#
#
# m1 = [
# [0, 0, 1, 0, 0, 1],
# [0, 1, 1, 1, 0, 1],
# [0, 1, 0, 1, 0, 0],
# [1, 0, 1, 0, 1, 0],
# [1, 0, 1, 1, 1, 1],
# [0, 1, 0, 0, 1, 1],
# [1, 0, 1, 1, 1, 1],
# [0, 1, 0, 0, 1, 1]
# ]
#
# m2 = [
# [1, 0, 1, 0, 1, 1],
# [1, 1, 1, 0, 1, 0],
# [0, 1, 1, 0, 0, 1],
# [0, 1, 1, 1, 1, 0],
# [0, 0, 0, 1, 0, 1],
# [0, 1, 0, 1, 0, 1],
# [0, 0, 0, 1, 0, 1],
# [0, 1, 0, 1, 0, 1]
# ]
# m3 = [
# [1, 1, 1, 1, 1, 1],
# [1, 1, 1, 1, 1, 1],
# [1, 1, 1, 1, 1, 1],
# [1, 1, 0, 0, 1, 1],
# [1, 1, 0, 0, 1, 1],
# [1, 1, 1, 1, 1, 1],
# [1, 1, 1, 1, 1, 1],
# [1, 1, 1, 1, 1, 1]
# ]
# m4 = [
# [3, 3, 3, 3, 3, 3],
# [3, 3, 3, 3, 3, 3],
# [3, 3, 3, 3, 3, 3],
# [3, 3, 0, 0, 3, 3],
# [3, 3, 0, 0, 3, 3],
# [3, 3, 3, 3, 3, 3],
# [3, 3, 3, 3, 3, 3],
# [3, 3, 3, 3, 3, 3]
# ]
# m5 = [
# [1, 0, 1, 0, 1, 1],
# [1, 1, 1, 0, 1, 0],
# [0, 1, 1, 0, 0, 1],
# [0, 1, 1, 1, 1, 0],
# [0, 0, 0, 1, 0, 1],
# [0, 1, 0, 1, 0, 1],
# [0, 0, 0, 1, 0, 1],
# [0, 1, 0, 1, 0, 1]
# ]
# m6 = [
# [1, 0, 1, 0, 1, 1],
# [1, 1, 1, 0, 1, 0],
# [0, 1, 1, 0, 0, 1],
# [0, 1, 1, 1, 1, 0],
# [0, 0, 0, 1, 0, 1],
# [0, 1, 0, 1, 0, 1],
# [0, 0, 0, 1, 0, 1],
# [0, 1, 0, 1, 0, 1]
# ]
# m7 = [
# [2, 2, 2, 2, 2, 2],
# [2, 2, 2, 2, 2, 2],
# [2, 2, 2, 2, 2, 2],
# [2, 2, 0, 4, 2, 2],
# [2, 2, 0, 0, 2, 3],
# [2, 2, 2, 2, 2, 3],
# [2, 2, 2, 2, 2, 3],
# [2, 4, 3, 3, 3, 3]
# ]
#
# m_in = [
# [2, 2, 2, 2, 2, 2],
# [2, 2, 2, 2, 2, 2],
# [2, 2, 2, 2, 2, 2],
# [2, 2, 0, 0, 2, 2],
# [2, 2, 0, 0, 2, 2],
# [2, 2, 2, 2, 2, 2],
# [2, 2, 2, 2, 2, 2],
# [2, 2, 2, 2, 2, 2]
# ]
# c_in = Carpet(0)
# c_in.set_layout(m_in , 'Pictures/input.png')
#
# c1.set_layout(m1, 'Pictures/p1.png')
# c2.set_layout(m2, 'Pictures/p2.png')
# c3.set_layout(m3, 'Pictures/p3.png')
# c4.set_layout(m4, 'Pictures/p4.png')
# c5.set_layout(m5, 'Pictures/p5.png')
# c6.set_layout(m6, 'Pictures/p6.png')
# c7.set_layout(m7, 'Pictures/p7.png')
# l = list()
# l.append(c1)
# l.append(c2)
# l.append(c3)
# l.append(c4)
# l.append(c5)
# l.append(c6)
# l.append(c7)
# r = Carpet.search(c_in , l)
#
# #c_in.show_layout()
# r[0].carpet.show_layout()
# r[1].carpet.show_layout()
# r[2].carpet.show_layout()
#
# print(r)

# c = Carpet(0)
# c.convert_image_to_matrix()
# c.show_layout()


# c1 = Carpet(8)
# c2 = Carpet(7)
# c3 = Carpet(19)
# c4 = Carpet(23)
# c5 = Carpet(43)
# c6 = Carpet(3)
# c7 = Carpet(9)
#
# l = list()
# l.append(c1)
# l.append(c2)
# l.append(c3)
# l.append(c4)
# l.append(c5)
# l.append(c6)
# l.append(c7)
#
# val = list()
#
# for i in range(7):
#     val.append(1)
#
# Carpet.efficient_shopping(43 , l , val ,len(l))
#

# g = Graph()
# g.add_vertex("k" , 0)
# g.add_vertex("k2" , 0)
# g.add_vertex("k3" , 0)
# g.add_vertex("k4" , 0)
# g.add_vertex("k5" , 0)
#
# g.add_edge('k' , 'k2')
# g.add_edge('k3' , 'k4')
# print('Done')




# print('sdf')
# x = 'nine'
# try:
#     print((InterSection[x].value))
# except KeyError as e:
#     print(e)

# graph = [
#     [0, 4, 2, 0, 0, 0, 0, 0, 0],
#     [4, 0, 0, 5, 0, 0, 0, 0, 0],
#     [2, 0, 0, 3, 0, 0, 0, 0, 0],
#     [0, 5, 3, 0, 1, 0, 0, 0, 0],
#     [0, 0, 0, 1, 0, 2, 0, 0, 0],
#     [0, 0, 0, 0, 2, 0, 4, 0, 0],
#     [0, 0, 0, 0, 0, 4, 0, 5, 0],
#     [0, 0, 0, 0, 0, 0, 5, 0, 3],
#     [0, 0, 0, 0, 0, 0, 0, 3, 0]
# ]
#
# vertices2 = list()
# v0 = Vertex(0,False)
# v1 = Vertex(1,True)
# v2 = Vertex(2,False)
# v3 = Vertex(3,False)
# v4 = Vertex(4,True)
# v5 = Vertex(5,False)
# v6 = Vertex(6,True)
# v7 = Vertex(7,False)
# v8 = Vertex(8,True)
# vertices2.append(v0)
# vertices2.append(v1)
# vertices2.append(v2)
# vertices2.append(v3)
# vertices2.append(v4)
# vertices2.append(v5)
# vertices2.append(v6)
# vertices2.append(v7)
# vertices2.append(v8)
# c = CityMap(len(vertices2) , vertices2 , graph)
# rslt = c.dijkstra(7)
# print(rslt.key.name)

def animated_effect(str):
    for c in str:
        print(c , end='')
        time.sleep(90/1000)
    time.sleep(200/1000)
#print('\t\t*** UNIVERSITY OF ISFAHAN ***')


animated_effect('\t\t*** UNIVERSITY OF ISFAHAN ***\n\n')


while True:
    print(Fore.MAGENTA + '1) Design a new carpet')
    print('2) Search by carpet design')
    print('3) Purchase based on amount of money')
    print('4) Navigate to the nearest factory store')
    cmd = input(Fore.BLUE + '👉🏻 ')
    print(Fore.MAGENTA)
    if cmd == '1':  # Design a new carpet
        print("🟪 Enter the amount of areas :" , end=' ')
        count = int(input())

        graph_matrix = [[0] * count for x in range (count)]

        print("\n🟪 Enter the adjacency of each of the areas :" ,end='\n')

        for row in graph_matrix:
            tmp_row = input().split(' ')
            for i in range(len(row)):
                row[i] = int(tmp_row[i])

        g = AdjacencyGraph()
        rslt = g.getting_carpet_adjacency_matrix(count , graph_matrix)
        print("\n🟣 The least amount of color you need to color this carpet graph is :" , end= ' ')
        print(Fore.CYAN + str(rslt) , end='\n\n')

    elif cmd == '2':    # Search by carpet design
        input_carpet = Carpet(0)
        input_carpet.load_image()
        print('d')
    elif cmd == '3':    # Purchase based on amount of money
        print()
    elif cmd == '4':    # Navigate to the nearest factory store
        print()

# input_carpet = Carpet(0)
# input_carpet.load_image()
# print('2')