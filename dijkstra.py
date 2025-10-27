# dijkstra.py
import heapq

def dijkstra(adj_list, start):
    """
    Алгоритм Дейкстры для графа, заданного как список смежности.
    adj_list — dict: vertex -> {neighbor: weight, ...}
    start — начальная вершина (int или str)
    Возвращает dict: вершина -> кратчайшее расстояние от start
    """
    distances = {vertex: float('inf') for vertex in adj_list}
    distances[start] = 0
    pq = [(0, start)]  # очередь приоритетов: (текущее расстояние, вершина)

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in adj_list[current_vertex].items():
            if weight < 0:
                # Dijkstra не работает с отрицательными весами!
                continue
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return distances

def dijkstra_all_pairs(adj_list):
    """
    Запускает Дейкстру для всех вершин как начальных (получаем "все-ко-всем").
    """
    results = {}
    for start in adj_list:
        results[start] = dijkstra(adj_list, start)
    return results
