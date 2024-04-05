def widerstand20(laenge, querschnitt, leitwert):
    """Widerstand bei 20 Grad berechnen1"""
    wider20 = laenge / leitwert / querschnitt
    return wider20


def deltawiderstand(wide20, temperatur, temperaturkoeffizient):
    """Widerstand bei 20 Grad berechnen2"""
    deltawider = wide20 * (temperatur - 20) * temperaturkoeffizient
    return deltawider


def widerstand(wider20, deltar):
    """Widerstand bei 20 Grad berechnen3"""
    return wider20 + deltar


def absspannungsabfall(widerstan, strom):
    """Widerstand bei 20 Grad berechnen4"""
    return widerstan * strom


def relspannungsabfall(spannung, abspannungsabfall):
    """Widerstand bei 20 Grad berechnen5"""
    return spannung - abspannungsabfall
