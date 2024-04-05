from utils import flächeRechteckBerechenen

def test_flächeRechteckBerechenen():
    assert flächeRechteckBerechenen(3,4) == 12
    assert flächeRechteckBerechenen(10,10) == 100
    assert flächeRechteckBerechenen(4,3) == 12
