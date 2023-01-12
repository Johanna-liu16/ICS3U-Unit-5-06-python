#!/usr/bin/env python3

# Created by: Johanna Liu
# Created on: Jan 2023
# This program converts a string to hexadecimal

import math

def decimal_converter(decimal, decimal_places):
    # rounds a number
    decimal[0] = decimal[0] * pow(10, decimal_places) + 0.5
    decimal[0] = int(decimal[0])
    decimal[0] = decimal[0] / pow(10, decimal_places)

def main():
    # takes user input, passes it to functions and calls them
    decimal = []

    print("This program rounds a number.")
    str_temp_decimal = input("Enter a number you want to round: ")
    str_decimal_places = input("Enter the number of decimal places you want rounded: ")
    
    try:
        temp_decimal = float(str_temp_decimal)
        decimal.append(temp_decimal)
        decimal_places = int(str_decimal_places)
        
        decimal_converter(decimal, decimal_places)

        print("The number rounded is: {0}".format(decimal[0]))
    except ValueError:
        print("Invalid Input")


if __name__ == "__main__":
    main()
