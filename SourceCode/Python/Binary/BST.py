#/* *** ODSATag: BST *** */
class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None


class BST:
    def __init__(self):
        self.root = None

    # Inserts a new key to the BST
    def insert(self, key):
    def __inserthelp(self, node, key):

    # Check if a key is in the BST
    def find(self, key):
    def __findhelp(self, node, key):

    # Removes a key from the BST
    def remove(self, key):
    def __removehelp(self, node, key):

    # Finds/removes the greatest key value from the BST
    def __getmax(self, node):
    def __removemax(self, node):
#/* *** ODSAendTag: BST *** */

#/* *** ODSATag: find *** */
def find(self, key):
    return self.__findhelp(self.root, key) 
    
    
def __findhelp(self, node, key):
    if node == None:
        return False
    elif node.key > key:
        return self.__findhelp(node.left, key)
    elif node.key < key:
        return self.__findhelp(node.right, key)
    else:
        return True
#/* *** ODSAendTag: find *** */

#/* *** ODSATag: insert *** */
def insert(self, key):
    self.root = self.__inserthelp(self.root, key)
    
    
def __inserthelp(self, node, key):
    if node == None:
        node = Node(key)
    elif node.key > key:
        node.left = self.__inserthelp(node.left, key)
    elif node.key < key:
        node.right = self.__inserthelp(node.right, key)
    return node
#/* *** ODSAendTag: insert *** */

#/* *** ODSATag: remove *** */
def remove(self, key):
    self.root = self.__removehelp(self.root, key)
    
    
def __removehelp(self, node, key):
    if node == None:
        return None
    elif node.key > key:
        node.left = self.__removehelp(node.left, key)
    elif node.key < key:
        node.right = self.__removehelp(node.right, key)
    else:
        if node.left == None:
            return node.right
        elif node.right == None:
            return node.left
        else:
            node.key = self.__getmax(node.left)
            node.left = self.__removemax(node.left)
    return node
#/* *** ODSAendTag: remove *** */

#/* *** ODSATag: getmax *** */
def __getmax(self, node):
    if node.right == None:
        return node.key
    else:
        return self.__getmax(node.right)
#/* *** ODSAendTag: getmax *** */


#/* *** ODSATag: removemax *** */
def __removemax(self, node):
    if node.right == None:
        return node.left
    node.right = self.removemax(node.right)
    return node
#/* *** ODSAendTag: removemax *** */

  
