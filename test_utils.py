from utils import widerstand20
from utils import deltawiderstand
from utils import widerstand
from utils import absspannungsabfall
from utils import relspannungsabfall


def test_widerstand20():
    """Test Widerstand 20 Grad"""
    assert widerstand20(1, 1, 1) == 1


def test_deltawiderstand():
    """Test deltaWiderstand"""
    assert deltawiderstand(1, 0, 1) == 0


def test_widerstand():
    """Test Widerstand bei angegebener Temperatur"""
    assert widerstand(1, 1) == 2


def test_absspannungsabfall():
    """Test Spannungsabfall"""
    assert absspannungsabfall(1, 1) == 1


def test_relspannungsabfall():
    """Test relativen Spannungsabfall"""
    assert relspannungsabfall(1, 1) == 0
