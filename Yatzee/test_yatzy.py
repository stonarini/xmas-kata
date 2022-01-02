import pytest
import string
import random
from yatzy import Yatzy


def gen_random_throws(num=2):
    throws = []
    for i in range(num):
        throws.append([random.randint(1, 6) for i in range(6)])
    return throws


def get_random_ascii_throws(num=2):
    throws = []
    for i in range(num):
        throws.append(
            [
                random.choice(string.ascii_letters + string.digits + string.punctuation)
                for i in range(6)
            ]
        )
    return throws


def get_expected_value(throw, value):
    expected_value = [ord(num) % 6 if type(num) != int else num for num in throw].count(
        value
    ) * value
    return expected_value if expected_value else 0


score_values = {"ones": 1, "twos": 2, "threes": 3, "fours": 4, "fives": 5, "sixes": 6}

random_throws = gen_random_throws(5)
random_throws += get_random_ascii_throws(5)


@pytest.mark.test_basic_scores
def test_basic_scores():
    for throw in random_throws:
        for score_key, score_value in score_values.items():
            test_yatzy = Yatzy(throw)
            expected_value = get_expected_value(throw, score_value)
            real_value = eval(f"test_yatzy.{score_key}()")
            assert expected_value == real_value
