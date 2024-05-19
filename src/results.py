import numpy as np

class Results:
    def __init__(self, config_args) -> None:
        self.results_path = config_args['results_path']
        self.iterations = config_args['iterations']
        # For each iteration, keep the mean size of the best clique found
        self.sizes = np.zeros(self.iterations) 
        self.best_clique = None
    
    def update_results(self, iteration, best_clique_size):
        self.sizes[iteration] += best_clique_size
    
    def update_best_clique(self, best_clique):
        if not self.best_clique:
            self.best_clique = best_clique
        else:
            if best_clique.get_size() > self.best_clique.get_size():
                self.best_clique = best_clique
    
    def write_results(self, exec_num):
        # Get mean of best sizes for each iteration
        self.sizes = self.sizes / exec_num
        np.savetxt(self.results_path, self.sizes, newline=' ', fmt='%.2f')

        # Write Best Clique Found.
        clique_repr = self.best_clique.get_repr()
        with open(self.results_path, 'a') as file:
            file.write(clique_repr)
