from turtle import color
import networkx as nx
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = [5,5]

Gra = nx.Graph()
nodes = ['Z','E','F','C','D','G','B','A']
edges = [('Z','F',2),
('Z','E',3),
('Z','C',1),
('C','F',1),
('E','F',1),
('E','D',2),
('C','B',5),
('D','G',1),
('B','G',1),
('D','A',5),
('B','A',4),
('G','A',2)]

Gra.add_nodes_from(nodes)
Gra.add_weighted_edges_from(edges)

pos = nx.shell_layout(Gra) 
nx.draw_networkx_nodes(Gra, pos, node_color="turquoise", node_size=700)
nx.draw_networkx_labels(Gra, pos, font_size=10, font_family='sans-serif')
nx.draw_networkx_edges(Gra, pos, width=4)
labels = nx.get_edge_attributes(Gra, 'weight')
nx.draw_networkx_edge_labels(Gra, pos, edge_labels=labels)


print("Ruta mas corta usando el algoritmo de Dijkstra entre Z y A: ", nx.algorithms.shortest_path(Gra, 'Z', 'A'))

Ma = nx.adjacency_matrix(Gra)
print(Ma.todense())

Mi = nx.incidence_matrix(Gra)
print(Mi.todense())


plt.axis('off')
plt.show()


