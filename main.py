from argparse import ArgumentParser
import json
import networkx as nx
import time
import matplotlib.pyplot as plt
from src.ssa import SalpSwarmOptimizer
from src.graph import Graph

def parse_args():
    parser = ArgumentParser()
    parser.add_argument("--config", required=True, type=str, help="Name of json file with config")
    return parser.parse_args()

def read_graph(file_path):
    return Graph(file_path)

def plot_initial_graph(graph):
    G = nx.Graph()
    for u in graph.get_vertices():
        neighbors = graph.get_neighbor_edges(u)
        for edge in neighbors:
            v = edge.get_vertex()
            G.add_edge(u, v)
    
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray')
    plt.title('Initial Graph')
    plt.show()

def plot_graph_with_clique(graph, clique_vertices):
    G = nx.Graph()
    for u in graph.get_vertices():
        neighbors = graph.get_neighbor_edges(u)
        for edge in neighbors:
            v = edge.get_vertex()
            G.add_edge(u, v)
    
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray')

    nx.draw_networkx_nodes(G, pos, nodelist=clique_vertices, node_color='red')
    clique_edges = [(clique_vertices[i], clique_vertices[j]) for i in range(len(clique_vertices)) for j in range(i+1, len(clique_vertices)) if graph.has_edge(clique_vertices[i], clique_vertices[j])]
    nx.draw_networkx_edges(G, pos, edgelist=clique_edges, edge_color='red')

    plt.title('Graph with Maximum Clique Highlighted')
    plt.show()

def parse_output(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    clique_size_line = lines[-2].strip()
    clique_vertices_line = lines[-1].strip()

    clique_size = int(clique_size_line.split('=')[-1])
    clique_vertices = list(map(int, clique_vertices_line.split(':')[-1].strip().split()))

    return clique_size, clique_vertices

if __name__ == '__main__':
    args = parse_args()

    with open(args.config) as f:
        config_args = json.load(f)

    start_time = time.time()  # Record start time
 
    ssa = SalpSwarmOptimizer(config_args)
    ssa.run()  # Run the SSA optimizer
    ssa.results.write_results(1)  # Write the results
    
    #execution time
    end_time = time.time()  # Record end time

    execution_time = end_time - start_time
    print("Execution time: {:.2f} seconds".format(execution_time))

    # Plotting the graphs
    graph = read_graph(config_args['file_path'])
    plot_initial_graph(graph)

    clique_size, clique_vertices = parse_output(config_args['results_path'])
    plot_graph_with_clique(graph, clique_vertices)
