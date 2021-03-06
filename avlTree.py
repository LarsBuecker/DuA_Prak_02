# Reprensentation of a node in an avl tree
# fields: key, left_child, right_child. height
class Node():
    def __init__(self, key):
        self.key = key
        self.left_child = None
        self.right_child = None
        self.height = 1

# Provides methods for avl tree managment
class AVL_Tree():
    
    # Perform a left rotation around x as pivot point
    # Return the new root node of the subtree
    def left_rot(self, x: Node) -> Node:
        y = x.right_child
        T2 = y.left_child
        y.left_child = x
        x.right_child = T2

        # recalculate heights
        x.height = 1 + max(self.getHeight(x.left_child),
                           self.getHeight(x.right_child))
        y.height = 1 + max(self.getHeight(y.left_child),
                           self.getHeight(y.right_child))
        
        return y

    # Perfom a right rotation around x as pivot point
    # Return the new root node of the subtree
    def right_rot(self, x):
        y = x.left_child
        T3 = y.right_child
        y.right_child = x
        x.left_child = T3

        # recalculate heights
        x.height = 1 + max(self.getHeight(x.left_child),
                           self.getHeight(x.right_child))
        y.height = 1 + max(self.getHeight(y.left_child),
                           self.getHeight(y.right_child))
        return y
    
    # calculates and returns the balance factor of the tree
    def balance(self, root) -> int:
        if not root:
            return 0
        return self.getHeight(root.left_child) - self.getHeight(root.right_child)

    # inserts a new Node into the tree if the key is not already in the tree
    def insert(self, root, key):        
        if not root:
            # The key is not in the tree -> add a new node to the tree
            print("ins true")
            return Node(key)
        elif key == root.key:
            #The key was found in the tree -> dont add the node
            print("ins false")
            pass
        elif key < root.key:
            # if the key is less than the key of the current node insert the new node at the left child
            root.left_child = self.insert(root.left_child, key)
        else:
            # ifthe key is greater than the key of the current node insert the new node at the right child
            root.right_child = self.insert(root.right_child, key)

        # Reset the height of the node of the current recusion depth
        root.height = 1 + max(self.getHeight(root.left_child),
                              self.getHeight(root.right_child))

        # rebalance the tree
        balanceFactor = self.balance(root)
        if balanceFactor > 1:
            if key < root.left_child.key:
                return self.right_rot(root)
            else:
                root.left_child = self.left_rot(root.left_child)
                return self.right_rot(root)

        if balanceFactor < -1:
            if key > root.right_child.key:
                return self.left_rot(root)
            else:
                root.right_child = self.right_rot(root.right_child)
                return self.left_rot(root)

        return root

    # Delete a node from the tree if the key is in the tree
    def delete(self, root, key):
        if not root:
            # The key wasnt found in the tree
            print("del false")
            return root
        elif key < root.key:
            # recursive searching in the left subtree
            root.left_child = self.delete(root.left_child, key)
        elif key > root.key:
            # recursive searching in the right subtree
            root.right_child = self.delete(root.right_child, key)
        else:
            # Key was found in the tree -> delete the node 
            if root.left_child is None:
                # Delete the right node if the left node was none
                print("del true")
                tmp = root.right_child
                root = None
                return tmp
            elif root.right_child is None:
                # Delete the left nide if the right node was none
                print("del true")
                tmp = root.left_child
                root = None
                return tmp
            tmp = self.getMinValueNode(root.right_child)
            root.key = tmp.key
            root.right_child = self.delete(root.right_child, tmp.key)
            
        # recursion termination
        if root is None:
            return root
        
        # recalculate the height
        root.height = 1 + max(self.getHeight(root.left_child),
                              self.getHeight(root.right_child))

        # reballance the tree
        balance = self.balance(root)
        if balance > 1: 
            if self.balance(root.left_child) >= 0:
                return self.right_rot(root)
            else:
                root.left = self.left_rot(root.left_child)
                return self.right_rot(root)
        if balance < -1:
            if self.balance(root.right_child) <= 0:
                return self.left_rot(root)
            else:
                root.right_child = self.right_rot(root.right_child)
                return self.left_rot(root)
        return root
    

    # search a key in the tree
    def search(self, root, key):
        if not root:
            # the key was not found in the tree
            print("search false")
            return root
        if key == root.key:
            # found the key in the tree
            print("search true")
            return root
        elif key < root.key:
            # search in the left subtree from node as root
            self.search(root.left_child, key)
        elif key > root.key:
            # search in the right subtree from node as root
            self.search(root.right_child, key)
        
        # recursion termination
        if root is None:
            return root
        
        # recalculate height
        root.height = 1 + max(self.getHeight(root.left_child),
                              self.getHeight(root.right_child))

        return root
        
    # returns the height of a given node
    # return 0 if the node is none
    def getHeight(self, root):
        if not root:
            return 0
        return root.height
    
    # returns the node with the smallest key in the subtree from root
    def getMinValueNode(self, root):
        if root is None or root.left_child is None:
            return root
        return self.getMinValueNode(root.left_child)