import os
import random
import sys
import time
from tkinter import filedialog

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


def animated_effect(str):
    for c in str:
        print(Fore.BLUE + c , end='')
        time.sleep(90/1000)
    time.sleep(200/1000)

city_graph = [
    [0, 4, 2, 0, 0, 0, 0, 0, 0],
    [4, 0, 0, 5, 0, 0, 0, 0, 0],
    [2, 0, 0, 3, 0, 0, 0, 0, 0],
    [0, 5, 3, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 2, 0, 0, 0],
    [0, 0, 0, 0, 2, 0, 4, 0, 0],
    [0, 0, 0, 0, 0, 4, 0, 5, 0],
    [0, 0, 0, 0, 0, 0, 5, 0, 3],
    [0, 0, 0, 0, 0, 0, 0, 3, 0]
]

city_graph_vertices = list()

v0 = Vertex(0,False)
v1 = Vertex(1,True)
v2 = Vertex(2,False)
v3 = Vertex(3,False)
v4 = Vertex(4,True)
v5 = Vertex(5,False)
v6 = Vertex(6,True)
v7 = Vertex(7,False)
v8 = Vertex(8,True)
city_graph_vertices.append(v0)
city_graph_vertices.append(v1)
city_graph_vertices.append(v2)
city_graph_vertices.append(v3)
city_graph_vertices.append(v4)
city_graph_vertices.append(v5)
city_graph_vertices.append(v6)
city_graph_vertices.append(v7)
city_graph_vertices.append(v8)


try:
    animated_effect('\t\t*** UNIVERSITY OF ISFAHAN ***\n\n')

    print(Fore.MAGENTA +'Select the initial carpets...\n---------------------------------')
    time.sleep(1)
    carpets = Carpet.set_carpets()
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
            rslt = Carpet.search(input_carpet , carpets)

            print('The result will be shown soon...')

            time.sleep(2)


            rslt[2].key.show_layout()
            rslt[1].key.show_layout()
            rslt[0].key.show_layout()


        elif cmd == '3':    # Purchase based on amount of money

            print("🟪 The prices are as follows: " , end=' ')

            for carpet in carpets:
                print(carpet.price , end=' ')

            print('\n🟪 Enter the amount  of your money :', end=' ')
            input_money = int(input())
            res , res_list = Carpet.efficient_shopping(input_money , carpets , [1] * len(carpets) ,len(carpets))

            print('\n🟣 The result is :' ,end=' ')
            print(res , res_list)
        elif cmd == '4':    # Navigate to the nearest factory store
            print('\n🟪 Enter the index of the Intersection that you are at (one to nine) :' , end=' ')
            input_intersection = input()

            try:
                input_intersection = InterSection[input_intersection].value
            except KeyError as e:
                print('\n🔴 The input is wrong...')
                print('\n---------------------------------')
                continue

            c = CityMap(len(city_graph_vertices), city_graph_vertices, city_graph)
            rslt = c.dijkstra(input_intersection)



            print('\n🟣 The nearest department to you is : ' + str(rslt.key.name))

        print('\n---------------------------------')
except Exception as e:
    print('\n🔴' , end= ' ')
    print(e , end='\n\n')
    os.system("python main.py")