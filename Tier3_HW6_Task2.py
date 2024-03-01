from collections import deque

# Створення графа як словника
social_network = {
    "User1": ["User2", "User3", "User4", "User10"],
    "User2": ["User1", "User5", "User6"],
    "User3": ["User1", "User7"],
    "User4": ["User1", "User8"],
    "User5": ["User2", "User9"],
    "User6": ["User2", "User10"],
    "User7": ["User3", "User10"],
    "User8": ["User4", "User9"],
    "User9": ["User5", "User8", "User10"],
    "User10": ["User6", "User7", "User9", "User1"]
}

# Реалізація DFS
def dfs(graph, start):
    visited = set()
    path = []

    def dfs_recursive(vertex):
        if vertex not in visited:
            visited.add(vertex)
            path.append(vertex)
            for neighbor in graph[vertex]:
                dfs_recursive(neighbor)

    dfs_recursive(start)
    return path

# Реалізація BFS
def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    path = []

    while queue:
        vertex = queue.popleft()
        path.append(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return path
# Знаходження шляхів за допомогою DFS
dfs_path = dfs(social_network, "User1")
print("Шляхи за допомогою DFS:", dfs_path)

# Знаходження шляхів за допомогою BFS
bfs_path = bfs(social_network, "User1")
print("Шляхи за допомогою BFS:", bfs_path)
