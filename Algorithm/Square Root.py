"""
******************************************************************************
* Purpose:  compute the square root of a nonnegative number c given in the
            input using Newton's method
* @author:  Krishna Murthy A V
* @version: 1.2
* @since:   28-2-2019
*
******************************************************************************
"""

from Utilities.utility import FunctionalCode
obj =FunctionalCode

class SquareRoot:
    try:
        print("Enter The Non-Negative Number:")
        num = int(input())

        while num <= 0:
            num = int(input("Please Provide Valid Value(Positive Number)\n"))
        obj.findSquareRoot(num)
    except ValueError:
        print("-------Please Provide Valid input(Positive Number)")