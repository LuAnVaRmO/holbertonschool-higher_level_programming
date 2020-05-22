#!/usr/bin/python3
"""
matrix_divided
This function divide by <div> a <matrix> of integers
return <matrix> / <div>
"""


def matrix_divided(matrix, div):
    """
    :param matrix: contain matrix of matrix of integers
    :param div: number to divide each element of the matrix
    :return: each_element / div
    """
    # Verifying type of <div> and != 0
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    # Verifying type of values of the matrix is int or floats
    if type(matrix) != list or type(matrix[0]) != list:
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    for row in range(0, len(matrix)):
        for col in range(0, len(matrix[0])):
            if type(matrix[row][col]) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists)"
                                " of integers/floats")
    for row in range(0, len(matrix)):
        if len(matrix[0]) != len(matrix[row]):
            raise TypeError("Each row of the matrix must have the same size")
    # Creating a new matrix to return
    new_matrix = [x[:] for x in matrix]
    for row in range(0, len(new_matrix)):
        for col in range(0, len(new_matrix[0])):
            new_matrix[row][col] = round(new_matrix[row][col] / div, 2)
    return new_matrix
