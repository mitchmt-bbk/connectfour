from flask import Flask, render_template, request, jsonify
from datetime import datetime
from ai.ConnectFourAi import ConnectFourAi

from random import randint # TODO remove this if no longer using

app = Flask(__name__)

# Register the JS and Styles
from util import assets

ai = ConnectFourAi()

@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}

@app.route('/')
def main_page():
	return render_template('index.html', now=datetime.utcnow())

@app.route('/process-move', methods=['POST'])
def process_move():
	if request.form:
		# Row (ai_move[1]) is currently being ignored on the frontend - just waiting
		# for the AI to tell it the correct row position in the Python
		ai_move = [randint(0,6),randint(0,5)] # [col,row]
		# player_move = request.form['player_move'] # Here to use when calculating AI response
		return jsonify({
			'ai_move': ai_move, 
			'is_win': 0, # 0 = no win, 1 = player win, 2 = AI win, 3 = draw
			'test': ai.burt_test('from outside')
			})
