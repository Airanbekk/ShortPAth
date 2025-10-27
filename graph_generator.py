# graph_generator.py
import random
import csv

def generate_random_graph(n, density=0.3, min_weight=1, max_weight=10, directed=True, allow_negative=False):
    """
    Генерирует случайный граф как матрицу смежности.
    n — количество вершин
    density — доля возможных рёбер (от 0 до 1)
    min_weight, max_weight — диапазон весов рёбер
    directed — флаг направленности
    allow_negative — разрешить ли отрицательные веса
    """
    matrix = [[float('inf') for _ in range(n)] for _ in range(n)]
    for i in range(n):
        matrix[i][i] = 0  # на себя всегда 0
        for j in range(n):
            if i != j and random.random() < density:
                weight = random.randint(min_weight, max_weight)
                if allow_negative and random.random() < 0.1:
                    weight *= -1
                matrix[i][j] = weight
                if not directed:
                    matrix[j][i] = weight
    return matrix

def matrix_to_adj_list(matrix):
    """
    Преобразует матрицу смежности в список смежности (для Дейкстры).
    """
    n = len(matrix)
    adj_list = {}
    for i in range(n):
        adj_list[i] = {}
        for j in range(n):
            if matrix[i][j] != float('inf') and matrix[i][j] != 0:
                adj_list[i][j] = matrix[i][j]
    return adj_list

def load_graph_from_csv(filename):
    """
    Загружает граф из csv-файла вида: строка=source, столбцы=target, value=вес
    """
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        matrix = [list(map(float, row)) for row in reader]
    return matrix

# Можно добавить генераторы для спец. случаев: полные графы, разреженные, с особыми паттернами и пр.
