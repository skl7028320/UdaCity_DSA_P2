# Search in a Rotated Sorted Array
## Problem description
You are given a sorted array which is rotated at some random pivot point.

Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]

You are given a target value to search. If found in the array return its index, otherwise return -1.

You can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of O(log n).

Example:

Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4

## Solution
1. First find the pivot.
2. Divide input list into two sub-lists separated by pivot.
3. Search the target value in either left or right sub-list depending on where the target value lies using binary search.

## Time complexity
The time complexity of first step is in the order of O(log(n)). The second step has time complexity of O(1). The final 
step is binary search which takes O(log(n)) time. Therefore the overall time complexity is in the order of O(log(n)).

## Space complexity
The space complexity O(logn).

Reference:  https://www.ideserve.co.in/learn/time-and-space-complexity-of-recursive-algorithms

To conclude, space complexity of recursive algorithm is proportional to maximum depth of recursion tree generated. If 
each function call of recursive algorithm takes O(m) space and if the maximum depth of recursion tree is 'n' then space 
complexity of recursive algorithm would be O(nm). In the case of this problem, each call uses O(1) space, the maximum 
depth of the recursive tree is O(logn) so the space complexity is O(logn).