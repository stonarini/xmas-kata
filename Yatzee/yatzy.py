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
        pairs = list(filter(lambda x: dice.count(x) >= 2, set(dice)))
        if len(pairs) == 2:
            return sum(pairs) * 2
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
        return sum(dice) if sorted(dice) == range(1, 7) else 0

    @staticmethod
    def large_straight(dice):
        return sum(dice) if sorted(dice) == range(2, 8) else 0

    @staticmethod
    def yatzy(dice):
        return 50 if set(dice) == 1 else 0
