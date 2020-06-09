# HTTP Router Using a Trie
## Problem description
For this exercise we are going to implement an HTTP Router like you would find in a typical web server using the Trie data structure we learned previously.

There are many different implementations of HTTP Routers such as regular expressions or simple string matching, but the Trie is an excellent and very efficient data structure for this purpose.

The purpose of an HTTP Router is to take a URL path like "/", "/about", or "/blog/2019-01-15/my-awesome-blog-post" and figure out what content to return. In a dynamic web server, the content will often come from a block of code called a handler.

## Solution
The Trie data structure used for router is similar to the one used for autocompletion. Instead of storing each char of 
a word, each part of path separated by `/` is stored in the node.

## Time complexity
Both inserting and finding operation of Trie data structure have the time complexity of O(m) where m is the number of 
path parts.

## Space complexity
Space complexity is O(1) because no auxiliary space is used.