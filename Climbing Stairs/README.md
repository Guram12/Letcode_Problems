# Climbing Stairs Solution

## Description
* This Python script contains a solution to the "Climbing Stairs" problem. The problem is as follows: given n steps in a staircase, you can climb the stairs by taking either one step or two steps at a time. The goal is to find out how many distinct ways there are to climb to the top of the staircase.

* The Solution class in this script provides a method climbStairs(n) that returns the number of distinct ways to reach the top of an n step staircase.

## Features
* Efficient calculation using dynamic programming.
* Handles staircases of varying sizes (value of n).
* Simple and easy to understand implementation.

## Methodology
* The climbStairs method uses a dynamic programming approach, where the number of ways to reach the current step is determined by the sum of the ways to reach the previous step and the step before that. This is because at any step, you can either come from the step right before it (one step) or from two steps before it (two steps).

* The method iterates from the third step (index 2) up to n, continuously updating the number of ways to reach the current and previous steps.

