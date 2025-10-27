# experiments.py
import time
import numpy as np
from graph_generator import generate_random_graph, matrix_to_adj_list
from dijkstra import dijkstra_all_pairs
from floyd_warshall import floyd_warshall
from utils import measure_memory

def run_experiments():
    """
    Основная функция запускает весь спектр экспериментов:
    — Перебор разных размеров и плотностей графов
    — Многократные прогоны (усреднение)
    — Замеры времени и памяти
    — Подготовка результатов для визуализации
    """
    results = []
    sizes = [10, 50, 100]
    densities = [0.1, 0.3, 0.7]
    repeats = 3

    for n in sizes:
        for density in densities:
            times_dijkstra = []
            times_fw = []
            mem_dijkstra = []
            mem_fw = []
            for _ in range(repeats):
                matrix = generate_random_graph(n, density=density)
                adj_list = matrix_to_adj_list(matrix)

                # Dijkstra
                t0 = time.perf_counter()
                mem_usage_dijkstra = measure_memory(lambda: dijkstra_all_pairs(adj_list))
                t1 = time.perf_counter()
                times_dijkstra.append(t1 - t0)
                mem_dijkstra.append(mem_usage_dijkstra)

                # Floyd–Warshall
                t2 = time.perf_counter()
                mem_usage_fw = measure_memory(lambda: floyd_warshall(matrix))
                t3 = time.perf_counter()
                times_fw.append(t3 - t2)
                mem_fw.append(mem_usage_fw)

            results.append({
                'n': n,
                'density': density,
                'dijkstra_time_mean': np.mean(times_dijkstra),
                'dijkstra_time_std': np.std(times_dijkstra),
                'fw_time_mean': np.mean(times_fw),
                'fw_time_std': np.std(times_fw),
                'dijkstra_mem_mean': np.mean(mem_dijkstra),
                'fw_mem_mean': np.mean(mem_fw),
            })
            print(f"Граф {n} узлов, плотность {density}: Dijkstra {np.mean(times_dijkstra):.4f}s, FW {np.mean(times_fw):.4f}s")
    return results
