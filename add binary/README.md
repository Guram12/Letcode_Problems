# Binary Addition Solution

* This Python module provides a solution for adding two binary strings and returning their sum as a binary string. The solution accounts for binary strings of unequal lengths and ensures accurate binary addition including carry handling.

## Features

* Handles binary strings of unequal lengths by padding the shorter string with leading zeros.
* Supports binary addition with carry over for accurate calculations.
* Returns the sum of two binary strings as a binary string.

## Usage

* To use this solution, include the Solution class in your Python script. Then, instantiate an object of the Solution class and call the addBinary method with two binary strings as arguments.

### Implementation Details

* The Solution class contains a single method addBinary, which performs the following steps:


* Padding: The shorter binary string is padded with leading zeros to match the length of the longer string.

* Addition: Starting from the least significant bit, the bits of both strings are added along with any carry from the previous addition.
* Carry Handling: The carry is calculated for each addition and propagated to the next most significant bit.
* Result Construction: The result is built bit by bit in a reverse order and then reversed to represent the correct binary sum.
* Final Carry: If there is a carry left after the final addition, it is added to the result.

### Requirements

* Python 3.x
