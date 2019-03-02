""""
******************************************************************************
* Purpose:  Take a, b and c as input values to find the roots of x.
            Using formulae
            delta = b*b - 4*a*c
            Root 1 of x = (-b + sqrt(delta))/(2*a)
            Root 2 of x = (-b - sqrt(delta))/(2*a)
* @author:  Krishna Murthy A V
* @version: 1.0
* @since:   27-2-2019
*
******************************************************************************
"""

from Utilities.utility import FunctionalCode

q1 = FunctionalCode


class Quadratic_Equ:
    try:
        print("Enter the value of a ")
        a = int(input())
        print("Enter the value of b ")
        b = int(input())
        print("Enter the value of c ")
        c = int(input())

        q1.rootsOfEquation(a, b, c)

    except RuntimeError:
        print("Runtime Error")
