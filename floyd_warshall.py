# floyd_warshall.py

def floyd_warshall(matrix):
    """
    Алгоритм Флойда–Уоршелла для поиска кратчайших путей между всеми парами.
    matrix — квадратная матрица смежности (n x n), float('inf') если ребра нет, 0 на главной диагонали.
    Возвращает матрицу кратчайших расстояний.
    """
    n = len(matrix)
    # Копируем матрицу во избежание изменений оригинала
    dist = [row[:] for row in matrix]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # если путь через вершину k короче — обновляем
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist
