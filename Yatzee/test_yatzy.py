import pytest
import random
from yatzy import Yatzy


def gen_random_throws(num=2):
    for i in range(num):
        yield [random.randint(1, 6) for j in range(5)]

random_yatzys = gen_random_throws(1)
def random_yatzy_gen():
    for throw in random_yatzys:
        yield Yatzy(throw)

@pytest.mark.parametrize("random_yatzy", [(yatzy for yatzy in random_yatzy_gen())])
def test_basic_scores(random_yatzy):
    score_values = {"ones": 1, "twos": 2, "threes": 3, "fours": 4, "fives": 5, "sixes": 6}
    for score_key, score_value in score_values.items():
        expected_value = random_yatzy.get_throw().count(score_value) * score_value
        real_value = eval(f"random_yatzy.{score_key}()")
        assert expected_value == real_value


def test_choice(random_yatzy):
    expected_value = sum(random_yatzy.get_throw())
    real_value = random_yatzy.chance()
    assert expected_value == real_value


def test_yatzy(random_yatzy):
    expected_value = 50 if set(random_yatzy.get_throw()) == 1 else 0
    real_value = random_yatzy.yatzy()
    assert expected_value == real_value

def test_pair(random_yatzy):
    expected_value = [i * 2 for i in range(6, 0, -1) if random_yatzy.get_throw().count(i) >= 2]
    real_value = random_yatzy.pair()
    if expected_value:
        assert expected_value[0] == real_value
    else:
        assert 0 == real_value

def test_two_pair(random_yatzy):
    pairs = [i * 2 for i in range(6, 0, -1) if random_yatzy.get_throw().count(i) >= 2]
    real_value = random_yatzy.two_pair()
    if len(pairs) > 1:
        assert sum(pairs) == real_value
    else:
        assert 0 == real_value

def test_three_of_a_kind(random_yatzy):
    expected_value = [i * 3 for i in range(6, 0, -1) if random_yatzy.get_throw().count(i) >= 3]
    real_value = random_yatzy.three_of_a_kind()
    if expected_value:
        assert expected_value[0] == real_value
    else:
        assert 0 == real_value

def test_four_of_a_kind(random_yatzy):
    expected_value = [i * 4 for i in range(6, 0, -1) if random_yatzy.get_throw().count(i) >= 4]
    real_value = random_yatzy.four_of_a_kind()
    if expected_value:
        assert expected_value[0] == real_value
    else:
        assert 0 == real_value

def test_full_house(random_yatzy):
    real_value = random_yatzy.full_house()
    if set(random_yatzy.get_throw()) == 2 and 4 > throw.count(throw[0]) > 1:
        assert sum(random_yatzy.get_throw()) == real_value
    else:
        assert 0 == real_value

def test_small_straight(random_yatzy):
    real_value = random_yatzy.small_straight()
    if set(random_yatzy.get_throw()) == 5 and sorted(throw)[0] == 1:
        assert 15 == real_value
    else:
        assert 0 == real_value

def test_large_straight(random_yatzy):
    real_value = random_yatzy.large_straight()
    if set(random_yatzy.get_throw()) == 5 and sorted(throw)[0] == 2:
        assert 20 == real_value
    else:
        assert 0 == real_value
