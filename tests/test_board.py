import unittest
import numpy as np
from ai.Board import Board
import ai.config as config

class BoardTests(unittest.TestCase):
    board = None
    test_board = None

    # # # # # # # # # # #
    # Setup and teardown
    # # # # # # # # # # #

    # Executed for each test
    def setUp(self):
        # Create the board
        self.board = Board()
        # Create empty testing 'board'
        self.test_board = np.zeros((config.ROWS,config.COLS),dtype = int)
 
    # Executed after each test
    def tearDown(self):
        pass
 
    # # # # #
    # Tests
    # # # # #

    def test_add_token(self):
        # Create a matching array
        self.test_board[2][2] = 2
        # Update board array to compare
        self.board.add_token(2,2,2)
        # Compare the two arrays – returns None if the arrays are equal
        self.assertIsNone(np.testing.assert_array_equal(self.board.get_board(), self.test_board))

    def test_is_vertical_win_true(self):
        self.test_board[0][0] = 2
        self.test_board[1][0] = 2
        self.test_board[2][0] = 2
        self.test_board[3][0] = 2
        self.assertTrue(self.board.is_vertical_win(3, 0, 2, self.test_board))

    def test_is_vertical_win_false(self):
        self.test_board[0][0] = 2
        self.test_board[1][0] = 2
        self.test_board[2][0] = 1 # Intentional error
        self.assertFalse(self.board.is_vertical_win(3, 0, 2, self.test_board))

    def test_is_horizontal_win_true(self):
        self.test_board[2][1] = 2
        self.test_board[2][2] = 2
        self.test_board[2][3] = 2
        self.test_board[2][4] = 2
        self.assertTrue(self.board.is_horizontal_win(2, 4, 2, self.test_board))

    def test_is_horizontal_win_false(self):
        self.test_board[2][1] = 2
        self.test_board[2][2] = 2
        self.test_board[2][3] = 1 # Intentional error
        self.assertFalse(self.board.is_horizontal_win(2, 4, 2, self.test_board))

    def test_is_diagonal_win_left_to_right_true(self):
        self.test_board[5][3] = 2
        self.test_board[4][2] = 2
        self.test_board[3][1] = 2
        self.test_board[2][0] = 2
        self.assertTrue(self.board.is_diagonal_win_left_to_right(2, 0, 2, self.test_board))

    def test_is_diagonal_win_left_to_right_false(self):
        self.test_board[5][3] = 2
        self.test_board[4][2] = 2
        self.test_board[3][1] = 1 # Intentional error
        self.assertFalse(self.board.is_diagonal_win_left_to_right(2, 0, 2, self.test_board))

    def test_is_diagonal_win_right_to_left_true(self):
        self.test_board[2][4] = 2
        self.test_board[3][3] = 2
        self.test_board[4][2] = 2
        self.test_board[5][1] = 2
        self.assertTrue(self.board.is_diagonal_win_right_to_left(5, 1, 2, self.test_board))

    def test_is_diagonal_win_right_to_left_false(self):
        self.test_board[2][4] = 2
        self.test_board[3][3] = 2
        self.test_board[5][1] = 2
        self.test_board[4][2] = 1 # Intentional error
        self.assertFalse(self.board.is_diagonal_win_right_to_left(5, 1, 2, self.test_board))

    def test_is_winning_move_true(self):
        self.test_board[2][4] = 2
        self.test_board[3][3] = 2
        self.test_board[4][2] = 2
        self.test_board[5][1] = 2
        self.assertTrue(self.board.is_winning_move(5, 1, 2, self.test_board))

    def test_is_winning_move_false(self):
        self.test_board[2][4] = 2
        self.test_board[3][3] = 2
        # self.test_board[4][2] = 2  Remove a token
        self.assertFalse(self.board.is_winning_move(5, 1, 2, self.test_board))

    def test_get_avail_positions(self):
        self.test_board[0][1] = 1
        self.test_board[0][2] = 2
        self.test_board[0][3] = 1
        self.test_board[0][4] = 1
        self.test_board[1][2] = 1
        self.test_board[1][3] = 2
        self.test_board[2][3] = 2
        self.test_board[3][3] = 1
        self.test_board[4][3] = 2
        self.test_board[5][3] = 1        
        self.test_board[0][6] = 2

        # Correct available positions
        avail_positions = [[0,0],[1,1],[2,2],[1,4],[0,5],[1,6]]
        self.assertIsNone(np.testing.assert_array_equal(self.board.get_avail_positions(self.test_board), avail_positions))


if __name__ == "__main__":
    unittest.main()
