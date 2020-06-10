# Autocomplete with Tries
## Problem description
A trie is a tree-like data structure that stores a dynamic set of strings. Tries are commonly used to facilitate operations like predictive text or autocomplete features on mobile phones or web search.

## Solution
After finding the node representing the prefix, the task becomes traversing all leaves under the prefix node. Python 
Generator is used to create an iterable which returns all the suffixes (leaves).

## Time complexity
Since the subtree under the prefix node is completely traversed in order to find all leaves, the time complexity is 
O(n) where n is the number of node in the subtree.

## Space complexity
Space complexity of Trie is O(m) where m is the number of word in the Trie.