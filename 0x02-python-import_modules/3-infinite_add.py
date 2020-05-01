#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) - 1 > 0:
        sum = 0
        for n in range(1, (len(sys.argv))):
            sum += int(sys.argv[n])
        print(("{:d}".format(sum)))
    else:
        print("0")
