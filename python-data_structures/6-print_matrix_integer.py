#!/usr/bin/python3
# map func to convert the row to a string, then we
# apply the join func to this whole row which
# converts it all to a single string and separate
# elements by the separator specified
def print_matrix_integer(matrix=[[]]):
    for line in matrix:
        print(" ".join(map(str, line)))
