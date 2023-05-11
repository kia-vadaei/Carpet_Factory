import json
import os.path
from MyGraph import Graph
from PIL import Image

class Carpet :
    _main_carpet_file_path = '../Files/carpet.json'
    carpet_map = [[0 for x in range(300)] for y in range(400)]
    price = float
    carpet_graph = Graph
    def __init__(self, carpet_map , price):
        self.carpet_map = carpet_map
        self.price = price

    @staticmethod
    def magnify_plan(self, matrix , scale_factor = 50):
        magnified_matrix = []
        for row in matrix:
            magnified_row = []
            for element in row:
                magnified_row.extend([element] * scale_factor)
            magnified_matrix.extend([magnified_row] * scale_factor)
        return magnified_matrix

    def convert_matrix_to_image(self , matrix, output_path):
        height = len(matrix)
        width = len(matrix[0])

        image = Image.new('RGB', (width, height), color='white')

        for y in range(height):
            for x in range(width):
                if matrix[y][x] == 1:   #red
                    image.putpixel((x, y), (255, 0, 0))  # Set pixel color to red
                if matrix[y][x] == 2:   #green
                    image.putpixel((x, y), (0, 255, 0))  # Set pixel color to green
                if matrix[y][x] == 3:   #blue
                    image.putpixel((x, y), (0, 0, 255))  # Set pixel color to blue

        # Save the image to the specified output path
        image.save(output_path)


#    def to_string(self):

