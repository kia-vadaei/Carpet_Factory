import json
import os.path
from MyGraph import Graph

class Carpet :
    _main_carpet_file_path = '../Files/carpet.json'
    carpet_map = [[0 for x in range(300)] for y in range(400)]
    price = float
    carpet_graph = Graph
    def __init__(self, carpet_map , price):
        self.carpet_map = carpet_map
        self.price = price


#    def to_string(self):

