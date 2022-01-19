class Yatzy:
    @staticmethod
    def ones(dice):
        return dice.count(1)

    @staticmethod
    def twos(dice):
        return dice.count(2) * 2

    @staticmethod
    def threes(dice):
        return dice.count(3) * 3

    @staticmethod
    def fours(dice):
        return dice.count(4) * 4

    @staticmethod
    def fives(dice):
        return dice.count(5) * 5

    @staticmethod
    def sixes(dice):
        return dice.count(6) * 6

    @staticmethod
    def chance(dice):
        return sum(dice)

    @staticmethod
    def pair(dice):
        return max(filter(lambda x: dice.count(x) >= 2, set(dice)), default=0) * 2

    @staticmethod
    def two_pair(dice):
        pairs = [i * 2 for i in range(6, 0, -1) if dice.count(i) >= 2]
        if len(pairs) > 1:
            return sum(pairs)
        else:
            return 0

    @staticmethod
    def three_of_a_kind(dice):
        return max(filter(lambda x: dice.count(x) >= 3, set(dice)), default=0) * 3

    @staticmethod
    def four_of_a_kind(dice):
        return max(filter(lambda x: dice.count(x) >= 4, set(dice)), default=0) * 4

    @staticmethod
    def full_house(dice):
        if set(dice) == 2 and 4 > dice.count(dice[0]) > 1:
            return sum(dice)
        return 0

    @staticmethod
    def small_straight(dice):
        if set(dice) == 5 and sorted(dice)[0] == 1:
            return 15
        else:
            return 0

    @staticmethod
    def large_straight(dice):
        if set(dice) == 5 and sorted(dice)[0] == 2:
            return 20
        else:
            return 0

    @staticmethod
    def yatzy(dice):
        return 50 if set(dice) == 1 else 0
