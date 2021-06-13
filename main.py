from os import read
import sys

mode = None

class Node():
    def __init__(self, key):
        self.key = key
        self.left_child = None
        self.right_child = None
        self.height = 1
            
class AVL_Tree():
    
    def left_rot(self, x):
        y = x.right_child
        T2 = y.left_child
        y.left_child = x
        x.right_child = T2
        x.height = 1 + max(self.getHeight(x.left_child),
                           self.getHeight(x.right_child))
        y.height = 1 + max(self.getHeight(y.left_child),
                           self.getHeight(y.right_child))
        return y

    def right_rot(self, x):
        y = x.left_child
        T3 = y.right_child
        y.right_child = x
        x.left_child = T3
        x.height = 1 + max(self.getHeight(x.left_child),
                           self.getHeight(x.right_child))
        y.height = 1 + max(self.getHeight(y.left_child),
                           self.getHeight(y.right_child))
        return y
    
    def balance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left_child) - self.getHeight(root.right_child)

    def insert(self, root, key):            
        if not root:
            print("ins true")
            return Node(key)
        elif key == root.key:
            print("ins false")
            pass
        elif key < root.key:
            root.left_child = self.insert(root.left_child, key)
        else:
            root.right_child = self.insert(root.right_child, key)

        root.height = 1 + max(self.getHeight(root.left_child),
                              self.getHeight(root.right_child))

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

    def delete(self, root, key):
        if not root:
            print("del false")
            return root
        elif key < root.key:
            root.left_child = self.delete(root.left_child, key)
        elif key > root.key:
            root.right_child = self.delete(root.right_child, key)
        else:
            if root.left_child is None:
                print("del true")
                tmp = root.right_child
                root = None
                return tmp
            elif root.right_child is None:
                print("del true")
                tmp = root.left_child
                root = None
                return tmp
            tmp = self.getMinValueNode(root.right_child)
            root.key = tmp.key
            root.right_child = self.delete(root.right_child, tmp.key)
            

        if root is None:
            return root
        
        root.height = 1 + max(self.getHeight(root.left_child),
                              self.getHeight(root.right_child))

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
    
    def search(self, root, key):
        if not root:
            print("search false")
            return root
        if key == root.key:
            print("search true")
            return root
        elif key < root.key:
            self.search(root.left_child, key)
        elif key > root.key:
            self.search(root.right_child, key)

        if root is None:
            return root
        
        root.height = 1 + max(self.getHeight(root.left_child),
                              self.getHeight(root.right_child))

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

    def getHeight(self, root):
        if not root:
            return 0
        return root.height
    
    def getMinValueNode(self, root):
        if root is None or root.left_child is None:
            return root
        return self.getMinValueNode(root.left_child)

class HashNode():
    def __init__(self, key):
        self.key = key
        self.next = None

class Hashtable():
    INITIAL_CAPACITY = 50
    # http://blog.chapagain.com.np/hash-table-implementation-in-python-data-structures-algorithms/
    def __init__(self):
        self.capacity = self.INITIAL_CAPACITY
        self.size = 0
        self.buckets = [None] * self.capacity

    def hash(self, key):
        hashsum = 0
        for i, c in enumerate(key):
            hashsum += (i + len(key)) ** ord(c)
            hashsum = hashsum % self.capacity
        
        return hashsum

    def insert(self, key):
        # 1. Increment size
        self.size += 1

        # 2. Compute index of key
        index = self.hash(key)
        node = self.buckets[index]
        
        # 3. If bucket is empty:
        if node is None:
            self.buckets[index] = HashNode(key)
            print("ins true")
            return

        
        # 4. Collision -> Iterate to the end of the linked list at provided index
        prev = node
        while node is not None:
            if key == node.key:
                print("ins false")
                return
            prev = node
            node = node.next

            # Add new node at the end of the list with provided key
        print("ins true")
        prev.next = HashNode(key)
        

    def delete(self, key):
        # 1. Compute hash
        index = self.hash(key)
        node = self.buckets[index]
        prev = None

        # 2. Iterate to the requestet node
        while node is not None and node.key != key:
            prev = node
            node = node.next
        
        # Node is requestet node or none
        if node is None:
            # Key not found
            print("del false")
            return None
        else:
            # 3. Key was found
            self.size -= 1
            # Delete the element in the linked list
            if prev is None:
                self.buckets[index] = node.next
            else:
                prev.next = prev.next.next
            
            print("del true")
            return key

    def search(self, key):
        # 1. Compute hash
        index = self.hash(key)

        # 2. Go to first node in list at bucket
        node = self.buckets[index]
        
        # 3. Traverse the linked list at this node
        while node is not None and node.key != key:
            node = node.next
        
        #4. Node is the searched one
        if node is None:
            # Not found
            print("search false")
            return None
        else:
            # Found - return node
            print("search true")
            return node
    
def read_file():
    command_buffer = []
    file = open(sys.argv[ len(sys.argv) - 1 ], "r")
    for line in file:
        tokens = line.split(" ")
        if tokens[0] == "#":
            continue
        entry = tokens[1]
        entry = entry[:-1]
        command_buffer.append((tokens[0], entry))
    #print("Commandbuffer: " + str(command_buffer))
    file.close()
    
    return command_buffer

if __name__ == "__main__":
    if sys.argv[1] == "-avl":
        mode = "avl"
    elif sys.argv[1] == "-hash":
        mode = "hash"
    else:
        print("Undefinded mode use -avl or -hash")

    command_buffer = read_file()
    
    if mode == "avl":
        AVL_tree = AVL_Tree()
        root = None

        for c in command_buffer:
            if c[0] == "ins":
                root = AVL_tree.insert(root, c[1])
            if c[0] == "del":
                root = AVL_tree.delete(root, c[1])
            if c[0] == "search":
                root = AVL_tree.search(root, c[1])
    else:
        hashtable = Hashtable()

        for c in command_buffer:
            if c[0] == "ins":
                hashtable.insert(c[1])
            if c[0] == "del":
                hashtable.delete(c[1])
            if c[0] == "search":
                hashtable.search(c[1])

            