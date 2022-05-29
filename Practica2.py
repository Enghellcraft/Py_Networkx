from turtle import color
import networkx as nx
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = [10,5]
G = nx.Graph()
nodes = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n']
edges = [
('a','b',6),
('a','c',9),
('a','d',3),
('b','c',10),
('d','c',4),
('b','e',12),
('c','e',3),
('f','e',8),
('c','f',2),
('d','f',15),
('d','g',10),
('e','h',4),
('e','i',11),
('g','f',9),
('g','j',13),
('f','i',10),
('i','h',7),
('i','l',11),
('i','j',15),
('h','k',20),
('j','m',9),
('l','k',13),
('l','n',12),
('l','m',5),
('m','n',5),
('k','n',6)]

G.add_nodes_from(nodes)
G.add_weighted_edges_from(edges)

pos = nx.spring_layout(G) 
nx.draw_networkx_nodes(G, pos, node_color="turquoise", node_size=700)
nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')
nx.draw_networkx_edges(G, pos, width=4)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

print("Ruta mas barata: ", nx.algorithms.shortest_path(G, 'a', 'n'))

print(f"Radio: {nx.radius(G)}")
print(f"Diámetro: {nx.diameter(G)}")
print(f"Excentricidad: {nx.eccentricity(G)}")
print(f"Centro: {nx.center(G)}")
print(f"Periferia: {nx.periphery(G)}")
print(f"Densidad: {nx.density(G)}" )

Ma = nx.adjacency_matrix(G)
print(Ma.todense())

Mi = nx.incidence_matrix(G)
print(Mi.todense())

plt.show()


