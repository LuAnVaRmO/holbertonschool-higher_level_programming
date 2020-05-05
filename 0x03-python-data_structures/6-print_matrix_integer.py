#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix != [[]]:
        for i in matrix:
            for j in i:
                if j == len(i) or j == len(i) + 3 or j == len(i) + 6:
                    print("{:d}".format(j), end='')
                else:
                    print("{:d}".format(j), end=' ')
            print(end="\n")
    else:
        print(end="\n")
