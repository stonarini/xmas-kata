from ScoreCard import ScoreCard


class Game:
    def __init__(self):
        self.ScoreCard = ScoreCard()

    # public interface
    def roll(self, throw):
        self.ScoreCard.add(throw)

    def get_score(self):
        return self.ScoreCard.score()

    def reset_score(self):
        self.ScoreCard.reset_score()
