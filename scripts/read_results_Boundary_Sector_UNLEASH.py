# -*- coding: utf-8 -*-
"""
Minimalist example file showing how to read the results of a Dispa-SET run

@author: Sylvain Quoilin
"""

# Add the root folder of Dispa-SET to the path so that the library can be loaded:
import sys,os
sys.path.append(os.path.abspath('..'))

# Import Dispa-SET
import dispaset as ds

# Load the inputs and the results of the simulation
inputs,results = ds.get_sim_results(path='../Simulations/simulation_(2)_BE-NUC',cache=False)

# if needed, define the plotting range for the dispatch plot:
import pandas as pd
rng = pd.date_range(start='2023-10-01',end='2023-10-10',freq='h')

# Generate country-specific plots
ds.plot_zone(inputs,results)

# Bar plot with the installed capacities in all countries:
cap = ds.plot_zone_capacities(inputs,results)

# Bar plot with the energy balances in all countries:
ds.plot_energy_zone_fuel(inputs,results,ds.get_indicators_powerplant(inputs,results))

# Analyse the results for each country and provide quantitative indicators:
r = ds.get_result_analysis(inputs,results)

# Test the new boundary sector dispatch plot
ds.plot_dispatchX(inputs, results)
