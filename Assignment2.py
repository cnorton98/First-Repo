# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 14:07:40 2021

@author: cnorton1
"""

"""This is POS program of a mattress firm that provides the price to the customer of any mattress combination desired,
I completed this work individually."""

print("Welcome! Please enter the characters that correspond to your desired selections below, thanks!")

# Asking for what brand of mattress
brand = int(input("Please select your mattress brand (1 for Sealy, 2 for Simmons): "))
if brand == 1:
    sealy_size = input("Please select the size (K = King, Q = Queen, T = Twin): ").upper()
elif brand == 2:
    simmons_size = input("Please select the size (K = King, Q = Queen, F = Full): ").upper()
elif brand != 1 or 2:
    brand = int(input("Please select your mattress brand (1 for Sealy, 2 for Simmons): "))

# Asking for what size of Sealy mattress
if sealy_size == "K":
    sealy_king_comfort = input("Please select the comfort level (M = Medium, F = Firm, E = Extra Firm): ").upper()
elif sealy_size == "Q":
    sealy_queen_comfort = input("Please select the comfort level (M = Medium, F = Firm, E = Extra Firm): ").upper()
elif sealy_size == "T":
    sealy_twin_comfort = input("Please select the comfort level (M = Medium, F = Firm, E = Extra Firm): ").upper()
elif sealy_size != "K, Q, T":
    sealy_size = input("Please select the size (K = King, Q = Queen, T = Twin): ").upper()

# Asking for what size of Simmmons mattress
if simmons_size == "K":
    simmons_king_comfort = input("Please select the comfort level (M = Medium, F = Firm, E = Extra Firm): ").upper()
elif simmons_size == "Q":
    simmons_queen_comfort = input("Please select the comfort level (M = Medium, F = Firm, E = Extra Firm): ").upper()
elif simmons_size == "F":
    simmons_twin_comfort = input("Please select the comfort level (M = Medium, F = Firm, E = Extra Firm): ").upper()
elif simmons_size != "K, Q, F":
    simmons_size = input("Please select the size (K = King, Q = Queen, F = Full): ").upper()

# Asking whether or no the customer likes box springs
if sealy_king_comfort == "M":
    sealy_king_spring = input("Do you like to have box springs (Y = Yes, N = No): ")
elif sealy_queen_comfort == "F":
    sealy_queen_spring = input("Do you like to have box springs (Y = Yes, N = No): ")
elif sealy_twin_comfort == "E":
    sealy_twin_comfort = input("Do you like to have box springs (Y = Yes, N = No): ")
elif simmons_king_comfort == "M":
    simmons_king_spring = input("Do you like to have box springs (Y = Yes, N = No): ")
elif simmons_queen_comfort == "F":
    sealy_queen_spring = input("Do you like to have box springs (Y = Yes, N = No): ")
elif simmons_twin_comfort == "E":
    sealy_full_spring = input("Do you like to have box springs (Y = Yes, N = No): ")

# Asking which shipping mode they perfer
shipping = input("Which shipping method woukd you like (S = Standard, N = Next Day): ")
if shipping == "S":
    shipping = 100
elif shipping == "N":
    shipping = 300
elif shipping != "S, N":
    shipping = input("Which shipping method woukd you like (S = Standard, N = Next Day): ")
