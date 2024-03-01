import heapq

# Визначення графа з вагами ребер
graph = {
    "User1": {"User2": 2, "User3": 2, "User4": 7, "User10": 2},
    "User2": {"User1": 2, "User5": 3, "User6": 1},
    "User3": {"User1": 2, "User7": 2},
    "User4": {"User1": 7, "User8": 5},
    "User5": {"User2": 3, "User9": 4},
    "User6": {"User2": 1, "User10": 1},
    "User7": {"User3": 2, "User10": 1},
    "User8": {"User4": 5, "User9": 8},
    "User9": {"User5": 4, "User8": 8, "User10": 1},
    "User10": {"User1": 2, "User6": 1, "User7": 1, "User9": 1}
}

# Реалізація алгоритму Дейкстри
def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    previous_vertices = {vertex: None for vertex in graph}
    pq = [(0, start)]

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)

        # Оновлення відстаней для сусідів
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_vertices[neighbor] = current_vertex
                heapq.heappush(pq, (distance, neighbor))

    return distances, previous_vertices

# Пошук шляху
def reconstruct_path(start, end, previous_vertices):
    path = []
    current_vertex = end
    while current_vertex != start:
        path.append(current_vertex)
        current_vertex = previous_vertices[current_vertex]
    path.append(start)
    path.reverse()
    return path

# Запускаємо алгоритм Дейкстри з User1
shortest_distances, previous_vertices = dijkstra(graph, "User1")
paths = {vertex: reconstruct_path("User1", vertex, previous_vertices) for vertex in graph}

print("Найкоротші відстані від User1 до інших вершин:")
for vertex, distance in shortest_distances.items():
    print(f"До {vertex}: {distance}")

print("\nНайкоротші шляхи від User1 до інших вершин:")
for vertex, path in paths.items():
    print(f"Шлях до {vertex}: {' -> '.join(path)}")
