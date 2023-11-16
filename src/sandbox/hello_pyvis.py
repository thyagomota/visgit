from pyvis.network import Network
import webbrowser

g = Network()
g.add_node(0)
g.add_node(1)
g.add_edge(0, 1)
g.show('basic.html', notebook=False)
webbrowser.get("/Applications/Microsoft\ Edge.app/Contents/MacOS/Microsoft\ Edge").open('basic.html')