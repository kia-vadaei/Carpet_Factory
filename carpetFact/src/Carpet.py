import json
import os.path
import subprocess
from tkinter import filedialog

from MyGraph import Graph
from PIL import Image
from Sort import QuickSort
from MyMap import MyMap



class Carpet :
    _main_carpet_file_path = '../Files/carpet.json'
    carpet_layout_matrix = list()
    carpet_layout_6_in_8_matrix = list()
    layout_path = str
    price = float
    carpet_graph = Graph

    def __init__(self , price):
        #self.carpet_map = carpet_map
        self.price = price
        self.layout_path = ''
        all_layout_list = list()


    def magnify_plan(self , matrix , scale_factor):
        magnified_matrix = []
        for row in matrix:
            magnified_row = []
            for element in row:
                magnified_row.extend([element] * scale_factor)
            magnified_matrix.extend([magnified_row] * scale_factor)

        self.carpet_layout_6_in_8_matrix = matrix
        self.carpet_layout_matrix = magnified_matrix    #To set the obj matrix

        return magnified_matrix

    def set_layout(self , matrix, output_path):
        height = len(matrix)
        width = len(matrix[0])
        matrix = self.magnify_plan(matrix , int(300 / width))

        width = 300
        height = 400
        image = Image.new('RGB', (width, height), color='white')

        for y in range(height):
            for x in range(width):
                if matrix[y][x] == 1:   #red
                    image.putpixel((x, y), (255, 0, 0))  # Set pixel color to red
                if matrix[y][x] == 2:   #green
                    image.putpixel((x, y), (0, 255, 0))  # Set pixel color to green
                if matrix[y][x] == 3:   #blue
                    image.putpixel((x, y), (0, 0, 255))  # Set pixel color to blue
                if matrix[y][x] == 4:   #blue
                    image.putpixel((x, y), (255, 255, 0))  # Set pixel color to blue

        # Save the image to the specified output path
        self.layout_path = output_path
        image.save(output_path)

    def show_layout(self) :
        if self.layout_path != '':
            img = Image.open(self.layout_path)
            img.show()
        else: raise Exception('This carpet has no layout yet!')



    @staticmethod
    def calculate_similarity(matrix1, matrix2, match_score = 2, mismatch_score = -1, gap_penalty = -1):
        # Convert the matrices to 1D arrays
        array1 = [item for sublist in matrix1 for item in sublist]
        array2 = [item for sublist in matrix2 for item in sublist]

        # Get the lengths of the arrays
        len1, len2 = len(array1), len(array2)

        # Initialize the alignment matrix
        alignment_matrix = [[0] * (len2 + 1) for _ in range(len1 + 1)]

        # Fill the first row and column with gap penalties
        for i in range(1, len1 + 1):
            alignment_matrix[i][0] = alignment_matrix[i - 1][0] + gap_penalty
        for j in range(1, len2 + 1):
            alignment_matrix[0][j] = alignment_matrix[0][j - 1] + gap_penalty

        # Fill the alignment matrix
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                # Calculate the match/mismatch score
                if array1[i - 1] == array2[j - 1]:
                    score = match_score
                else:
                    score = mismatch_score
                # Calculate the scores for different operations
                match = alignment_matrix[i - 1][j - 1] + score
                delete = alignment_matrix[i - 1][j] + gap_penalty
                insert = alignment_matrix[i][j - 1] + gap_penalty
                # Choose the maximum score among match, delete, and insert
                alignment_matrix[i][j] = max(match, delete, insert)

        # The similarity score is the value in the bottom-right corner of the alignment matrix
        similarity_score = alignment_matrix[len1][len2]

        return similarity_score

    @staticmethod
    def search(input_carpet , carpets=list):

        score_list = list()
        for carpet in carpets:
            myMap = MyMap(carpet , Carpet.calculate_similarity(input_carpet.carpet_layout_6_in_8_matrix , carpet.carpet_layout_6_in_8_matrix))

            score_list.append(myMap)

        #calling the quick sort method
        QuickSort.quickSort(score_list , 0 , len(score_list)-1)

        return score_list[len(score_list) - 3 : ]


    def new_carpet_layout(self):
        subprocess.Popen('mspaint.exe')



    def open_layout(self):
        file_path = filedialog.askopenfile(defaultextension='.png', filetypes=[('PNG Image', '*.png')])
        img = Image.open(file_path.name)
        img = img.resize((300,400))
        img = img.resize((6,8))
        img.save("p6in8.png")