import sys

from matplotlib import pyplot as plt

from MyMap import MyMap
from Sort import QuickSort

from enum import Enum


class InterSection(Enum):
	one = 0
	two = 1
	three = 2
	four = 3
	five = 4
	six = 5
	seven = 6
	eight = 7
	nine = 8
	ten = 9
class CityMap :

	class_vertices = list

	def __init__(self, v_count, class_vertices , graph):
		self.v_count = v_count
		self.graph = graph
		self.class_vertices = class_vertices


	def printSolution(self, dist):

		department_list = list()
		left_coordinates = list()
		heights = list()
		# print("Vertex \tDistance from Source")
		for node in range(self.v_count):
			# print(node, "\t", dist[node])
			left_coordinates.append(node)
			heights.append(dist[node])
			path_department = MyMap(self.class_vertices[node] , dist[node])
			department_list.append(path_department)
		QuickSort.quickSort(department_list , 0 , len(department_list)- 1)

		CityMap.show_diagram(left_coordinates, heights)

		for department in department_list :
			if department.key.is_department:
				return department
		raise Exception('Something went wrong!')



	@staticmethod
	def show_diagram(left_coordinates , heights):
		bar_labels = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']

		plt.bar(left_coordinates, heights, tick_label=bar_labels, width=0.6, color=['cyan', 'purple'])
		plt.xlabel('Vertices')
		plt.ylabel('Distance')
		plt.title("Vertex-Distance line graph")
		plt.show()
	def minDistance(self, dist, sptSet):

		# Initialize minimum distance for next node
		min = sys.maxsize
		min_index = -1
		# Search not nearest vertex not in the
		# shortest path tree
		for u in range(self.v_count):
			if dist[u] < min and sptSet[u] == False:
				min = dist[u]
				min_index = u

		return min_index

	# Function that implements Dijkstra's single source
	# shortest path algorithm for a graph represented
	# using adjacency matrix representation
	def dijkstra(self, src):

		dist = [sys.maxsize] * self.v_count
		dist[src] = 0
		sptSet = [False] * self.v_count

		for cout in range(self.v_count):

			# Pick the minimum distance vertex from
			# the set of vertices not yet processed.
			# x is always equal to src in first iteration
			x = self.minDistance(dist, sptSet)

			# Put the minimum distance vertex in the
			# shortest path tree
			sptSet[x] = True

			# Update dist value of the adjacent vertices
			# of the picked vertex only if the current
			# distance is greater than new distance and
			# the vertex in not in the shortest path tree
			for y in range(self.v_count):
				if self.graph[x][y] > 0 and sptSet[y] == False and \
						dist[y] > dist[x] + self.graph[x][y]:
					dist[y] = dist[x] + self.graph[x][y]

		return self.printSolution(dist)

