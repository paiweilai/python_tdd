class Game(object):

    def __init__(self):
        self._rolls = [0] * 21
        self._current_roll = 0

    def roll(self, pins):
        self._rolls[self._current_roll] = pins
        self._current_roll += 1

    def is_spare(self, ball_index):
        return self._rolls[ball_index] + self._rolls[ball_index + 1] == 10

    def is_strike(self, ball_index):
        return self._rolls[ball_index] == 10

    def get_spare_bonus(self, ball_index):
        return self._rolls[ball_index + 2]

    def get_strike_bonus(self, ball_index):
        return self._rolls[ball_index + 1] + self._rolls[ball_index + 2]

    def score(self):
        s = 0
        ball_index = 0

        for _ in range(10):

            if self.is_strike(ball_index):
                s += 10 + self.get_strike_bonus(ball_index)
                ball_index += 1
            elif self.is_spare(ball_index):
                s += 10 + self.get_spare_bonus(ball_index)
                ball_index += 2
            else:
                s += self._rolls[ball_index] + self._rolls[ball_index + 1]
                ball_index += 2

        return s
