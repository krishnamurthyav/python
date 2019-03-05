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

quadratic = FunctionalCode


class Quadratic_Equ:
    flag = 0
    while flag == 0:
        try:
            valueA = int(input("Enter valueA "))
            type(valueA) == int
            flag = 1
        except:
            print("Re-Enter valueA value")
            continue

    while flag == 1:
        try:
            valueB = int(input("Enter valueB "))
            type(valueB) == int
            flag = 2
        except:
            print("Re-Enter valueB value")
            continue

    while flag == 2:
        try:
            valueC = int(input("Enter valueC "))
            type(valueC) == int
            flag = 3
        except:
            print("Re_enter valueC value")
            continue

    try:
        quadratic.rootsOfEquation(valueA, valueB, valueC)

    except RuntimeError:
        print("Runtime Error")
