import pytest
import random
from yatzy import Yatzy


def gen_random_throws(num=2):
    throws = []
    for i in range(num):
        throws.append([random.randint(1, 6) for i in range(5)])
    return throws


score_values = {"ones": 1, "twos": 2, "threes": 3, "fours": 4, "fives": 5, "sixes": 6}

random_throws = gen_random_throws(5)


@pytest.mark.test_basic_scores
def test_basic_scores():
    for throw in random_throws:
        for score_key, score_value in score_values.items():
            test_yatzy = Yatzy(throw)
            expected_value = throw.count(score_value) * score_value
            real_value = eval(f"test_yatzy.{score_key}()")
            assert expected_value == real_value
