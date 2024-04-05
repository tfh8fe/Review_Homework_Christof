def widerstand20(laenge, querschnitt, leitwert):
    wider20 = laenge / leitwert / querschnitt
    return wider20

def deltawiderstand(wider20, temperatur, temperaturkoeffizient):
    deltawider = wider20 * (temperatur-20) * temperaturkoeffizient
    return deltawider

def widerstand(wider20, deltawiderstand):
    return wider20 + deltawiderstand

def absspannungsabfall(widerstand, strom):
    return widerstand * strom

def relspannungsabfall(spannung,absspannungsabfall):
    return spannung - absspannungsabfall
