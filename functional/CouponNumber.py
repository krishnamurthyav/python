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

coupon = FunctionalCode


class Coupon_Code:
    flag = 0
    while flag == 0:
        try:
            number = int(input("Enter Required Distinct Coupon Number : \n"))     # reading input as number
            type(number) == int
            flag = 1
        except:
            print("Error - Please Provide Positive Number\n")  # reading input as number
            continue

        try:
            coupon.generateCouponNumbers(number)     # calling function and passsing number as argument

        except Exception as e:
            print("Something Went Wrong.........",e)
