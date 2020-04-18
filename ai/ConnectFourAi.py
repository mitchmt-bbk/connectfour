import numpy as np
import threading
from random import randrange
from ai.qlearning.QLearningAgent import QLearningAgent

# The Agent
class ConnectFourAi:

	def __init__(self):
		pass

	def ai_selection(self, options):
		return randrange(len(options))