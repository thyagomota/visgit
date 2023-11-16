import networkx as nx
import matplotlib.pyplot as plt

G = nx.gnm_random_graph(300, 200)
graph_pos = nx.spring_layout(G)

plt.figure(figsize=(5, 5))
nx.draw_networkx_nodes(G, graph_pos, node_size=10, node_color='blue', alpha=0.3)
nx.draw_networkx_edges(G, graph_pos)
nx.draw_networkx_labels(G, graph_pos, font_size=8, font_family='sans-serif')

plt.show()
