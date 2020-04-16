import numpy as np
import ai.config as config

# The Environment
class Board:
	__board = None

	def __init__(self):
		self.__board = np.zeros((config.ROWS,config.COLS),dtype = int)


	def add_token(self, row, col, token):
		self.__board[row][col] = token


	def get_board(self):
		return self.__board


	def is_vertical_win(self, row, col, token, board):
		tokens_away_from_current = 3
		row_range = row - tokens_away_from_current
		if 0 <= row_range < config.ROWS:
			placed_tokens = 0
			for i in range(0,config.NUM_TOKENS_FOR_WIN):
				next_row = row - i
				if board[next_row][col] == token:
					placed_tokens += 1

			if placed_tokens == config.NUM_TOKENS_FOR_WIN:
				# print('is_vertical_win')
				return True	

		return False


	def is_horizontal_win(self, row, col, token, board):
		for i in range(0,config.NUM_TOKENS_FOR_WIN):
			start = i
			end = start + config.NUM_TOKENS_FOR_WIN
			placed_tokens = 0
			for j in range(start,end):	
				if board[row][j] == token:
					placed_tokens += 1
			if placed_tokens == config.NUM_TOKENS_FOR_WIN:
				# print('is_horizontal_win')
				return True

		return False


	def is_diagonal_win_left_to_right(self, row, col, token, board):
		# 'Remove' the array indexing
		start_row = row + 1
		start_col = col + 1

		# Calculate the starting positon for that diagonal
		if start_col - start_row < 0:
			start_row = abs(start_col - start_row)
			start_col = 0
		else:			
			start_col = start_col - start_row
			start_row = 0

		# If a four in a row is possible
		if start_col < config.NUM_TOKENS_FOR_WIN and start_row < 3:

			# Calculate how many repitions it'll take for whole diagonal
			reps = 0
			if start_col == 0:
				reps = config.ROWS - (start_row + 3)
			else:
				reps = config.COLS - (start_col + 3)

			# Loop through the diagonal and check for four in a row
			for i in range(0,reps):
				placed_tokens = 0
				for j in range(0,config.NUM_TOKENS_FOR_WIN):
					if board[start_row + j][start_col + j] == token:
						placed_tokens += 1

				start_row = start_row + 1
				start_col = start_col + 1

				if placed_tokens == config.NUM_TOKENS_FOR_WIN:
					# print('is_diagonal_win_left_to_right')
					return True

		return False


	def is_diagonal_win_right_to_left(self, row, col, token, board):
		# 'Remove' the array indexing
		start_row = row + 1
		start_col = col + 1
		
		# Calculate the starting positon for that diagonal
		if start_row - config.ROWS < 0:
			start_col = start_row + start_col - 2
			start_row = 0
		else:			
			start_col = start_row + start_col - 2
			start_row = 0	

		if start_col > config.COLS - 1:
			start_row = abs(config.COLS - start_col -1)
			start_col = config.COLS - 1

		# If a four in a row is possible
		if start_col >= config.NUM_TOKENS_FOR_WIN - 1 and start_row < config.NUM_TOKENS_FOR_WIN:

			# Calculate how many repitions it'll take for whole diagonal
			reps = 0
			if start_col == config.COLS - 1:
				reps = config.ROWS - (start_row + 3)
			else:
				reps = (start_col + 5) - config.COLS
			
			# Loop through the diagonal and check for four in a row
			for i in range(0,reps):
				placed_tokens = 0
				for j in range(0,config.NUM_TOKENS_FOR_WIN):
					if board[start_row + j][start_col - j] == token:
						placed_tokens += 1

				start_row = start_row + 1
				start_col = start_col - 1

				if placed_tokens == config.NUM_TOKENS_FOR_WIN:
					# print('is_diagonal_win_right_to_left')
					return True

		return False


	def is_winning_move(self, row, col, token, board):
		if (self.is_vertical_win(row, col, token, board) or 
			self.is_horizontal_win(row, col, token, board) or 
			self.is_diagonal_win_left_to_right(row, col, token, board) or 
			self.is_diagonal_win_right_to_left(row, col, token, board)):
			# print('Yes, a winning move!')
			return True

		return False


	def get_avail_positions(self, board):
		avail_positions = []
		for i in range(0,config.COLS):
			for j in range(0,config.ROWS):
				if board[j][i] == 0:
					avail_positions.append([j,i])
					break
		return avail_positions


	# Helper for debugging
	def print_board(self):
		for row in reversed(range(config.ROWS)):
			print()
			for col in range(config.COLS):
				print ("| {} ".format(self.__board[row][col]), end ="")
			print("|", end="")
		print("")




# Debugging

# board = Board()
# # board.add_token(2,1,2);
# # board.add_token(3,2,2);
# # board.add_token(4,3,2);
# # board.is_winning_move(5,4,2, board.get_board())
# # board.add_token(5,4,2);

# # board.print_board();


# board.play_human()































