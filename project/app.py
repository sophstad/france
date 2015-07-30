from flask import Flask
from flask_frozen import Freezer
import chartkick

app = Flask(__name__)
app.config.from_pyfile('settings.py')
app.jinja_env.add_extension("chartkick.ext.charts")
freezer = Freezer(app)