class Yatzy:
    def __init__(self, dice):
        self.dice = dice

    def get_throw(self):
        return self.dice

    def ones(self):
        return self.dice.count(1)

    def twos(self):
        return self.dice.count(2) * 2

    def threes(self):
        return self.dice.count(3) * 3

    def fours(self):
        return self.dice.count(4) * 4

    def fives(self):
        return self.dice.count(5) * 5

    def sixes(self):
        return self.dice.count(6) * 6

    def chance(self):
        return sum(self.dice)

    def pair(self):
        for i in range(6, 0, -1):
            if self.dice.count(i) >= 2:
                return i * 2
        return 0

    def two_pair(self):
        pairs = [i * 2 for i in range(6, 0, -1) if self.dice.count(i) >= 2]
        if len(pairs) > 1:
            return sum(pairs)
        else:
            return 0

    def three_of_a_kind(self):
        for i in range(6, 0, -1):
            if self.dice.count(i) >= 3:
                return i * 3
        return 0

    def four_of_a_kind(self):
        for i in range(6, 0, -1):
            if self.dice.count(i) >= 4:
                return i * 4
        return 0

    def full_house(self):
        if set(self.dice) == 2 and 4 > self.dice.count(self.dice[0]) > 1:
            return sum(self.dice)
        return 0

    def small_straight(self):
        if set(self.dice) == 5 and sorted(self.dice)[0] == 1:
            return 15
        else:
            return 0

    def large_straight(self):
        if set(self.dice) == 5 and sorted(self.dice)[0] == 2:
            return 20
        else:
            return 0

    def yatzy(self):
        if set(self.dice) == 1:
            return 50
        else:
            return 0
