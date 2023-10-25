"""
A simple graph in plotly
"""

import plotly.graph_objects as go
import networkx as nx

fig = go.Figure(go.Scatter(x=[0], y=[0], mode='markers', marker=dict(size=20)))
fig.show()