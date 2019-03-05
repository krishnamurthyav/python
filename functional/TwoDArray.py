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

array = FunctionalCode

class TwoDArray:
    flag = 0
    while flag == 0:
        try:
            rows = int(input("Enter row number"))
            while rows <= 0:
                rows = int(input("Enter correct row "))
                continue
            type(rows) == int
            flag = 1
        except:
            print("Re-Enter row number")
            continue

    while flag == 1:
        try:
            cols = int(input("Enter column "))
            while cols <= 0:
                cols = float(input("Enter valid column number"))
                type(cols) == float
                flag = 2
        except:
            print("Re-Enter column number")
            continue

    try:
        size = rows * cols
        print("Enter ", size ,"numbers")
        matrix = []

        for row in range(rows):
            row_list = []
            for col in range(cols):
                row_list.append(int(input()))
            matrix.append(row_list)

        array.MatrixArray(matrix, rows, cols)

    except RuntimeError:
        print("Error occuer")
