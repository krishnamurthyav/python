"""
******************************************************************************
* Purpose:  Take given number and find the power of 2 of the
             the given number.
*
* @author:  Krishna Murthy A V
* @version: 1.1
* @since:   27-2-2019
*
******************************************************************************
"""

from Utilities.utility import FunctionalCode

p1 = FunctionalCode

class PowerTwo:
    try:
        print("Enter power value")
        n = int(input())
        while n < 0 or n >= 32:
            n = int(input("Enter value between 0 to 31"))

        p1.power_Of_two(n)

    except RuntimeError:
        print("Error occured")