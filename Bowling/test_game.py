import pytest
from ScoreCard import ScoreCard
        
@pytest.mark.total_score_hitting_pins
def test_total_score_hitting_pins():
    pins = "12345123451234512345"
    total = 60
    score_card = ScoreCard(pins)
    assert total == score_card.score()

@pytest.mark.zero_symbol
def test_zero_symbol():
    pins = "9-9-9-9-9-9-9-9-9-9-"
    total = 90
    score_card = ScoreCard(pins)
    assert total == score_card.score()    
    
    pins = "9-3561368153258-7181"
    total = 82
    score_card = ScoreCard(pins)
    assert total == score_card.score()

@pytest.mark.spare_symbol
def test_spare_symbol():
    pins = "5/5/5/5/5/5/5/5/5/5/5"
    total = 150
    score_card = ScoreCard(pins)
    assert total == score_card.score()

    pins = "0//////////"
    total = 50
    score_card = ScoreCard(pins)
    assert total == score_card.score()

@pytest.mark.strike_symbol
def test_strike_symbol():
    pins = "X818181818181818181"
    total = 100
    score_card = ScoreCard(pins)
    assert total == score_card.score()

@pytest.mark.strike_and_zero
def test_strike_and_zero():
    pins = "9-9-9-9-9-9-9-9-9-X9-"
    total = 100
    score_card = ScoreCard(pins)
    assert total == score_card.score()

    pins = "X9-X9-9-9-9-9-9-9-"
    total = 110
    score_card = ScoreCard(pins)
    assert total == score_card.score()

    pins = "XX9-9-9-9-9-9-9-9-"
    total = 120
    score_card = ScoreCard(pins)
    assert total == score_card.score()

    pins = "XXX9-9-9-9-9-9-9-"
    total = 141
    score_card = ScoreCard(pins)
    assert total == score_card.score()

    pins = "9-9-9-9-9-9-9-9-9-XXX"
    total = 111
    score_card = ScoreCard(pins)
    assert total == score_card.score()

@pytest.mark.all_stikes
def test_all_stikes():
    pins = "XXXXXXXXXXXX"
    total = 300
    score_card = ScoreCard(pins)
    assert total == score_card.score()

@pytest.mark.real_example
def test_real_example():
    pins = "8/549-XX5/53639/9/X"
    total = 149
    score_card = ScoreCard(pins)
    assert total == score_card.score()

    pins = "X5/X5/XX5/--5/X5/"
    total = 175
    score_card = ScoreCard(pins)
    assert total == score_card.score()

    pins = "9-3/613/815/-/8-7/8/8"
    total = 131
    score_card = ScoreCard(pins)
    assert total == score_card.score()