"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()                                             # Creating q as a queue
        q.enqueue(starting_vertex)                              # Add starting vertex passed in

        visited_vertices = set()                                # Keep track of visited vertices using a set

        while q.size() > 0:                                     # while elements are present in the queue...

            current_vertex = q.dequeue()                            # ... dequeue the first vertex in the queue

            if current_vertex not in visited_vertices:              # ... if that dequeued vertex has not been visted yet...

                print(current_vertex)                                   # ... print it

                visited_vertices.add(current_vertex)                    # ... add it to the visited vertices

                for neighbor in self.get_neighbors(current_vertex):     # ... add the unvisited neighbors to the queue
                    if neighbor not in visited_vertices:
                        q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        q = Stack()                                                 # Creating q as a stack
        q.push(starting_vertex)                                     # Add starting vertex passed in

        visited_vertices = set()                                    # Keep track of visited vertices using a set

        while q.size() > 0:                                         # While elements are present in the stack...

            current_vertex = q.pop()                                    # Remove the first vertex from the stack

            if current_vertex not in visited_vertices:                  # ...if the removed vertex has not been visted yet...

                print(current_vertex)                                       # ... print it

                visited_vertices.add(current_vertex)                        # ... add it to the visited vertices

                for neighbor in self.get_neighbors(current_vertex):         # ... add the unvisited neighbors to the queue
                    if neighbor not in visited_vertices:
                        q.push(neighbor)

    def dft_recursive(self, starting_vertex, visited = None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        if visited == None:                                         # Inital Case
            visited = set()

        visited.add(starting_vertex)                                # Tracks visited vertices

        print(starting_vertex)                                      # Print vertex

        for neighbor in self.get_neighbors(starting_vertex):        # Recursively call function for neighbors
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()                                                 # Creating q as a queue
        q.enqueue([starting_vertex])                                # enqueue starting_vertex for path

        visited_vertices = set()                                    # Keep track of visited vertices using a set
        paths = []                                                  # Create list to track vertices for paths

        while q.size() > 0:                                         # While elements are present in the queue...

            path = q.dequeue()                                          # Dequeue the first vertex in path

            current_vertex = path[-1]                                   # Switch to last vertex in path
            
            if current_vertex not in visited_vertices:                  # ...if the current vertex has not been visted yet...

                if current_vertex == destination_vertex:                    # ... if it's the destination
                    return path                                                 # return the current path of vertices

                visited_vertices.add(current_vertex)                        # ... mark it as visited

                for neighbor in self.get_neighbors(current_vertex):         # ... create additional paths (based off current) with neighbors added
                    new_path = list(path)
                    new_path.append(neighbor)
                    q.enqueue(new_path)
                    
        return None

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        q = Stack()                                                         # Creating q as a stack
        q.push([starting_vertex])                                           # Add a starting vertex to it

        visited_vertices = set()                                            # Keep track of visited vertices using a set

        while q.size() > 0:                                                 # While elements are present in the stack...

            path = q.pop()                                                  # Remove the first vertex from the path

            current_vertex = path[-1]                                       # Switch to last vertex in path

            if current_vertex not in visited_vertices:                      # If the current index has been visted...

                if current_vertex == destination_vertex:                        # ... if it's the destination
                    return path                                                     # return the current path of vertices
                
                visited_vertices.add(current_vertex)                            # ... mark it as visited

                for neighbor in self.get_neighbors(current_vertex):             # ... create additional paths (based off current) with neighbors added
                    new_path = list(path)
                    new_path.append(neighbor)
                    q.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited = None, path = None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        This should be done using recursion.
        """
        if visited == None:                         # Initial Case
            visited = set()
        if path == None:
            path = []

        visited.add(starting_vertex)                # Track the visted vertices

        path = path + [starting_vertex]             # Add to current path

        if starting_vertex == destination_vertex:   # If at destination, return the current path
            return path

        for neighbor in self.get_neighbors(starting_vertex):    # Recursively call function on neighbors
            if neighbor not in visited:
                neighbor_path = self.dfs_recursive(neighbor, destination_vertex, visited, path) # ...searches for a path
                if neighbor_path:   #returns if there is a path
                    return neighbor_path


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
