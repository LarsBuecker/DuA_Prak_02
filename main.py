import sys

from hashtable import Hashtable
from avlTree import AVL_Tree

# GLOBALS ----------------- #
mode = None

# Reads the data from input file and stores the data in a command buffer
# The Layout of the command buffer is: [(<command>, <key>), ...]
def read_file():
    command_buffer = []
    # open the file
    file = open(sys.argv[ len(sys.argv) - 1 ], "r")

    # loop linewise through the input file
    for line in file:
        # split up the line at blanks
        tokens = line.split(" ")

        # check for commands in the input file
        if tokens[0] == "#":
            continue

        # remove the new line char ("\n") from the key
        entry = tokens[1]
        entry = entry[:-1]

        # append the command and the key to the command buffer
        command_buffer.append((tokens[0], entry))
    file.close()
    
    return command_buffer

if __name__ == "__main__":
    # check and set the mode for dictionary
    if sys.argv[1] == "-avl":
        mode = "avl"
    elif sys.argv[1] == "-hash":
        mode = "hash"
    else:
        print("Undefinded mode use -avl or -hash")

    # Get the command buffer from input file
    command_buffer = read_file()
    
    if mode == "avl":
        # Run commands from command buffer in avl mode
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
        # Run commands from command buffer in hash mode
        hashtable = Hashtable()
        for c in command_buffer:
            if c[0] == "ins":
                hashtable.insert(c[1])
            if c[0] == "del":
                hashtable.delete(c[1])
            if c[0] == "search":
                hashtable.search(c[1])