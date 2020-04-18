import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt
from flask import Flask, render_template, request, jsonify
from datetime import datetime
from ai.ConnectFourAi import ConnectFourAi
from ai.Board import Board
from random import randint # TODO remove this if no longer using
from ai.qlearning.QTable import QTable
from ai.qlearning.QLearningAgent import QLearningAgent

app = Flask(__name__)

q_agent = QLearningAgent()

connectfour = ConnectFourAi()

# q_table = QTable()
# q_table.print_q_table(q_table.get_table())

# # # # Original
# # q_table.add_to_table('start')
# q_table.print_q_table(q_table.get_table())

# # # # Update and store
# q_table.add_to_table('burt')
# q_table.add_to_table('jones')
# q_table.add_to_table('smith')
# q_table.add_to_table('mike')

# q_table.store_table(q_table.get_table())

# # # # Load and print table
# data = q_table.load_table()
# q_table.print_q_table(q_table.get_table())

# q_table.add_to_table('afterwards')
# q_table.print_q_table(q_table.get_table())


# q_table.store_table(q_table.get_table())
# data = q_table.load_table()
# q_table.print_q_table(q_table.get_table())

# table = q_table.get_table()


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
			})


def play_human():
	human_token = 1
	ai_token = 2 
	player_to_go = 0
	while True:
		avail_pos = board.get_avail_positions(board.get_board())
		board.print_board()

		if len(avail_pos):
			print('Select your move from:')
			print(avail_pos)

			if player_to_go == 0:
				selection = input()
				if selection == 'exit':
					break

				selection = int(selection)
				if selection < board.COLS:
					player_to_go = 1
					selected_option = avail_pos[selection]
					user_row = selected_option[0]
					user_col = selected_option[1]
					board.add_token(user_row, user_col, human_token)
					if board.is_winning_move(user_row, user_col, human_token, board.get_board()):
						board.print_board()
						print('The HUMAN won!')
						break
				else: 
					print('Select bewteen 0-{}'.format(board.COLS-1))

			else:
				ai_selection = avail_pos[ai.ai_selection(avail_pos)]
				user_row = ai_selection[0]
				user_col = ai_selection[1]
				board.add_token(user_row, user_col, ai_token)
				if board.is_winning_move(user_row, user_col, ai_token, board.get_board()):
					board.print_board()
					print('The AI won!')
					break
				player_to_go = 0

		else:
			print('Game Over! It was a draw!')


def get_reward_mean(total_rewards):
    return sum(reward[0] for reward in total_rewards) / sum(reward[0] + reward[1] for reward in total_rewards)


def play_ai_ai():
	human_token = 1
	ai_token = 2 
	all_winning_moves = []
	rewards = []
	player_1 = 0
	player_2 = 0
	draws = 0
	for x in tqdm(range(1,100)):
		player_to_go = 0
		moves = 0		
		winner = None
		ai = ConnectFourAi()
		board = Board()
		if x%100 == 0:
			pass
			# q_table.print_q_table(q_table)
		while True:
			avail_pos = board.get_avail_positions(board.get_board())

			if len(avail_pos):
				if player_to_go == 0:
					player_to_go = 1
					selected_option = avail_pos[ai.ai_selection(avail_pos)]
					user_row = selected_option[0]
					user_col = selected_option[1]
					board.add_token(user_row, user_col, human_token)
					if board.is_winning_move(user_row, user_col, human_token, board.get_board()):
						# board.print_board()
						# print('The TOP AI won!')
						# print('Moves:', moves)	
						winner = 'Top AI'
						rewards.append([1,0])
						player_1 = player_1 + 1
						break

				else:
					ai_selection = avail_pos[ai.ai_selection(avail_pos)]
					user_row = ai_selection[0]
					user_col = ai_selection[1]
					board.add_token(user_row, user_col, ai_token)
					if board.is_winning_move(user_row, user_col, ai_token, board.get_board()):
						# board.print_board()
						# print('The BOTTOM AI won!')
						# print('Moves:', moves)
						winner = 'BOTTOM AI'
						rewards.append([0,1])
						player_2 = player_2 + 1
						break
					player_to_go = 0
				moves += 1

			else:
				# print('Game Over! It was a draw!')
				winner = 'Draw'
				draws = draws + 1
				break
		all_winning_moves.append(moves)

	print('player_1 won: {} – player_2 won: {} – Draws: {}'.format(player_1,player_2,draws))
	print(get_reward_mean(rewards))
	# print(all_winning_moves)

	# plt.plot(all_winning_moves)
	# plt.xlabel('Games')
	# plt.ylabel('Number of moves to win')
	# plt.show()




# play_ai_ai()



# board = [[1,0,1,2,0,1,0],[2,0,1,2,1,1,1],[1,0,0,2,1,0,0],[1,2,1,1,2,1,0],[1,0,2,0,1,0,1],[1,0,1,1,2,1,1]]

# state_key = []
# for row in range(len(board)):
# 	state_key = state_key + board[row]

# state_key = np.array(state_key).astype(str)
# state_key = ''.join(state_key)
# state_key = hex(int(state_key, 3))
# state_key = state_key[2:]

# print(state_key)


# q_table = dict()
# q_table['state_12d'] = list(np.zeros((7)))
# q_table['state_2d'] = list(np.zeros((7)))
# q_table['state_31dg'] = list(np.zeros((7)))

# q_table['state_31dg'][2] = 199.0 # Action number 2 (drop token in column 3) has value of 99


# print_q_table(q_table)








































