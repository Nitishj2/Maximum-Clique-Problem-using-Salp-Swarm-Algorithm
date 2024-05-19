from src.ssa import SalpSwarmOptimizer
import multiprocessing

EXEC_NUM = 30

FILE_PATH = "datasets/brock800_4.clq.txt"
RESULTS_ROOT = "results_brock"

def test_swarm_size(swarm_size):
    result_path = f'{RESULTS_ROOT}/600it{swarm_size}swarm.txt'
    config_args = {
        "swarm_size": swarm_size,
        "iterations": 600,
        "file_path": FILE_PATH,
        "results_path": result_path
    }
    
    ssa = SalpSwarmOptimizer(config_args)

    print(f'\nExecuting {EXEC_NUM} times for swarm_size={swarm_size}')
    for i in range(EXEC_NUM):
        print(f'Execution {i}')
        ssa.run()
    
    ssa.results.write_results(EXEC_NUM)


def test_iterations_rho(iterations_rho):
    iterations, rho = iterations_rho

    result_path = f'{RESULTS_ROOT}/iterations{iterations}rho{rho}.txt'
    config_args = {
        "swarm_size": 30,
        "iterations": iterations,
        "file_path": FILE_PATH,
        "results_path": result_path
    }
    
    ssa = SalpSwarmOptimizer(config_args)

    print(f'\nExecuting {EXEC_NUM} times for iterations={iterations}, rho={rho}')
    for i in range(EXEC_NUM):
        print(f'Execution {i}')
        ssa.run()
    
    ssa.results.write_results(EXEC_NUM)


if __name__ == '__main__':
    swarm_sizes = [5, 10, 15, 20, 30]
    iterations_rho_list = [(400, 0.80), (400, 0.90), (400, 0.99), (600, 0.80), (600, 0.90), (600, 0.99)]

    with multiprocessing.Pool() as pool:
        pool.map(test_swarm_size, swarm_sizes)
        pool.map(test_iterations_rho, iterations_rho_list)
