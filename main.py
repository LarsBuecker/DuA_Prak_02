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

        x.height = 1 + max(self.getHeight(x.left_child), self.getHeight(x.right_child))
        y.height = 1 + max(self.getHeight(y.left_child), self.getHeight(y.right_child))

        return y

    def right_rot(self, x):
        y = x.left_child
        T = y.right_child

        y.right_child = x
        x.left_child = T

        x.height = 1 + max(self.getHeight(x.left_child), self.getHeight(x.right_child))
        y.height = 1 + max(self.getHeight(y.left_child), self.getHeight(y.right_child))

        return y
    
    def balance(self, root):
        if self.getHeight(root.left_child) > self.getHeight(root.right_child) + 1:
            if self.getHeight(root.left_child.left_child) < self.getHeight(root.right_child.left_child):
                self.left_rot(root.right_child)
            self.right_rot(root)
        elif self.getHeight(root.right_child) > self.getHeight(root.left_child) + 1:
            if self.getHeight(root.right_child.right_child) < self.getHeight(root.right_child.left_child):
                self.right_rot(root.right_child)
            self.left_rot(root)

    def insert(self, root, key):
        if not root:
            return Node(root, key)
        elif key < root.key:
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
            #print(c[1])
            root = AVL_tree.insert(root, c[1])
            if not root:
                print("ins false")
            else:
                print("ins true")
            