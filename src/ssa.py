from src.graph import Graph
from src.clique import Clique
from src.results import Results
import random
import numpy as np

class Salp:
    def __init__(self, graph):
        self.clique = Clique(graph)  # Alpha is not used in SSA
    
    def construct_random_clique(self):
        self.clique.construct_random_clique()
    
    def get_clique_size(self):
        return self.clique.get_size()

    def get_clique(self):
        return self.clique
    
    def update_position(self, leader_position, food_position, c1, c2):
        new_position = leader_position + c1 * (food_position - leader_position) + c2 * (food_position - leader_position)
        self.clique.set_position(new_position)

class SalpSwarmOptimizer:
    def __init__(self, config_args):
        self.graph = Graph(config_args['file_path'])
        self.swarm_size = config_args['swarm_size']  # Update to use 'swarm_size' key
        self.iterations = config_args['iterations']
        self.results = Results(config_args)
        self.alpha = 1  # Example SSA parameter
        self.positions = np.zeros((self.swarm_size, len(self.graph.get_vertices())))

    
    def run(self):
        it = 0
        best_clique_size = 0
        best_clique = None

        salps = [Salp(self.graph) for _ in range(self.swarm_size)]
        for salp in salps:
            salp.construct_random_clique()

        while it < self.iterations:
            best_cycle_clique_size = 0
            food_position = None

            for salp in salps:
                size = salp.get_clique_size()
                if size > best_cycle_clique_size:
                    best_cycle_clique = salp.get_clique()
                    best_cycle_clique_size = size

            if best_cycle_clique_size > best_clique_size:
                best_clique = best_cycle_clique
                best_clique_size = best_cycle_clique_size
            
            print(f'Iteration {it}: Best Clique k = {best_cycle_clique_size}')
            
            c1 = 2 * np.exp(-4 * (it / self.iterations)**2)
            c2 = random.uniform(0, 1)
            leader_position = np.array(best_cycle_clique.get_positions())
            food_position = leader_position  # in SSA, food is the best solution

            for salp in salps:
                salp.update_position(leader_position, food_position, c1, c2)

            self.results.update_results(it, best_clique_size)
            it += 1

        self.results.update_best_clique(best_clique)
        print(f'\nBest Clique Found: k = {best_clique_size}')

