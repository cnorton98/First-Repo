# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 20:02:23 2021

@author: cnorton1
"""

""" This program converts an amount of gold given in lbs and ounces to grams and kilograms. """
""" Additionally, this program will give the user the total value of the amount of entered gold."""

# The following three lines is given information
Price = 1868.40
Ounce = 28.35
Pound = 453.59

# Inputs
pounds = float(input("Enter the amount of Gold in Pounds: "))
ounces = float(input("Enter the amount of Gold in Ounces: "))

# Conversion formulas so that the output will tel lthe user how many grams of gold they have
weight_in_ounces = (pounds * 16) + ounces
weight_in_grams = weight_in_ounces * Ounce
weight_in_kilos = weight_in_grams / 1000
# This formula will tell the user how much their amount of gold is worth in ounces
total_cost = weight_in_ounces * 1868.40

# Outputs
print("-" * 25)
print(f"The total weight is {weight_in_grams:.2f} grams or {weight_in_kilos:.2f} kilograms")
print(f"The total cost of {weight_in_ounces:.2f} ounces of gold is ${total_cost:.2f}")

# This formula converts the price of the gold in ounces to grams
cost_gram = Price // Ounce

# More output
print("-" * 25)
print(f"Cost per ounce = ${Price:.2f}")
print(f"Cost per gram = ${cost_gram:.2f}")
