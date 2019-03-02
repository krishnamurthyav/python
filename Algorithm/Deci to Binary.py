"""
******************************************************************************
* Purpose:  Take decimal number from user and print the conversion into
              binary.
* @author:  Krishna Murthy A V
* @version: 1.1
* @since:   1-3-2019
*
******************************************************************************
"""

from Utilities.utility import FunctionalCode

db = FunctionalCode

class DeciToBinary:
    try:
        print("enter the number ")
        n = int(input())
        while n < 0:
            n = int(input("Enter positive number only"))

        out = db.covertDecimalToBinary(n)
        print("Decimal To Binary", out)

    except RuntimeError:
        print("Something went Wrong")