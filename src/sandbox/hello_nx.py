"""
A simple graph in networkx
"""

# import plotly.graph_objects as go
import networkx as nx
import matplotlib.pyplot as plt

# defining my node data
node_data = {
    'c0': {
        'branch': 'main'
    }, 
    'c1': {
        'branch': 'main'
    }, 
    'c2': {
        'branch': 'dev'
    }
}

# create a graph from node_data
G = nx.Graph()
for key in node_data:
    G.add_node(key, **node_data[key])

# G = nx.Graph()
# G.add_node("c0000")
# G.add_node("c1")
# node_sizes = [len(str(label)) * 300 for label in G.nodes()]
# subset_key = [x for x in range(1, len(G.nodes)+1)]

# G.add_edge(c1, c0)

#pos = nx.spring_layout(G)
# pos = nx.kamada_kawai_layout(G)
# pos = nx.planar_layout(G)
pos = nx.multipartite_layout(G, subset_key='branch', align='vertical')

options = {
    'font_family': 'Arial',
    'font_size': 12
}

# options = {
#     "font_size": 12,
#     "node_size": 1000,
#     "node_color": "white",
#     "edgecolors": "black",
#     # "linewidths": 5,
#     "width": 5
# }

nx.draw_networkx(G, pos, **options)
plt.show()