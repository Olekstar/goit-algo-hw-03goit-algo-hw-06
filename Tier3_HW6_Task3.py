import networkx as nx

# Граф, створений у першому завданні
social_network = nx.Graph()
social_network.add_nodes_from([
    "User1", "User2", "User3", "User4", "User5",
    "User6", "User7", "User8", "User9", "User10"
])
social_network.add_edges_from([
    ("User1", "User2", {'weight': 2}), ("User1", "User3", {'weight': 2}), ("User1", "User4", {'weight': 7}),
    ("User2", "User5", {'weight': 3}), ("User2", "User6", {'weight': 1}), ("User3", "User7", {'weight': 2}),
    ("User4", "User8", {'weight': 5}), ("User5", "User9", {'weight': 4}), ("User6", "User10", {'weight': 1}),
    ("User7", "User10", {'weight': 1}), ("User8", "User9", {'weight': 8}), ("User9", "User10", {'weight': 1}),
    ("User1", "User10", {'weight': 2})
])

# Знаходження найкоротших шляхів між всіма вершинами графа
shortest_paths = dict(nx.all_pairs_dijkstra_path(social_network))

# Виведення результатів
for source in shortest_paths:
    print(f"Найкоротші шляхи для вершини {source}:")
    for target in shortest_paths[source]:
        path = shortest_paths[source][target]
        length = nx.shortest_path_length(social_network, source=source, target=target, weight='weight')
        print(f"{source} -> {target}: {path} (довжина: {length})")
