from flask import Flask, render_template
from flask_scss import Scss

app = Flask(__name__)
# Scss(app, static_dir='styles', asset_dir='assets')
Scss(app)
# assets.register('scss_all', scss)

@app.route('/')
def hello_world():
	return render_template('index.html')