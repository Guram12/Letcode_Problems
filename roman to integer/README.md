# Roman Numeral to Integer Converter
## Overview
This project includes a Python class Solution which contains a method romanToInt that converts a string representing a Roman numeral into its integer equivalent. This method is particularly useful for understanding Roman numerals and their usage in modern computing contexts.

## Features
* Converts Roman numerals to integers.
* Handles subtractive notation (e.g., IV for 4, IX for 9).
* Supports all standard Roman numeral symbols (I, V, X, L, C, D, M).

## Requirements
* Python 3.x

## Usage
* To use the romanToInt method, first import the Solution class, create an instance of it, and then call the romanToInt method with a Roman numeral string as an argument.

## Implementation Details
* The method romanToInt works by iterating through the string of Roman numerals from left to right.
* For each symbol, the method checks if there is a subsequent symbol and whether the current symbol is less than the next one, indicating a subtractive scenario.
* The method uses a dictionary to map Roman numeral symbols to their respective integer values.
* The total is calculated by adding or subtracting values based on the Roman numeral rules.
