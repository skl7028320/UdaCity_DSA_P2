# Dutch National Flag Problem (Sorting 0, 1, 2)
## Problem description
Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal. You're not allowed to use any sorting function that Python provides.

Note: O(n) does not necessarily mean single-traversal. For e.g. if you traverse the array twice, that would still be an O(n) solution but it will not count as single traversal.

## Solution
The problem can be solved by putting all 0 in input list to the front and all 2 in input list to the back.

## Time complexity
In the worst case, the input list is only traversed once. Therefore the time complexity is O(n).

## Space complexity
The space complexity is O(1) because no extra space is used (the sorting happens in place).