# Rotate String Checker
## Overview
This project includes a Python class `Solution` which contains a method `rotateString` that checks if one string can become another string after some number of shifts. A shift consists of moving the leftmost character of the string to the rightmost position.

## Features
* Checks if one string can be rotated to become another string.
* Efficiently determines the result using string concatenation and substring checking.

## Requirements
* Python 3.x

## Usage
* To use the `rotateString` method, first import the `Solution` class, create an instance of it, and then call the `rotateString` method with two strings as arguments.

## Implementation Details
* The method `rotateString` first checks if the lengths of the two strings are equal.
* It then concatenates the first string with itself and checks if the second string is a substring of this concatenated string.
* This approach ensures an efficient check with a time complexity of O(n).

_