"""
******************************************************************************
* Purpose:  Take input from user and print the 2D matrix.
* @author:  Krishna Murthy A V
* @version: 1.1
* @since:   28-2-2019
*
******************************************************************************
"""

from Utilities.utility import FunctionalCode

ta = FunctionalCode

class TwoDArray:
    try:
        print("Enter Number of rows")
        rows = int(input())
        print("Enter Number of columns")
        cols = int(input())

        while rows < 0:
            rows = int(input("Enter positive value"))

        while cols < 0:
            cols = int(input("Enter positive value"))

        size = rows * cols
        print("Enter ", size ,"numbers")
        matrix = []

        for i in range(rows):
            row_list = []
            for j in range(cols):
                row_list.append(int(input()))

            matrix.append(row_list)

        ta.MatrixArray(matrix,rows,cols)

    except RuntimeError:
        print("Error occuer")
