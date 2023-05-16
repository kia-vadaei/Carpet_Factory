# from Carpet import Carpet
from MyEdge import EdgeClass
from Vertex import Vertex


class Graph:
    edges = list
    vertices = list

    def __init__(self):
        self.edges = list()
        self.vertices = list()

    def add_vertex(self, name , is_department):
        v = Vertex(name , is_department)
        self.vertices.append(v)
        return v
    def bfs(self, starting_point=Vertex):
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

    def add_edge(self, start_node_name, end_node_name):
        try:
            start_node = self.find_vertex(start_node_name)
            end_node = self.find_vertex(end_node_name)
        except Exception as e:
            print(e)

        if self.getEdge(start_node, end_node) is None:
            edge = EdgeClass(start_node, end_node)

            # adding connected people
            end_node.add_link(start_node, edge)
            start_node.add_link(end_node, edge)

            # adding the new edge
            self.edges.append(edge)

        else:
            raise Exception('you are already connected to this user')

    def find_vertex(self, name):
        for vertex in self.vertices:
            if vertex.name == name:
                return vertex
        raise Exception('this vertex does not exist!')
