class FindLeastColor :

    graph = None
    vertex = int


    def getting_carpet_adjacency_matrix(self):
        print("please enter carpet matrix : first enter the amount of areas:")

        area = input()
        area = int(area)

        carpet_matrix = [[0] * area for x in range (area)]


        print("now please enter the adjacency of each of the areas : ")

        for row in carpet_matrix:
            tmp_row = input().split(' ')
            for i in range(len(row)):
                row[i] = int(tmp_row[i])

        self.graph = carpet_matrix
        self.vertex = area

        color  =  area
        self.graphColouring(color)



    # is safe for vertex v
    def isSafe(self, v, colour, c):
        for i in range(self.vertex):
            if self.graph[v][i] == 1 and colour[i] == c:
                return False
        return True

    # A recursive utility function to solve m
    # coloring  problem
    def graphColourUtil(self, m, colour, v):
        if v == self.vertex:
            return True

        for c in range(1, m + 1):
            if self.isSafe(v, colour, c) == True:
                colour[v] = c
                if self.graphColourUtil(m, colour, v + 1) == True:
                    return True
                colour[v] = 0

    def graphColouring(self, m):
        colour = [0] * self.vertex
        if self.graphColourUtil(m, colour, 0) == False:
            return False

        uniqe_colors = set()
        for c in colour:
            if c in uniqe_colors:
                continue
            uniqe_colors.add(c)

        # Print the solution
        print("the least amount of color you need to color this carpet graph is : ")
        print(len(uniqe_colors))

        return True
