from turtle import color
import networkx as nx
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = [10,5]
G = nx.Graph()

nodes = ['A','B','C','D','E','F','G','H']
edges = [('A','B',4),       
('A','E',5),
('E','F',6),
('F','D',7),
('B','C',8),
('F','G',9),
('F','H',11)]

G.add_nodes_from(nodes)
G.add_weighted_edges_from(edges)

pos = nx.spring_layout(G) 
nx.draw_networkx_nodes(G, pos, node_color="turquoise", node_size=700)
nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')
nx.draw_networkx_edges(G, pos, width=4)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

print("El camino mas corto es: ", nx.algorithms.shortest_path(G, 'A', 'H'))

Ma = nx.adjacency_matrix(G)
print(Ma.todense())

Mi = nx.incidence_matrix(G)
print(Mi.todense())

plt.show()
