from turtle import color
import networkx as nx
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = [11,8]
G = nx.Graph()

nodes = ['A','B','C','D','E','F','G','H','I']
edges = [('A','B',20),
('A','F',34),
('A','I',45),
('B','C',20),
('B','F',10),
('B','I',26),
('C','D',28),
('C','I',22),
('D','G',18),
('D','H',19),
('D','I',13),
('E','F',22),
('E','G',12),
('E','H',25),
('F','G',30),
('F','I',12),
('G','H',16),
('G','I',14),
('H','I',32),
('A','H',68)]

G.add_nodes_from(nodes)
G.add_weighted_edges_from(edges)

pos = nx.spring_layout(G) 
nx.draw_networkx_nodes(G, pos, node_color="turquoise", node_size=700)
nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')
nx.draw_networkx_edges(G, pos, width=4)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

dict_shortpath = dict(nx.all_pairs_shortest_path(G))['A']
print(f"El camino mas corto de A a todos los destinos es:\n {dict_shortpath}")

for i in nodes:
    print(f"El camino de 'A' a {i} es de: {nx.shortest_path_length(G, 'A', i)}")
print(f"El camino de 'B' a 'G' es de: {nx.shortest_path_length(G, 'B', 'G')}")   
print(f"El camino mas corto de 'B' a 'G' es de: {nx.shortest_path(G, 'B', 'G')}")

Ma = nx.adjacency_matrix(G)
print(Ma.todense())

Mi = nx.incidence_matrix(G)
print(Mi.todense())

plt.show()