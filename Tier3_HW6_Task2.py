import networkx as nx

# Граф, створений у першому завданні
social_network = nx.Graph()
social_network.add_nodes_from([
    "User1", "User2", "User3", "User4", "User5",
    "User6", "User7", "User8", "User9", "User10"
])
social_network.add_edges_from([
    ("User1", "User2"), ("User1", "User3"), ("User1", "User4"),
    ("User2", "User5"), ("User2", "User6"), ("User3", "User7"),
    ("User4", "User8"), ("User5", "User9"), ("User6", "User10"),
    ("User7", "User10"), ("User8", "User9"), ("User9", "User10"), 
    ("User1", "User10")
])

# Знаходження шляхів за допомогою DFS
dfs_paths = list(nx.dfs_edges(social_network, source="User1"))
print("Шляхи за допомогою DFS:", dfs_paths)

# Знаходження шляхів за допомогою BFS
bfs_paths = list(nx.bfs_edges(social_network, source="User1"))
print("Шляхи за допомогою BFS:", bfs_paths)
