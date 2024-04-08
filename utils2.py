"""
This module defines the functions required for calculating net present value.
The parameters are defined in main.py
"""


def calc_self_consumption(installed_capacity, full_load_hours):
    """Calculation of self-consumption per yeaar with the assumption that
    50% of the energy generated is consumed"""
    self_consumption = installed_capacity * full_load_hours * 0.5
    return self_consumption


def calc_annual_costs(annual_load, self_consumption, supply_tarif):
    """Calculation of annual electricity costs"""
    annual_costs = (annual_load - self_consumption) * supply_tarif
    return annual_costs


def calc_annual_revenues(self_consumption, feedin_tarif):
    """Calculation of annual revenues"""
    annual_revenues = self_consumption * feedin_tarif
    return annual_revenues
