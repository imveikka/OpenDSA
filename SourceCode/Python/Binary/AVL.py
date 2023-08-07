#/* *** ODSATag: AVLTree *** */
class Node:
    """A node in an AVL tree."""

    def __init__(self, key, value, left = None, right = None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.update_height()

    def height(self):
        """Return the height of a tree. Also works for None."""

        if self is None:
            return 0
        else:
            return self._height

    def height_diff(self):
        """Return the height difference, left height - right height."""

        return Node.height(self.left) - Node.height(self.right)

    def update_height(self):
        """Recompute the value of the height field.
        Must be called every time the height of the tree could change."""

        self._height = max(Node.height(self.left), Node.height(self.right))+1

class AVL:
    """A dictionary implemented using a binary search tree."""

    def __init__(self):
        self.root = None

    def check_invariant(self):
        """Check that the invariant holds."""

        self.check_invariant_helper(self.root, None, None)

    @staticmethod
    def check_invariant_helper(node, lo, hi):
        """Helper method for 'check_invariant'.

        Checks that the node is the root of a valid AVL tree, and that
        all keys k satisfy lo < k < hi. The test lo < k is skipped
        if lo is None, and k < hi is skipped if hi is None."""

        if node is None: return

        if node.height_diff() > 1:
            raise AssertionError("too left-leaning")
        if node.height_diff() < -1:
            raise AssertionError("too right-leaning")

        if lo is not None and node.key <= lo:
            raise AssertionError("key too small", node.key, lo, hi)

        if hi is not None and node.key >= hi:
            raise AssertionError("key too big", node.key, lo, hi)

        # Keys in the left subtree should be < node.key
        AVL.check_invariant_helper(node.left, lo, node.key)
        # Keys in the right subtree should be > node.key
        AVL.check_invariant_helper(node.right, node.key, hi)

    def isEmpty(self):
        """Return true if there are no keys."""

        return self.root is None
    
    def size(self):
        """Return the number of keys."""

        return self.size_helper(self.root)

    @staticmethod
    def size_helper(node):
        """Helper method for 'size'."""

        if node is None: return 0
        else: return 1 + size_helper(node.left) + size_helper(node.right)

    def containsKey(self, key):
        """Return true if the key has an associated value."""

        return self.get(key) is not None

    def get(self, key):
        """Look up a key."""

        return self.get_helper(self.root, key)

    @staticmethod
    def get_helper(node, key):
        """Helper method for 'get'."""

        if node is None:
            return None
        elif key < node.key:
            return AVL.get_helper(node.left, key)
        elif key > node.key:
            return AVL.get_helper(node.right, key)
        else:
            return node.value

    def put(self, key, value):
        """Add a key-value pair, or update the value associated with
        an existing key.

        Returns the value previously associated with the key, or None
        if the key was not present."""

        self.root, old_value = self.put_helper(self.root, key, value)
        return old_value

    @staticmethod
    def put_helper(node, key, value):
        """Helper method for 'put'.

        Returns the updated node, and the value previously associated
        with the key."""

        if node is None:
            return Node(key, value, None, None), None
        elif key < node.key:
            node.left, old_value = AVL.put_helper(node.left, key, value)
            node.update_height()
        elif key > node.key:
            node.right, old_value = AVL.put_helper(node.right, key, value)
            node.update_height()
        else:
            old_value = node.value
            node.value = value
        return AVL.rebalance(node), old_value

    def remove(self, key):
        """Delete a key.

        Returns the value previously associated with the key, or None
        if the key was not present."""

        self.root, old_value = self.remove_helper(self.root, key)
        return old_value

    @staticmethod
    def remove_helper(node, key):
        """Helper method for 'remove'.

        Returns the updated node, and the value previously associated
        with the key."""

        if node is None:
            return None, None
        elif key < node.key:
            node.left, old_value = AVL.remove_helper(node.left, key)
            node.update_height()
            return AVL.rebalance(node), old_value
        elif key > node.key:
            node.right, old_value = AVL.remove_helper(node.right, key)
            node.update_height()
            return AVL.rebalance(node), old_value
        else: # key == node.key
            if node.left is None:
                return node.right, node.value
            elif node.right is None:
                return node.left, node.value
            else:
                last_node = AVL.lastNode(node.left)
                last_key = last_node.key
                last_val = last_node.value
                node.left, _ = AVL.remove_helper(node.left, last_key)
                node.key = last_key
                old_value = node.value
                node.value = last_val
                node.update_height()
                return AVL.rebalance(node), old_value

    def lastKey(self):
        """Find the largest key."""

        if self.root is None:
            return None
        else:
            last_node = self.lastNode(self.root)
            return last_node.key

    @staticmethod
    def lastNode(node):
        """Find the node having the largest key."""

        while node.right is not None:
            node = node.right

        return node

    @staticmethod
    def rebalance(node):
        if node is None: return None
        diff = node.height_diff()
        if diff == 2:
            left_diff = node.left.height_diff()
            if left_diff == -1:
                node.left = AVL.rotate_left(node.left)
                node.update_height()
            return AVL.rotate_right(node)
        elif diff == -2:
            right_diff = node.right.height_diff()
            if right_diff == 1:
                node.right = AVL.rotate_right(node.right)
                node.update_height()
            return AVL.rotate_left(node)
        else:
            return node

    @staticmethod
    def rotate_left(node):
        """
        Left rotation.

           x                y
          / \              / \
         A  y      ===>   x  C
           / \           / \
          B  C          A  B
        """

        # Variables are named according to the picture above.
        x = node
        A = x.left
        y = x.right
        B = y.left
        C = y.right

        return Node(key = y.key, value = y.value,
                    left =
                        Node(key = x.key, value = x.value,
                             left = A, right = B),
                    right = C)

    @staticmethod
    def rotate_right(node):
        """
        Right rotation.

             x             y
            / \           / \
           y  C    ===>  A  x
          / \              / \
         A  B             B  C
        """

        # Variables are named according to the picture above.
        x = node
        y = x.left
        A = y.left
        B = y.right
        C = x.right

        return Node(key = y.key, value = y.value,
                    left = A,
                    right =
                        Node(key = x.key, value = x.value,
                             left = B, right = C))

    def __iter__(self):
        """Iterate through all keys.

        This is called when the user writes 'for key in bst: ...'."""

        return self.iter_helper(self.root)

    @staticmethod
    def iter_helper(node):
        """Helper method for '__iter__'."""

        # This method is a generator:
        # https://docs.python.org/3/howto/functional.html#generators
        # Generators are an easy way to make iterators

        if node is None:
            return
        else:
            for key in AVL.iter_helper(node.left):
                yield key
            yield node.key
            for key in AVL.iter_helper(node.right):
                yield key

    def __getitem__(self, key):
        """This is called when the user writes 'x = bst[key]'."""

        return self.get(key)
    
    def __setitem__(self, key, value):
        """This is called when the user writes 'bst[key] = value'."""

        self.put(key, value)

    def __contains__(self, key):
        """This is called when the user writes 'key in bst'."""

        return self.containsKey(key)

    def __delitem__(self, key):
        """This is called when the user writes 'del bst[key]'."""

        self.remove(key)

    def __str__(self):
        """This is called to show the AVL as a string."""

        # Use a dict comprehension to convert the AVL into a dict:
        # https://docs.python.org/3/tutorial/datastructures.html#dictionaries
        # Then show the dict as a string.

        return str({key: self[key] for key in self})
        # This code is the same as:
        # d = {}
        # for key in self:
        #   d[key] = self[key]
        # return str(d)
        # Note that 'for key in self' calls self.__iter__ to produce
        # the keys, and 'self[key]' calls self.__getitem__.

    def __repr__(self):
        """This is called to show the AVL as a string."""

        return repr({key: self[key] for key in self})

# Some code to test that the AVL tree is working
if __name__ == '__main__':
    bst = AVL()
    keys = [3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6]
    values = list(range(len(keys)))

    for i in range(len(keys)):
        bst[keys[i]] = values[i]
        print(Node.height(bst.root), bst)
        bst.check_invariant()
    for i in range(len(keys)):
        print(bst[keys[i]])
        bst.check_invariant()
    for i in range(len(keys)):
        del bst[keys[i]]
        print(Node.height(bst.root), bst)
        bst.check_invariant()
#/* *** ODSAendTag: AVLTree *** */
