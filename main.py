from os import read
import sys

mode = None

class Node():
    def __init__(self, parent, key):
        self.key = key
        self.parent = parent
        self.left_child = None
        self.right_child = None
        self.height = None
            
class AVL_Tree():
    
    def left_rot(self, x):
        y = x.right_child
        T = y.left_child

        y.left_child = x
        x.right_child = T

        return y

    def right_rot(self, x):
        y = x.left_child
        T = y.right_child

        y.right_child = x
        x.left_child = T

        return y
    
    def balance(self, root):
        if self.getHeight(root.left_child) > self.getHeight(root.right_child) + 1:
            if root.left_child.left_child.height < root.right_child.left_child.height:
                self.left_rot(root.right_child)
            self.right_rot(root)
        elif self.getHeight(root.right_child) > self.getHeight(root.left_child) + 1:
            if self.getHeight(root.right_child.right_child) < self.getHeight(root.right_child.height.left_child):
                self.right_rot(root.right_child)
            self.left_rot(root)

    def insert(self, root, key):
        if not root:
            return Node(root, key)
        elif key < root.key:
<<<<<<< Updated upstream
            root.left_child = self.insert(root.left_child, key)
        elif key > root.key:
            root.right_child = self.insert(root.right_child, key)
        elif root.key == key:
            return
        root.height = 1 + max(self.root.left_child.height, self.root.right_child.height)
        balance(root)
=======
            self.insert(root.left_child, key)
        elif key > root.key:
            self.insert(root.right_child, key)
        else:
            return
        root.height = 1 + max(self.getHeight(root.left_child), self.getHeight(root.right_child))
        self.balance(root)
    
    def getHeight(self, root):
        if not root:
            return 0
        return root.height
>>>>>>> Stashed changes

def read_file():
    command_buffer = []
    file = open(sys.argv[ len(sys.argv) - 1 ], "r")
    for line in file:
        tokens = line.split(" ")
        if tokens[0] == "#":
            continue
        command_buffer.append((tokens[0], tokens[1]))
    print("Commandbuffer: " + str(command_buffer))
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
    AVL_tree = AVL_Tree()
    root = None

    for c in command_buffer:
        if c[0] == "ins":
<<<<<<< Updated upstream
            if not AVL_tree.insert(root, c[1]):
=======
            print(c[1])
            root = AVL_tree.insert(root, c[1])
            if not root:
>>>>>>> Stashed changes
                print("ins false")
            else:
                print("ins true")
            