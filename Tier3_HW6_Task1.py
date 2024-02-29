import networkx as nx
import matplotlib.pyplot as plt

# Створення пустого графа
social_network = nx.Graph()

# Додавання вершин (користувачів)
social_network.add_nodes_from([
    "User1", "User2", "User3", "User4", "User5",
    "User6", "User7", "User8", "User9", "User10"
])

# Додавання зв'язків між користувачами
social_network.add_edges_from([
    ("User1", "User2"), ("User1", "User3"), ("User1", "User4"),
    ("User2", "User5"), ("User2", "User6"), ("User3", "User7"),
    ("User4", "User8"), ("User5", "User9"), ("User6", "User10"),
    ("User7", "User10"), ("User8", "User9"), ("User9", "User10"),
    ("User1", "User10")
])

# Візуалізація графа
nx.draw(social_network, with_labels=True, node_color='skyblue', node_size=1500, font_size=10, font_weight='bold')
plt.title("Соціальна мережа користувачів")
plt.show()

# Аналіз основних характеристик графа
print("Кількість вершин:", social_network.number_of_nodes())
print("Кількість ребер:", social_network.number_of_edges())
print("Ступінь вершин:")
for node in social_network.nodes():
    print(node, ":", social_network.degree[node])