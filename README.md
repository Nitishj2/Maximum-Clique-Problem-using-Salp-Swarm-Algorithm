<h1 align="center"> Ant Colony Optimization for Maximum Clique problem </h1>

Given an undirected graph, the objective of the Maximum Clique problem is to find a set of mutually adjacent vertices that contains the largest possible number of vertices. Many problems from various domains can be modeled as a Maximum Clique, such as social networks, bioinformatics, and network optimization. Due to its classification as an NP-Hard problem, various approaches are devised to seek approximate solutions. One such approach involves utilizing Ant Colony Optimization, which is implemented here.

The ant colony-based algorithm utilizes a population of virtual agents (the ants), to navigate the search space and uncover promising solutions. These ants gradually construct partial solutions (cliques) through probabilistic incremental method, and update pheromone trails proportionally to the quality of the solutions they build. Depositing pheromones on specific edges enhances the likelihood of those edges being selected when another agent is constructing a solution.

## Execution

The program can be executed using the following command line:

```bash
python main.py --config src/config/config.json
```

The scripts to run the experiments used to find optimal parameters are also provided:
```bash
python experiments.py
```

## Config File

An essential step for running the algorithm is to create a configuration file in JSON format, which includes the number of ants, number of iterations, pheromone evaporation rate, pheromone weight (alpha), path for dataset and for .txt file to save results. An example of a possible config file is shown below:


```json
{
    "ants_num": 30,
    "iterations": 100,
    "evaporation": 0.8,
    "alpha": 1,
    "file_path": "datasets/p_hat700-2.clq.txt",
    "results_path": "results/results.txt"
}
```
