# visualization.py
import matplotlib.pyplot as plt
import pandas as pd
import os

def plot_results(results):
    print("plot_results запущен, результатов: ", len(results))

    """
    Строит графики: время работы и память по размерам графа и плотности.
    """
    if not os.path.exists('charts'):
        os.makedirs('charts')
    df = pd.DataFrame(results)
    print("plot_results запущен, результатов: ", len(results))


    # Время выполнения
    for density in sorted(df['density'].unique()):
        sub = df[df['density'] == density]
        plt.figure()
        plt.plot(sub['n'], sub['dijkstra_time_mean'], label='Dijkstra')
        plt.plot(sub['n'], sub['fw_time_mean'], label='Floyd–Warshall')
        plt.xlabel('Количество вершин')
        plt.ylabel('Время (сек.)')
        plt.title(f'Время на графах с плотностью {density}')
        plt.legend()
        plt.grid()
        plt.savefig(f'charts/time_density_{density}.png')
        print(f"Сохранил график: charts/time_density_{density}.png")
    
        plt.close()

    # Память
    for density in sorted(df['density'].unique()):
        sub = df[df['density'] == density]
        plt.figure()
        plt.plot(sub['n'], sub['dijkstra_mem_mean'], label='Dijkstra')
        plt.plot(sub['n'], sub['fw_mem_mean'], label='Floyd–Warshall')
        plt.xlabel('Количество вершин')
        plt.ylabel('Память (байт)')
        plt.title(f'Память на графах с плотностью {density}')
        plt.legend()
        plt.grid()
        plt.savefig(f'charts/memory_density_{density}.png')
        print(f"Сохранил график: charts/time_density_{density}.png")

        plt.close()

def save_tables(results):
    """
    Сохраняет таблицу с результатами экспериментов (csv/xlsx).
    """
    df = pd.DataFrame(results)
    df.to_csv('charts/experiment_results.csv', index=False)
    df.to_excel('charts/experiment_results.xlsx', index=False)
