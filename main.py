from os import read
import sys

mode = None

class Node(object):
    def __init__(self, parent, key):
        self.key = key
        self.parent = parent
        self.left_child = None
        self.right_child = None
        self.height = None
            
class AVL_Tree(object):
    
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
        if root.left_child.height > root.right_child.height + 1:
            if root.left_child.left_child.height < root.right_child.left_child.height:
                left_rot(root.right_child)
            right_rot(root)
        elif root.right_child.height > root.left_child.height + 1:
            if root.right_child.right_child.height < root.right_child.height.left_child.height:
                right_rot(root.right_child)
            left_rot(root)

    def insert(self, root, key):
        if not root:
            return Node(root, key)
        elif key < root.key:
            root.left_child = self.insert(root.left_child, key)
        elif key > root.key:
            root.right_child = self.insert(root.right_child, key)
        elif root.key == key:
            return
        root.height = 1 + max(self.root.left_child.height, self.root.right_child.height)
        balance(root)

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
            if not AVL_tree.insert(root, c[1]):
                print("ins false")
            else:
                print("ins true")
            