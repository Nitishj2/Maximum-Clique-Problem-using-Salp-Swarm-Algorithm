<h1 align="center"> Salp Swarm Algorithm for Maximum Clique problem </h1>

Given an undirected graph, the objective of the Maximum Clique problem is to find a set of mutually adjacent vertices that contains the largest possible number of vertices. Many problems from various domains can be modeled as a Maximum Clique, such as social networks, bioinformatics, and network optimization. Due to its classification as an NP-Hard problem, various approaches are devised to seek approximate solutions. One such approach involves utilizing Salp Swarm Algorithm, which is implemented here.

The Salp Swarm Algorithm (SSA) is a metaheuristic optimization algorithm inspired by the collective behavior of salps, a type of marine invertebrate. Salps exhibit swarm behavior in their movement patterns, which researchers have found applicable to solving optimization problems.

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

An essential step for running the algorithm is to create a configuration file in JSON format, which includes the number of salp, number of iterations, path for dataset and for .txt file to save results. An example of a possible config file is shown below:


```json
{
    "swarm_size": 50,
    "iterations": 50,
    "file_path": "datasets/test3.col.txt",
    "results_path": "results/results.txt"
}
```
