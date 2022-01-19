import pytest
from yatzy import Yatzy


@pytest.mark.parametrize("d1", [i for i in range(1, 7)])
@pytest.mark.parametrize("d2", [i for i in range(1, 7)])
@pytest.mark.parametrize("d3", [i for i in range(1, 7)])
@pytest.mark.parametrize("d4", [i for i in range(1, 7)])
@pytest.mark.parametrize("d5", [i for i in range(1, 7)])
@pytest.mark.basic_scores
def test_basic_scores(d1, d2, d3, d4, d5):
    throw = [d1, d2, d3, d4, d5]
    score_values = {
        "ones": 1,
        "twos": 2,
        "threes": 3,
        "fours": 4,
        "fives": 5,
        "sixes": 6,
    }
    for score_key, score_value in score_values.items():
        expected_value = throw.count(score_value) * score_value
        real_value = eval(f"Yatzy.{score_key}(throw)")
        assert expected_value == real_value


@pytest.mark.parametrize("d1", [i for i in range(1, 7)])
@pytest.mark.parametrize("d2", [i for i in range(1, 7)])
@pytest.mark.parametrize("d3", [i for i in range(1, 7)])
@pytest.mark.parametrize("d4", [i for i in range(1, 7)])
@pytest.mark.parametrize("d5", [i for i in range(1, 7)])
@pytest.mark.chance
def test_chance(d1, d2, d3, d4, d5):
    throw = [d1, d2, d3, d4, d5]
    expected_value = sum(throw)
    real_value = Yatzy.chance(throw)
    assert expected_value == real_value


@pytest.mark.parametrize("d1", [i for i in range(1, 7)])
@pytest.mark.parametrize("d2", [i for i in range(1, 7)])
@pytest.mark.parametrize("d3", [i for i in range(1, 7)])
@pytest.mark.parametrize("d4", [i for i in range(1, 7)])
@pytest.mark.parametrize("d5", [i for i in range(1, 7)])
@pytest.mark.pair
def test_pair(d1, d2, d3, d4, d5):
    throw = [d1, d2, d3, d4, d5]
    expected_value = [i * 2 for i in range(6, 0, -1) if throw.count(i) >= 2]
    real_value = Yatzy.pair(throw)
    if expected_value:
        assert expected_value[0] == real_value
    else:
        assert 0 == real_value


@pytest.mark.parametrize("d1", [i for i in range(1, 7)])
@pytest.mark.parametrize("d2", [i for i in range(1, 7)])
@pytest.mark.parametrize("d3", [i for i in range(1, 7)])
@pytest.mark.parametrize("d4", [i for i in range(1, 7)])
@pytest.mark.parametrize("d5", [i for i in range(1, 7)])
@pytest.mark.two_pair
def test_two_pair(d1, d2, d3, d4, d5):
    throw = [d1, d2, d3, d4, d5]
    pairs = [i * 2 for i in range(6, 0, -1) if throw.count(i) >= 2]
    real_value = Yatzy.two_pair(throw)
    if len(pairs) > 1:
        assert sum(pairs) == real_value
    else:
        assert 0 == real_value


@pytest.mark.parametrize("d1", [i for i in range(1, 7)])
@pytest.mark.parametrize("d2", [i for i in range(1, 7)])
@pytest.mark.parametrize("d3", [i for i in range(1, 7)])
@pytest.mark.parametrize("d4", [i for i in range(1, 7)])
@pytest.mark.parametrize("d5", [i for i in range(1, 7)])
@pytest.mark.three_of_a_kind
def test_three_of_a_kind(d1, d2, d3, d4, d5):
    throw = [d1, d2, d3, d4, d5]
    expected_value = [i * 3 for i in range(6, 0, -1) if throw.count(i) >= 3]
    real_value = Yatzy.three_of_a_kind(throw)
    if expected_value:
        assert expected_value[0] == real_value
    else:
        assert 0 == real_value


@pytest.mark.parametrize("d1", [i for i in range(1, 7)])
@pytest.mark.parametrize("d2", [i for i in range(1, 7)])
@pytest.mark.parametrize("d3", [i for i in range(1, 7)])
@pytest.mark.parametrize("d4", [i for i in range(1, 7)])
@pytest.mark.parametrize("d5", [i for i in range(1, 7)])
@pytest.mark.four_of_a_kind
def test_four_of_a_kind(d1, d2, d3, d4, d5):
    throw = [d1, d2, d3, d4, d5]
    expected_value = [i * 4 for i in range(6, 0, -1) if throw.count(i) >= 4]
    real_value = Yatzy.four_of_a_kind(throw)
    if expected_value:
        assert expected_value[0] == real_value
    else:
        assert 0 == real_value


@pytest.mark.parametrize("d1", [i for i in range(1, 7)])
@pytest.mark.parametrize("d2", [i for i in range(1, 7)])
@pytest.mark.parametrize("d3", [i for i in range(1, 7)])
@pytest.mark.parametrize("d4", [i for i in range(1, 7)])
@pytest.mark.parametrize("d5", [i for i in range(1, 7)])
@pytest.mark.full_house
def test_full_house(d1, d2, d3, d4, d5):
    throw = [d1, d2, d3, d4, d5]
    real_value = Yatzy.full_house(throw)
    if set(throw) == 2 and 4 > throw.count(throw[0]) > 1:
        assert sum(throw) == real_value
    else:
        assert 0 == real_value


@pytest.mark.parametrize("d1", [i for i in range(1, 7)])
@pytest.mark.parametrize("d2", [i for i in range(1, 7)])
@pytest.mark.parametrize("d3", [i for i in range(1, 7)])
@pytest.mark.parametrize("d4", [i for i in range(1, 7)])
@pytest.mark.parametrize("d5", [i for i in range(1, 7)])
@pytest.mark.small_straight
def test_small_straight(d1, d2, d3, d4, d5):
    throw = [d1, d2, d3, d4, d5]
    real_value = Yatzy.small_straight(throw)
    if set(throw) == 5 and sorted(throw)[0] == 1:
        assert 15 == real_value
    else:
        assert 0 == real_value


@pytest.mark.parametrize("d1", [i for i in range(1, 7)])
@pytest.mark.parametrize("d2", [i for i in range(1, 7)])
@pytest.mark.parametrize("d3", [i for i in range(1, 7)])
@pytest.mark.parametrize("d4", [i for i in range(1, 7)])
@pytest.mark.parametrize("d5", [i for i in range(1, 7)])
@pytest.mark.large_straight
def test_large_straight(d1, d2, d3, d4, d5):
    throw = [d1, d2, d3, d4, d5]
    real_value = Yatzy.large_straight(throw)
    if set(throw) == 5 and sorted(throw)[0] == 2:
        assert 20 == real_value
    else:
        assert 0 == real_value


@pytest.mark.parametrize("d1", [i for i in range(1, 7)])
@pytest.mark.parametrize("d2", [i for i in range(1, 7)])
@pytest.mark.parametrize("d3", [i for i in range(1, 7)])
@pytest.mark.parametrize("d4", [i for i in range(1, 7)])
@pytest.mark.parametrize("d5", [i for i in range(1, 7)])
@pytest.mark.yatzy
def test_yatzy(d1, d2, d3, d4, d5):
    throw = [d1, d2, d3, d4, d5]
    expected_value = 50 if set(throw) == 1 else 0
    real_value = Yatzy.yatzy(throw)
    assert expected_value == real_value
