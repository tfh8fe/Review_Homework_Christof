from utils import flaecheRechteck


def test_flächeRechteckBerechenen():
    assert flaecheRechteck(3,4) == 12
    assert flaecheRechteck(10,10) == 100
    assert flaecheRechteck(4,3) == 12
