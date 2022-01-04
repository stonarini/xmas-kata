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
random_throws += [[1, 1, 1, 1, 1], [6, 6, 6, 6, 6]]


def test_yatzy_class():
    print()
    for throw in random_throws:
        dummy_yatzy = Yatzy(throw)
        print("Testing -->", throw)
        assert_basic_scores(dummy_yatzy, throw)
        assert_choice(dummy_yatzy, throw)
        assert_yatzy(dummy_yatzy, throw)


def assert_basic_scores(dummy_yatzy, throw):
    for score_key, score_value in score_values.items():
        expected_value = throw.count(score_value) * score_value
        real_value = eval(f"dummy_yatzy.{score_key}()")
        assert expected_value == real_value


def assert_choice(dummy_yatzy, throw):
    expected_value = sum(throw)
    real_value = dummy_yatzy.chance()
    assert expected_value == real_value


def assert_yatzy(dummy_yatzy, throw):
    expected_value = 50 if set(throw) == 1 else 0
    real_value = dummy_yatzy.yatzy()
    assert expected_value == real_value
