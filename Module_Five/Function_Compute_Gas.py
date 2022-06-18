"""
Define a function compute_gas_volume that returns the volume of a gas given parameters pressure, temperature, and moles. Use the gas equation PV = nRT, where P is pressure in Pascals, V is volume in cubic meters, n is number of moles, R is the gas constant 8.3144621 ( J / (mol*K)), and T is temperature in Kelvin.

Sample output with inputs: 100.0 1.0 273.0
Gas volume: 22.698481533 m^3
"""

gas_const = 8.3144621

def compute_gas_volume(gas_pressure, gas_temperature, gas_moles):
    return (gas_moles * gas_const *gas_temperature) / gas_pressure

gas_pressure = float(input())
gas_moles = float(input())
gas_temperature = float(input())
gas_volume = 0.0

gas_volume = compute_gas_volume(gas_pressure, gas_temperature, gas_moles)
print('Gas volume:', gas_volume, 'm^3')
