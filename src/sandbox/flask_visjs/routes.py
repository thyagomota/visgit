from app import app
from flask import render_template
from flask_visjs import Network

@app.route('/')
@app.route('/index')
def index():
    my_network = Network()

    # add some data
    my_network.add_node(1, label='First node', shape='box')
    my_network.add_node(2, title='Second node', shape='circle')
    my_network.add_node('third', title='Third node', shape='ellipse')

    # connect the nodes
    my_network.add_edge(1, 2)
    my_network.add_edge(2, 'third', value=2)
    my_network.add_edge('third', 1, title='Foo')

    return render_template('your_template.html.j2', graph=my_network)