from flask import Flask, render_template
from flask_scss import Scss

app = Flask(__name__)
Scss(app)

@app.route('/')
def hello_world():
	return render_template('index.html')