import sys

mode = None

def read_file():
    file = open(sys.argv[])

if __name__ == "__main__":
    if sys.argv[len(1] == "-avl":
        mode = "avl"
    elif sys.argv[1] == "-hash":
        mode = "hash"
    else:
        print("Undefinded mode use -avl or -hash")
        exit()