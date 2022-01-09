class ScoreCard:
    def __init__(self):
        self.throws = ""
        self.max_frames = 10

    # public interface
    def add(self, throw):
        self.throws += throw

    def score(self):
        return self.calculate_score()

    def reset_score(self):
        self.throws = ""

    def set_max_frames(self, max_frames):
        self.max_frames = max_frames

    # private methods
    def calculate_score(self):
        STRIKE = 10
        SPARE = 10

        score = 0
        frame = 0
        i = 0
        while i <= len(self.throws) - 1:
            throw = self.compute_value(i)
            next_throw = self.compute_value(i + 1)
            next_next_throw = self.compute_value(i + 2)

            if frame == 9:
                if throw == STRIKE:
                    score += throw
                else:
                    score += throw + next_throw

            elif (throw + next_throw) < SPARE:
                score += throw + next_throw
            else:
                score += throw + next_throw + next_next_throw

            if frame == self.max_frames:
                break
            frame += 1

            if throw != STRIKE:
                i += 2
            else:
                i += 1

        return score

    def compute_value(self, value):
        if value >= len(self.throws) or self.throws[value] == "-":
            return 0
        elif self.throws[value] == "X":
            return 10
        elif self.throws[value] == "/":
            return 10 - int(self.throws[value - 1])
        else:
            return int(self.throws[value])
