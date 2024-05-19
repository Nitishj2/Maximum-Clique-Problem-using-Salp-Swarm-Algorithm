import random
import numpy as np

class Candidate:
    def __init__(self, edge) :
        self.edge = edge
    
    def __repr__(self) -> str:
        return f'Vertex {self.edge.get_vertex()}'
    
    def items(self):
        return self.edge
    
    def get_edge(self):
        return self.edge


class Clique:
    def __init__(self, graph):
        self.graph = graph
        self.vertices = []
        self.size = 0
        self.positions = []

    def get_repr(self) -> str:
        repr = f'\nClique: k={self.get_size()}\nVertices: '
        for v in self.vertices:
            repr += f'{v} '
        return repr
    
    def get_size(self):
        return self.size

    def get_vertices(self):
        return self.vertices

    def get_edges(self):
        size = self.get_size()
        edges = []
        for i in range(size):
            for j in range (i+1, size):
                edges.append( (self.vertices[i], self.vertices[j]) )
        return edges
    
    def get_random_vertex(self):
        return random.choice(self.graph.get_vertices())

    def construct_random_clique(self):
        u = self.get_random_vertex()
        self.vertices.append(u)
        self.size += 1

        neighbors = self.graph.get_neighbor_edges(u)

        candidates = [Candidate(edge) for edge in neighbors]

        while candidates:
            chosen = random.choice(candidates)

            edge = chosen.get_edge()
            v = edge.get_vertex()
            self.vertices.append(v)
            self.size += 1

            candidates.remove(chosen)
            self.update_candidates(candidates, v)
    
    def update_candidates(self, candidates, v1):
        candidates_copy = list(candidates)
        for candidate in candidates_copy:
            edge = candidate.get_edge()
            v2 = edge.get_vertex()
            if not self.graph.has_edge(v1, v2): 
                candidates.remove(candidate)
    
    def set_position(self, positions):
        self.positions = positions
    
    def get_positions(self):
        return self.positions

    def update_position(self, leader_position, food_position, c1, c2):
        new_position = leader_position + c1 * (food_position - leader_position) + c2 * (food_position - leader_position)
        self.set_position(new_position)
