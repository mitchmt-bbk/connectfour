from pathlib import Path
import numpy as np
import ai.config as config
import h5py
import ast

class QTable:

	def __init__(self, debug = False):
		data_filename = "data/qlearning_table_data.hdf5"
		if debug:
			# Test data file
			data_filename = "tests/test_data/qlearning_table_data_test.hdf5"

		path_to_data_file = Path(__file__).parents[2] / data_filename
		self.FILENAME = path_to_data_file
		try: 
			self.__q_table = self.load_table()
		except:
			self.__q_table = dict()


	def get_table(self):
		return self.__q_table


	def add_to_table(self, state_key):
		self.__q_table[state_key] = list(np.zeros(config.COLS))


	def store_table(self, table):
		try:
			with h5py.File(self.FILENAME, "w") as file:

				table_keys = list(table)
				table_values = np.array(list(table.values()))
				
				file.create_dataset('keys', data=str(table_keys))
				file.create_dataset('values', data=table_values, dtype=float)
				file.close()
		except IOError as err:
			print("I/O error: {}".format(err))

  
	def load_table(self):
		with h5py.File(self.FILENAME, "r") as file:
		
			table_keys = file['keys'][...].tolist()
			table_keys = ast.literal_eval(table_keys)
			table_values = file['values'][...].tolist()
			file.close()

			loaded_table = dict()
			for i in range(len(table_values)):
				loaded_table[table_keys[i]] = table_values[i]

			return loaded_table


	# For debuggin
	def print_q_table(self, table):
		print("")
		for index, state in enumerate(table):
			end_space_len = 13
			num_len = len(state)
			end_space_len = (end_space_len - num_len)
			print(state + ' '*end_space_len +'|', end ="")
			for action in range(len(table[state])):
				end_space_len = 6
				num_len = len(str(table[state][action]))
				end_space_len = (end_space_len - num_len)
				start_space_len = 3 if num_len < 4 else 2
				end_space_len = end_space_len if num_len < 4 else end_space_len + 1
				print ("|{}{}{}".format(' '*start_space_len,table[state][action],' '*end_space_len), end ="")
			print("|", end="")
			print("")
		print("")







# Push the test suite to git
# Create new branch for prototype / board etc
# Push to git
# Create branch to create Q Learning




















