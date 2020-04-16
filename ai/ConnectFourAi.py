import numpy as np
import threading
from random import randrange

# The Agent
class ConnectFourAi:

	def __init__(self):
		pass

	def ai_selection(self, options):
		return randrange(len(options))