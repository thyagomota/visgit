# https://networkx.org/
# https://pyvis.readthedocs.io/en/latest/tutorial.html
# https://visjs.github.io/vis-network/docs/network/

# import networkx as nx
# from pyvis.network import Network

# G = nx.DiGraph()
# G.add_nodes_from([1, 2, 3, 4, 5, 6, 7 ])
# G.add_edge(1, to="2")
# G.add_edge(2, 3)
# G.add_edge(3, 4)
# G.add_edge(4, 5)
# G.add_edge(2, 6)
# G.add_edge(6, 7)
# graph = Network()
# graph.from_nx(G)

# graph.set_options("""
# {
#   "layout": {
#     "hierarchical": {
#       "enabled": true,
#       "direction": "LR",
#       "sortMethod": "directed"
#     }
#   }
# }
# """)

# graph.show('nx.html', notebook=False)

from pyvis.network import Network

G = Network(directed=True)
G.add_nodes([1, 2, 3, 4, 5, 6, 7 ])
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(3, 4)
G.add_edge(4, 5)
G.add_edge(2, 6)
G.add_edge(6, 7)

G.set_options("""
{
  "layout": {
    "hierarchical": {
      "enabled": true,
      "direction": "LR",
      "sortMethod": "directed"
    }
  }
}
""")
G.show('nx.html', notebook=False)