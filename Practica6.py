from turtle import color
import networkx as nx
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = [11,8]
G = nx.Graph()

nodes = ['A','B','C','D','E','F','G','H','I','J','K','L']
edges = [('A','B', 2),
('A','C', 6),
('A','K', 7),
('B','D', 7),
('B','F', 11), 
('B','G', 13), 
('C','D', 2), 
('C','G', 12), 
('D','I', 14), 
('D','J', 12),
('E','F', 4),
('E','L', 14),
('F','J', 10),
('G','I', 8),
('H','I', 3),
('J','L', 9)]

G.add_nodes_from(nodes)
G.add_weighted_edges_from(edges)

pos = nx.spring_layout(G) 
nx.draw_networkx_nodes(G, pos, node_color="turquoise", node_size=700)
nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')
nx.draw_networkx_edges(G, pos, width=4)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

if (nx.shortest_path_length(G,'A','B'))==1:
    print(f"Es posible el par A y B ")
else:
    print(f"NO es posible el par A y B ")
if (nx.shortest_path_length(G,'C','D'))==1:
    print(f"Es posible el par C y D ")
else:
    print(f"NO es posible el par C y D ")
if (nx.shortest_path_length(G,'E','F'))==1:
    print(f"Es posible el par E y F ")
else:
    print(f"NO es posible el par E y F  ")
if (nx.shortest_path_length(G,'G','H'))==1:
    print(f"Es posible el par G y H ")
else:
    print(f"NO es posible el par G y H ")
if (nx.shortest_path_length(G,'I','J'))==1:
    print(f"Es posible el par I y J ")
else:
    print(f"NO es posible el par I y J ")
if (nx.shortest_path_length(G,'K','L'))==1:
    print(f"Es posible el par K y L ")
else:
    print(f"NO es posible el par K y L ")

print(f"El camino mas corto de 'A' a 'J' es de: {nx.shortest_path(G, 'A', 'J')}")
print(f"El camino de 'A' a 'J' es de: {nx.shortest_path_length(G, 'A', 'J')}")   

Ma = nx.adjacency_matrix(G)
print(Ma.todense())

Mi = nx.incidence_matrix(G)
print(Mi.todense())

plt.show()
