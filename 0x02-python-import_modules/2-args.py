#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    l = (len(sys.argv) - 1)
    if l == 0:
        print("0 arguments.")
    elif l == 1:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    elif l > 1:
        print("{:d} arguments:".format(l))
        for count, item in enumerate(sys.argv):
            if count >= 1:
                print("{}: {}".format(count, item))
