def get_graph_size(file_path):
    with open(file_path, 'r') as file:
        for line in file.readlines():
            line = line.strip()
            if line.startswith('p'):
                _, _, N, _ = line.split()
                break
    return int(N)


class Edge:
    def __init__(self, v):
        self.v = v
    
    def get_vertex(self):
        return self.v


# Graph as Adjacency Matrix.
class Graph:
    def __init__(self, file_path):
        N = get_graph_size(file_path)
        self.vertices = {}

        for u in range(1, N + 1):
            self.vertices[u] = []

        with open(file_path, 'r') as file:
            for line in file.readlines():
                line = line.strip()
                if line.startswith('e'):
                    _, v1, v2 = line.split(' ')
                    v1 = int(v1)
                    v2 = int(v2)
                    self.vertices[v1].append(Edge(v2))
                    self.vertices[v2].append(Edge(v1))
    
    def get_edge(self, u, v):
        for edge in self.vertices[u]:
            if edge.get_vertex() == v: 
                return edge
    
    def get_vertices(self):
        return list(self.vertices.keys())

    def get_neighbor_edges(self, vertex):
        return [edge for edge in self.vertices[vertex]]
    
    # Verify if there is an edge between vertices v1 and v2
    def has_edge(self, v1, v2):
        for edge in self.vertices[v1]:
            if edge.get_vertex() == v2: 
                return True
        return False
