from ai.qlearning.QTable import QTable

class QLearningAgent:
	q_table = None

	def __init__(self):
		self.q_table_obj = QTable()
		self.q_table = self.q_table_obj.get_table()
		print(self.q_table)
