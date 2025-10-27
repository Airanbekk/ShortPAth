# main.py
from experiments import run_experiments
from visualization import plot_results, save_tables

def main():
    print("=== Benchmark: Dijkstra vs. Floyd–Warshall ===")
    
    # Запуск всех экспериментальных серий
    all_results = run_experiments()
    
    # Визуализация результатов (графики, таблицы)
    plot_results(all_results)
    save_tables(all_results)
    
    print("Анализ завершён! Все графики и таблицы сохранены в папке charts/.")

if __name__ == "__main__":
    main()
