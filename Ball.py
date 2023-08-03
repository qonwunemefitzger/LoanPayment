# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 00:35:13 2023

@author: 16614
"""

def calculate_max_height(v0, g):
    # Using the kinematic equation: h_max = (v0^2) / (2 * g)
    h_max = (v0 ** 2) / (2 * g)
    return h_max

def main():
    try:
        v0 = float(input("Enter the initial velocity of the ball (ft/sec): "))
        g = 32.8  # Acceleration due to gravity in ft/sec^2

        if v0 < 0:
            raise ValueError("Initial velocity must be a positive value.")

        max_height = calculate_max_height(v0, g)
        print(f"The maximum height the ball reaches is {max_height:.2f} feet.")
    except ValueError as e:
        print(f"Error: {e}. Please enter a valid positive number for the initial velocity.")

if __name__ == "__main__":
    main()
