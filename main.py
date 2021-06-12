from os import read
import sys

mode = None

class Node(object):
    def __init__(self, key, parent, left_child, right_child, height):
        self.key = key
        self.parent = parent
        self.left_child = left_child
        self.right_child = right_child
        self.height = height
            
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

def read_file():
    command_buffer = []
    file = open(sys.argv[ len(sys.argv) - 1 ], "r")
    for line in file:
        tokens = line.split(" ")
        if tokens[0] == "#":
            continue
        command_buffer.append((tokens[0], tokens[1]))
    print("Commandbuffer: " + str(command_buffer))

    #Node.left_rot(T, x)

    return command_buffer

if __name__ == "__main__":
    if sys.argv[1] == "-avl":
        mode = "avl"
    elif sys.argv[1] == "-hash":
        mode = "hash"
    else:
        print("Undefinded mode use -avl or -hash")

    read_file()