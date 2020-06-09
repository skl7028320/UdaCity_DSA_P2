# Square Root of an Integer
## Problem description
Find the square root of the integer without using any Python library. You have to find the floor value of the square root.

For example if the given number is 16, then the answer would be 4.

If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5.

The expected time complexity is O(log(n)).

## Solution
The problem can be solved as finding the integer `i` which makes the input `number` lies between square of `i` 
(inclusively) and square of `i + 1` (exclusively). The naive approach is to starting from 0, check every integer by 
incrementing 1 until find the answer. More efficient approach is using binary search where the search space is 
originally from `0` to input `number`.

## Time complexity
For the naive approach, an array of size sqrt(n) is traversed once. Therefore the time complexity is O(sqrt(n)).

For the binary search approach, the time complexity is O(log(n)).

## Space complexity
For both naive and binary search approaches, extra used spaces are constant.