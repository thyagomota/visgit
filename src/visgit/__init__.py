'''
A bit branch tree visualizer web app for educational purposes. 
'''

from flask import Flask, render_template, session, request
from flask_visjs import VisJS4, Network
import networkx as nx
import uuid
import os
import shutil
from visgit import pygit

app = Flask(__name__)
app.secret_key = 'hide at all costs!'

VisJS4().init_app(app)

REPOS = os.path.join(os.getcwd(), 'visgit/repos/')

@app.route('/', methods=['GET'])
def index():
    # creates a user, commit-related info, and git repository if one cannot be found associated to the current session
    if 'user_id' not in session:
        user_id = str(uuid.uuid4())
        session['user_id'] = user_id
        session['commits'] = {}
        session['next_commit'] = 1
        if not os.path.exists(os.path.join(REPOS, f'{user_id}')):
            os.mkdir(os.path.join(REPOS, f'{user_id}'))
        else:
            shutil.rmtree(os.path.join(REPOS, f'{user_id}'), ignore_errors=True)
        os.chdir(os.path.join(REPOS, f'{user_id}'))
        pygit.init()
    # if a user can be found associated to the current session, just set the working directory to the user's repo
    else: 
        os.chdir(os.path.join(REPOS, f"{session['user_id']}"))

    # evaluate the command
    command = request.args.get('command')
    if command: 
        if command == 'commit':
            pygit.commit()
            commit = pygit.head()
            session['commits'][commit] = session['next_commit']
            session['next_commit'] += 1
        elif command.startswith('checkout'): 
            try: 
                data = command.split(' ')
                if len(data) == 2:
                    _, branch = data
                    branch = branch.strip()
                    pygit.checkout(branch)
                elif len(data) == 3:
                    _, create, branch = data
                    if create.strip() == '-b':
                        pygit.checkout(branch.strip(), create=True)
            except: 
                pass
        elif command.startswith('merge'):
            try: 
                data = command.split(' ')
                if len(data) == 2:
                    _, branch = data
                    branch = branch.strip()
                    pygit.merge(branch)
                    commit = pygit.head()
                    session['commits'][commit] = session['next_commit']
                    session['next_commit'] += 1
            except: 
                pass  
        elif command == 'init':
            os.chdir(REPOS)
            shutil.rmtree(os.path.join(REPOS, f"{session['user_id']}"), ignore_errors=True)
            os.mkdir(os.path.join(REPOS, f"{session['user_id']}"))
            os.chdir(os.path.join(REPOS, f"{session['user_id']}"))
            pygit.init()
            session['commits'] = {}
            session['next_commit'] = 1

    # create the graph
    graph = Network(directed=True)
    graph.options = {  
            "layout": {
                "hierarchical": {
                "enabled": True,
                "direction": "LR",
                "sortMethod": "directed"
                }
            },      
            "edges": {
                "color": {
                    "inherit": False
                }
            }
        }

    head = ''
    try: 
        head = pygit.head()
    except: 
        pass
    
    current_branch = pygit.current_branch()
    previous = None
    if current_branch:
        for commit in pygit.log(current_branch.strip().removeprefix('* ')):
            commit_number = session['commits'][commit]
            if commit == head: 
                graph.add_node(commit_number, label=f'c{commit_number}', shape='ellipse', color='#ff5533')
            else:
                graph.add_node(commit_number, label=f'c{commit_number}', shape='ellipse', color='#ff884d')
            if previous and previous not in graph.neighbors(commit_number):
                graph.add_edge(commit_number, previous, color='#ff884d')
            previous = commit_number

    branches = pygit.branches()
    for branch in branches: 
        if branch == current_branch:
            continue
        previous = None
        for commit in pygit.log(branch.strip().removeprefix('* ')):
            commit_number = session['commits'][commit]
            graph.add_node(commit_number, label=f'c{commit_number}', shape='ellipse', color='#d3d3d3')
            if previous and previous not in graph.neighbors(commit_number):
                graph.add_edge(commit_number, previous, color='#d3d3d3')
            previous = commit_number
        
    return render_template('your_template.html.j2', graph=graph, branches=branches)
