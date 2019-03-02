"""
******************************************************************************
* Purpose: Take in three arguments P, Y, and R from user and calculates
           the monthly payments.
* @author:  Krishna Murthy A V
* @version: 1.2
* @since:   28-2-2019
*
******************************************************************************
"""

from Utilities.utility import FunctionalCode

mp = FunctionalCode

class MonthlyPayment:
    try:
        print("Enter P value")
        p = int(input())
        while p < 0:
            p = int(input("Enter valid number"))

        print("Enter Y value")
        y= int(input())
        while y < 0:
            y = int(input("Enter valid number"))

        print("Enter R value")
        r = int(input())
        while r < 0:
            r = int(input("Enter valid number"))

        mp.MonthPay(p,y,r)

    except RuntimeError:
        print("Error OCcured")
