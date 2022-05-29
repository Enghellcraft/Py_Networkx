from turtle import color
import networkx as nx
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = [11,8]
G = nx.Graph()

nodes = ['A','B','C','D','E','F','G','H','I']
edges = [('A','B',12),
('A','D',6),
('A','F',5),
('A','H',4),
('B','C',7),
('B','G',8),
('B','I',2),
('C','D',7),
('C','H',5),
('D','E',2),
('D','I',1),
('E','F',3),
('F','I',15),
('G','F',6),
('G','H',3),
('H','I',5)]

G.add_nodes_from(nodes)
G.add_weighted_edges_from(edges)

pos = nx.spring_layout(G) 
nx.draw_networkx_nodes(G, pos, node_color="turquoise", node_size=700)
nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')
nx.draw_networkx_edges(G, pos, width=4)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

Ma = nx.adjacency_matrix(G)
print(Ma.todense())

Mi = nx.incidence_matrix(G)
print(Mi.todense())

plt.show()