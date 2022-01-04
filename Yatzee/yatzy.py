class Yatzy:
    def __init__(self, dice):
        self.dice = dice

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

    def pair(d1, d2, d3, d4, d5):
        counts = [0] * 6
        counts[d1 - 1] += 1
        counts[d2 - 1] += 1
        counts[d3 - 1] += 1
        counts[d4 - 1] += 1
        counts[d5 - 1] += 1
        at = 0
        for at in range(6):
            if counts[6 - at - 1] == 2:
                return (6 - at) * 2
        return 0

    def two_pair(d1, d2, d3, d4, d5):
        counts = [0] * 6
        counts[d1 - 1] += 1
        counts[d2 - 1] += 1
        counts[d3 - 1] += 1
        counts[d4 - 1] += 1
        counts[d5 - 1] += 1
        n = 0
        score = 0
        for i in range(6):
            if counts[6 - i - 1] >= 2:
                n = n + 1
                score += 6 - i

        if n == 2:
            return score * 2
        else:
            return 0

    def three_of_a_kind(d1, d2, d3, d4, d5):
        t = [0] * 6
        t[d1 - 1] += 1
        t[d2 - 1] += 1
        t[d3 - 1] += 1
        t[d4 - 1] += 1
        t[d5 - 1] += 1
        for i in range(6):
            if t[i] >= 3:
                return (i + 1) * 3
        return 0

    def four_of_a_kind(_1, _2, d3, d4, d5):
        tallies = [0] * 6
        tallies[_1 - 1] += 1
        tallies[_2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1
        for i in range(6):
            if tallies[i] >= 4:
                return (i + 1) * 4
        return 0

    def full_house(d1, d2, d3, d4, d5):
        tallies = []
        _2 = False
        i = 0
        _2_at = 0
        _3 = False
        _3_at = 0

        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1

        for i in range(6):
            if tallies[i] == 2:
                _2 = True
                _2_at = i + 1

        for i in range(6):
            if tallies[i] == 3:
                _3 = True
                _3_at = i + 1

        if _2 and _3:
            return _2_at * 2 + _3_at * 3
        else:
            return 0

    def small_straight(d1, d2, d3, d4, d5):
        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1
        if (
            tallies[0] == 1
            and tallies[1] == 1
            and tallies[2] == 1
            and tallies[3] == 1
            and tallies[4] == 1
        ):
            return 15
        return 0

    def large_straight(d1, d2, d3, d4, d5):
        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1
        if (
            tallies[1] == 1
            and tallies[2] == 1
            and tallies[3] == 1
            and tallies[4] == 1
            and tallies[5] == 1
        ):
            return 20
        return 0

    def yatzy(self):
        if set(self.dice) == 1:
            return 50
        else:
            return 0