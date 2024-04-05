from utils import flaecheRechteck


def test_flächeRechteckBerechenen():
    assert flaecheRechteck(3, 4) == 7
    assert flaecheRechteck(10, 10) == 20
    assert flaecheRechteck(4, 3) == 7
