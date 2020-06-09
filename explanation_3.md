# Rearrange Array Digits
## Problem description
Rearrange Array Elements so as to form two number such that their sum is maximum. Return these two numbers. You can assume that all array elements are in the range [0, 9]. The number of digits in both the numbers cannot differ by more than 1. You're not allowed to use any sorting function that Python provides and the expected time complexity is O(nlog(n)).

for e.g. [1, 2, 3, 4, 5]

The expected answer would be [531, 42]. Another expected answer can be [542, 31]. In scenarios such as these when there are more than one possible answers, return any one.

## Solution
1. Sort the input list using Merge Sort in descending order.
2. Use the largest number from sorted list as the most front digit of the output two numbers until all numbers are consumed.

## Time complexity
The time complexity of the first step is O(nlog(n)). The second step has the time complexity in the order of O(n). 
Therefore the overall time complexity is O(nlog(n) + n) which can be approximated to O(nlog(n))

## Space complexity
The auxiliary space needed is O(n) because of Merge Sort.