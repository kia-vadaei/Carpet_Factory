class AdjacencyGraph :

    graph = None
    vertex = int


    def getting_carpet_adjacency_matrix(self , count , graph_matrix):
        self.graph = graph_matrix
        self.vertex = count

        color = count
        return self.graph_colouring(color)



    # is safe for vertex v
    def is_safe(self, v, colour, c):
        for i in range(self.vertex):
            if self.graph[v][i] == 1 and colour[i] == c:
                return False
        return True

    # A recursive utility function to solve m
    # coloring  problem
    def graph_colour_util(self, m, colour, v):
        if v == self.vertex:
            return True

        for c in range(1, m + 1):
            if self.is_safe(v, colour, c) == True:
                colour[v] = c
                if self.graph_colour_util(m, colour, v + 1) == True:
                    return True
                colour[v] = 0
        return False
    def graph_colouring(self, m):
        colour = [0] * self.vertex
        if self.graph_colour_util(m, colour, 0) == False:
            return -1

        uniqe_colors = set()
        for c in colour:
            if c in uniqe_colors:
                continue
            uniqe_colors.add(c)

        # Print the solution
        # print("the least amount of color you need to color this carpet graph is : ")
        return len(uniqe_colors)

