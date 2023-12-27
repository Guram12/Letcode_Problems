# Plus One

## Description
* The plusOne function is part of the Solution class. It is designed to increment a number represented as an array of digits by one. The digits are stored such that the most significant digit is at the head of the list. For example, the number 123 would be represented as [1, 2, 3]. This function handles carrying over when digits are incremented beyond 9.

## Features
* Handles large numbers that may not fit in standard integer types.
Correctly manages carrying over for numbers ending in 9.
Works with an array of any size.

## Usage
* Import the Class: First, import the Solution class from the script.
* Create an Instance: Instantiate an object of the Solution class.
* Call the Method: Call the plusOne method with a list of digits.

## Methodology

### The plusOne method executes the following steps:

* Converts the list of digits into a string.
* Converts this string to an integer.
* Increments the integer by one.
* Converts the incremented integer back to a string.
* Splits this string into individual characters.
* Converts each character back to an integer and stores them in a list.
* Returns the final list.