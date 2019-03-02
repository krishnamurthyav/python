"""
******************************************************************************
* Purpose:  Takes two integer from user x and y and prints the Euclidean
              distance from the point (x, y) to the origin (0, 0).
* @author:  Krishna Murthy A V
* @version: 1.0
* @since:   28-2-2019
*
******************************************************************************
"""

from Utilities.utility import FunctionalCode

obj = FunctionalCode

class Distance:
    try:
        print("Enter The value of X :")
        x = float(input())
        print("Enter The value of Y :")
        y = float(input())

        while x < 0.0:
            x = float(input("Please Provide valid Input X"))

        while y < 0.0:
            y = float(input("Please Provide valid Input Y"))

        obj.findEuclideanDistance(x, y)
    except ValueError:
        print("oops Something Went Wrong......... Please Provide Only Float Values........")