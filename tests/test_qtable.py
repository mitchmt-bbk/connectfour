import unittest
import numpy as np
from ai.qlearning.QTable import QTable
import ai.config as config

class QTableTests(unittest.TestCase):
    q_table = None
    test_q_table = None

    # # # # # # # # # # #
    # Setup and teardown
    # # # # # # # # # # #

    # Executed for each test
    def setUp(self):
        # Create the QTable
        self.q_table = QTable(True) # Debugging set to True
        # Create empty testing 'q_table'
        self.test_q_table = dict()
 
    # Executed after each test
    def tearDown(self):
        pass
 
    # # # # #
    # Tests
    # # # # #

    def test_add_to_table(self):
        # Update the table using add_to_table()
        self.q_table.add_to_table('test_1')
        updated_table = self.q_table.get_table()

        # Create test example to compare
        self.test_q_table['test_1'] = list(np.zeros(config.COLS))

        self.assertDictEqual(self.test_q_table, updated_table)


    def test_store_table(self):
        # Update the table using add_to_table()
        self.q_table.add_to_table('test_1')
        # Store the table
        self.q_table.store_table(self.q_table.get_table())
        stored_table = self.q_table.load_table()

        # Create test example to compare        
        self.test_q_table['test_1'] = list(np.zeros(config.COLS))

        self.assertDictEqual(self.test_q_table, stored_table)


if __name__ == "__main__":
    unittest.main()
