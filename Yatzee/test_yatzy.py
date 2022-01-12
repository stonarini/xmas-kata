import pytest
import random
from yatzy import Yatzy


def gen_random_throws(num=2):
    throws = []
    for i in range(num):
        throws.append([random.randint(1, 6) for j in range(5)])
    return throws


score_values = {"ones": 1, "twos": 2, "threes": 3, "fours": 4, "fives": 5, "sixes": 6}

random_throws = gen_random_throws(40000)
random_throws += [[1, 1, 1, 1, 1], [6, 6, 6, 6, 6]]


def test_yatzy_class():
    print()
    for throw in random_throws:
        dummy_yatzy = Yatzy(throw)
        print("Testing -->", throw)
        assert_basic_scores(dummy_yatzy, throw)
        assert_choice(dummy_yatzy, throw)
        assert_pair(dummy_yatzy, throw)
        assert_two_pair(dummy_yatzy, throw)
        assert_three_of_a_kind(dummy_yatzy, throw)
        assert_four_of_a_kind(dummy_yatzy, throw)
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

def assert_pair(dummy_yatzy, throw):
    expected_value = [i * 2 for i in range(6, 0, -1) if throw.count(i) >= 2]
    real_value = dummy_yatzy.pair()
    if expected_value:
        assert expected_value[0] == real_value
    else:
        assert 0 == real_value

def assert_two_pair(dummy_yatzy, throw):
    pairs = [i * 2 for i in range(6, 0, -1) if throw.count(i) >= 2]
    real_value = dummy_yatzy.two_pair()
    if len(pairs) > 1:
        assert sum(pairs) == real_value
    else:
        assert 0 == real_value

def assert_three_of_a_kind(dummy_yatzy, throw):
    expected_value = [i * 3 for i in range(6, 0, -1) if throw.count(i) >= 3]
    real_value = dummy_yatzy.three_of_a_kind()
    if expected_value:
        assert expected_value[0] == real_value
    else:
        assert 0 == real_value

def assert_four_of_a_kind(dummy_yatzy, throw):
    expected_value = [i * 4 for i in range(6, 0, -1) if throw.count(i) >= 4]
    real_value = dummy_yatzy.four_of_a_kind()
    if expected_value:
        assert expected_value[0] == real_value
    else:
        assert 0 == real_value

def assert_full_house(dummy_yatzy, throw):
    real_value = dummy_yatzy.full_house()
    if set(throw) == 2 and 4 > throw.count(throw[0]) > 1:
        assert sum(throw) == real_value
    else:
        assert 0 == real_value

def assert_small_straight():
    pass

def assert_large_straight():
    pass

