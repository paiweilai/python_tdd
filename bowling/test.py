import unittest

from game import Game


class BowlingGameTest(unittest.TestCase):

    def test_create_game(self):
        Game()


if __name__ == '__main__':
    unittest.main()
