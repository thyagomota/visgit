from flask import Flask

app = Flask(__name__)
app.secret_key = 'bla'

# # session setup
# SESSION_TYPE = 'redis'
# Session(app)

import routes