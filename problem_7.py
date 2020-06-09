# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, root_handler, not_found_handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()
        self.root.handler = root_handler
        self.not_found_handler = not_found_handler

    def insert(self, splitted_path, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current_node = self.root
        for path_part in splitted_path:
            if path_part == "":
                continue
            if path_part not in current_node.children:
                current_node.insert(path_part)
            current_node = current_node.children[path_part]

        current_node.handler = handler

    def find(self, splitted_path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current_node = self.root
        for path_part in splitted_path:
            if path_part == "":
                continue
            if path_part in current_node.children:
                current_node = current_node.children[path_part]
            else:
                return self.not_found_handler

        if current_node.handler is not None:
            return current_node.handler
        else:
            return self.not_found_handler


# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = None

    def insert(self, path_part):
        # Insert the node as before
        self.children[path_part] = RouteTrieNode()


# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, root_handler, not_found_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.route_tree = RouteTrie(root_handler, not_found_handler)

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        splitted_path = self.split_path(path)

        self.route_tree.insert(splitted_path, handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        if path == "":
            return "empty path"
        if path[0] != "/":
            return "invalid path"

        splitted_path = self.split_path(path)

        handler = self.route_tree.find(splitted_path)

        return handler

    def split_path(self, path):
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        splitted_path = path.split("/")

        return splitted_path


# Here are some test cases and expected outputs you can use to test your implementation
# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler") # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("")) # test empty path input, should return 'empty path'
print(router.lookup("home/about")) # test invalid path input, should return 'invalid path'
