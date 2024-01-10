#!/usr/bin/python3
"""
Module to divide all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Function to divide all elements of a matrix by a number

    Args:
        matrix (list of lists): Matrix of integers or floats
        div (int or float): Number to divide the elements of the matrix by

    Returns:
        list of lists: New matrix with elements divided by div

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                   if each row of the matrix doesn't have the same size,
                   or if div is not a number
        ZeroDivisionError: If div is equal to 0
    """
    # Check if matrix is a list of lists of integers or floats
    if not all(isinstance(row, list) and all(isinstance(el, (int, float)) for el in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if each row of the matrix has the same size
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide all elements of the matrix by div, rounded to 2 decimal places
    new_matrix = [[round(el / div, 2) for el in row] for row in matrix]

    return new_matrix


if __name__ == "__main__":
    # Example usage
    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    print(matrix_divided(matrix, 3))
    print(matrix)

