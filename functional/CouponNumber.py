"""
******************************************************************************
* Purpose:  Given N distinct number and print the distinct coupon number.
* @author:  Krishna Murthy A V
* @version: 1.0
* @since:   27-2-2019
*
******************************************************************************
"""

from Utilities.utility import FunctionalCode

cn = FunctionalCode


class Coupon_Code:
    try:
        print("Enter Distinct Coupon Number :")
        n = int(input())

        while n < 0:
            n = int(input("Please Provide Positive Number"))

        cn.generateCouponNumbers(n)

    except ValueError:
        print("oops Something Went Wrong......... Please Provide Only Integer Values........")
