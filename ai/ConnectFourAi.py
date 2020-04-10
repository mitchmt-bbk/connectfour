import numpy as np
import threading
from random import randint
from tqdm import tqdm

class ConnectFourAi:
	grid = None
	counter = 0
	grid_size = (3,3)

	def __init__(self):
		self.grid = np.zeros(self.grid_size,dtype = int)
		self.grid_size = np.count_nonzero(self.grid==0)
		print('Started')

	def printit(self):
		pass
		# for i in tqdm(range(1000)):
		# 	j = i + i

		# if self.counter < self.grid_size:
		# 	self.grid[self.get_available_slot()] = randint(1,2)
		# 	threading.Timer(1.0, self.printit).start()
		# 	self.counter = self.counter + 1
		# 	print ""
		# 	print self.counter
		# 	print self.grid
		# else :
		# 	print "All done"

	def get_available_slot(self):
		free_slot_found = False
		while free_slot_found is False:
			col, row = randint(0,2),randint(0,2)			
			if self.grid[col, row] == 0:
				free_slot_found = True

		return col, row
			
		


class Board:
	board = None
	ROWS = 6
	COLS = 7
	NUM_TOKENS_FOR_WIN = 4

	def __init__(self):
		self.board = np.zeros((self.ROWS,self.COLS),dtype = int)

	def print_board(self):
		for row in reversed(range(self.ROWS)):
			print()
			for col in range(self.COLS):
				print ("| {} ".format(self.board[row][col]), end ="")
			print("|", end="")
		print("")


	def add_token(self, row, col, token):
		self.board[row][col] = token


	def is_vertical_win(self, row, col, token):
		tokens_away_from_current = 3
		row_range = row - tokens_away_from_current
		if 0 <= row_range < self.ROWS:
			placed_tokens = 0
			for i in range(0,self.NUM_TOKENS_FOR_WIN):
				next_row = row - i
				if self.board[next_row][col] == token:
					placed_tokens += 1

			if placed_tokens == 3:
				print('is_vertical_win')
				return True	

		return False

	def is_horizontal_win(self, row, col, token):
		for i in range(0,self.NUM_TOKENS_FOR_WIN):
			start = i
			end = start + self.NUM_TOKENS_FOR_WIN
			placed_tokens = 0
			for j in range(start,end):	
				if self.board[row][j] == token:
					placed_tokens += 1
			if placed_tokens == 3:
				print('is_horizontal_win')
				return True

		return False


	def is_diagonal_win_left_to_right(self, row, col, token):
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
		if start_col < self.NUM_TOKENS_FOR_WIN and start_row < 3:

			# Calculate how many repitions it'll take for whole diagonal
			reps = 0
			if start_col == 0:
				reps = self.ROWS - (start_row + 3)
			else:
				reps = self.COLS - (start_col + 3)

			# Loop through the diagonal and check for four in a row
			for i in range(0,reps):
				placed_tokens = 0
				for j in range(0,self.NUM_TOKENS_FOR_WIN):
					if self.board[start_row + j][start_col + j] == token:
						placed_tokens += 1

				start_row = start_row + 1
				start_col = start_col + 1

				if placed_tokens == 3:
					print('is_diagonal_win_left_to_right')
					return True

		return False






	def is_diagonal_win_right_to_left(self, row, col, token):
		# 'Remove' the array indexing
		start_row = row + 1
		start_col = col + 1
		
		# Calculate the starting positon for that diagonal
		if start_row - self.ROWS < 0:
			start_col = start_row + start_col - 2
			start_row = 0
		else:			
			start_col = start_row + start_col - 2
			start_row = 0	

		if start_col > self.COLS - 1:
			start_row = abs(self.COLS - start_col -1)
			start_col = self.COLS - 1

		# If a four in a row is possible
		if start_col >= self.NUM_TOKENS_FOR_WIN - 1 and start_row < self.NUM_TOKENS_FOR_WIN:

			# Calculate how many repitions it'll take for whole diagonal
			reps = 0
			if start_col == self.COLS - 1:
				reps = self.ROWS - (start_row + 3)
			else:
				reps = (start_col + 5) - self.COLS
			
			# Loop through the diagonal and check for four in a row
			for i in range(0,reps):
				placed_tokens = 0
				for j in range(0,self.NUM_TOKENS_FOR_WIN):
					if self.board[start_row + j][start_col - j] == token:
						placed_tokens += 1

				start_row = start_row + 1
				start_col = start_col - 1

				if placed_tokens == 3:
					print('is_diagonal_win_right_to_left')
					return True

		return False





	def is_winning_move(self, row, col, token):
		if (self.is_vertical_win(row, col, token) or 
			self.is_horizontal_win(row, col, token) or 
			self.is_diagonal_win_left_to_right(row, col, token) or 
			self.is_diagonal_win_right_to_left(row, col, token) ):
			print('Yes, a winning move!')
			return True

		return False





board = Board()

# board.add_token(3,1,2);
# board.add_token(1,3,2);
# board.add_token(4,0,2);
board.is_winning_move(2,2,2)

# board.add_token(2,2,2);

board.print_board();


# 3 2 (start)
# 1 0 

# 1 0 
# 1 0

# 2 1
# 1 0

# 3 2
# 1 0

# 4 3
# 1 0 





# Write the diagonal checkers
# Create a new branch and implement the testing suite



























