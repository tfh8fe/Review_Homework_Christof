def widerstand20(laenge, querschnitt, leitwert):
    wider20 = laenge / leitwert / querschnitt
    return wider20

def deltawiderstand(wide20, temperatur, temperaturkoeffizient):
    deltawider = wide20 * (temperatur-20) * temperaturkoeffizient
    return deltawider

def widerstand(wider20, deltar):
    return wider20 + deltar

def absspannungsabfall(widerstan, strom):
    return widerstan * strom

def relspannungsabfall(spannung,abspannungsabfall):
    return spannung - abspannungsabfall
