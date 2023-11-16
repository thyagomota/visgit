from flask_visjs import VisJS4
from flask import Flask

app = Flask(__name__)

VisJS4().init_app(app)

import routes