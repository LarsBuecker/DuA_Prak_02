import sys

from hashtable import Hashtable
from avlTree import AVL_Tree

mode = None
    
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