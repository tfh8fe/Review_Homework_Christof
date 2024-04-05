from utils import widerstand20


def test_widerstand20():
    """Widerstand bei 20 Grad berechnen"""
    assert widerstand20(1, 1, 1) == 1
