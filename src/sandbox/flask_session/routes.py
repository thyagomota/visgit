from app import app
from flask import render_template, session
import uuid
import os

@app.route('/')
@app.route('/index')
def index():
    if 'user_id' not in session:
        user_id = str(uuid.uuid4())
        session['user_id'] = user_id
        os.mkdir(f'flask_session/repos/{user_id}')
        return f"user_id {user_id} was created!"
    else:
        user_id = session['user_id']
        return f"welcome back {user_id}!"