#from Carpet import Carpet
from MyEdge import EdgeClass
from Vertex import Vertex


class Graph:
    edges = list()
    vertices = list()

    def __init__(self):
        self.edges = list()
        self.vertices = list()

    def find_vertex(self):
        {}

    def add_vertex(self , type , color):
        v = Vertex(type , color)
        self.vertices.append(v)
        return v

    def bfs(self , starting_point=Vertex):
        known = list()
        bfs_tree = dict()
        level = list()

        known.append(starting_point)
        level.append(starting_point)

        while len(level) != 0:

            next_level = list()
            for node in level:
                for linked in list(node.linked_vertices.keys()):
                    if not known.__contains__(linked):
                        known.append(linked)
                        next_level.append(linked)

            level = next_level

        return bfs_tree

    def getEdge(self, v=Vertex, u=Vertex):
        try:

            if v.linked_vertices.keys().__contains__(u):
                return v.linked_vertices[u]
        except Exception:
            return None

    def add_edge(self, start_node=Vertex, end_node=Vertex):

        if self.getEdge(start_node, end_node) is None:
            edge = EdgeClass(start_node, end_node)

            # adding connected people
            end_node.add_link(start_node, edge)
            start_node.add_link(end_node, edge)

            # adding the new edge
            self.edges.append(edge)

        else:
            raise Exception('you are already connected to this user')
