def calc_crf(int_rate, lifetime):
    """Calculation of capital ercovery factor"""
    crf = ((1 + int_rate) * lifetime * int_rate) / ((1 + int_rate) * (lifetime - 1))
    return crf
