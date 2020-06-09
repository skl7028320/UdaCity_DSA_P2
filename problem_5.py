## Represents a single node in the Trie
class TrieNode:
    ## Initialize this node in the Trie
    def __init__(self):
        self.children = {}
        self.is_word = False

    ## Recursive function that collects the suffix for
    ## all complete words below this point
    def suffixes(self, suffix = ''):
        if self.is_word:
            if suffix != '':
                yield suffix

        for char, node in self.children.items():
            yield from node.suffixes(suffix + char)


## The Trie itself containing the root node and insert/find functions
class Trie:
    ## Initialize this Trie (add a root node)
    def __init__(self):
        self.root = TrieNode()
        self.is_word = False

    ## Add a word to the Trie
    def insert(self, word):
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
                current_node = current_node.children[char]
            else:
                current_node = current_node.children[char]

        current_node.is_word = True

    ## Find the Trie node that represents this prefix
    def find(self, prefix):
        current_node = self.root

        for char in prefix:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return None

        return current_node


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

# Test 1
print('Test 1: auto completion of "a"')
prefix_node = MyTrie.find("a")
suffix_list = []
for suffix in prefix_node.suffixes():
    suffix_list.append(suffix)
print("Pass" if suffix_list == ['nt', 'nthology', 'ntagonist', 'ntonym'] else "Fail")

# Test 2
print('\nTest 2: auto completion of "fun"')
prefix_node = MyTrie.find("fun")
suffix_list = []
for suffix in prefix_node.suffixes():
    suffix_list.append(suffix)
print("Pass" if suffix_list == ['ction'] else "Fail")

# Test 3
print('\nTest 3: auto completion of "trie"')
prefix_node = MyTrie.find("trie")
suffix_list = []
for suffix in prefix_node.suffixes():
    suffix_list.append(suffix)
print("Pass" if suffix_list == [] else "Fail")
