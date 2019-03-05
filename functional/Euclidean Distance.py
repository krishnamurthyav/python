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

distance = FunctionalCode


class Distance:
    flag = 0
    while flag == 0:
        try:
            pointX = float(input("Enter The value of X :"))  # reading input as float
            type(pointX) == float
            flag = 1
        except:
            print("Enter valid number")
            continue

    while flag == 1:
        try:
            pointY = float(input("Enter The value of Y :"))  # reading input as float
            type(pointY) == float
            flag = 2
        except:
            print("Enter valid value")
            continue

    try:
        distance.findEuclideanDistance(pointX, pointY)  # calling function
    except ValueError:
        print("oops Something Went Wrong......... Please Provide Only Float Values........")
