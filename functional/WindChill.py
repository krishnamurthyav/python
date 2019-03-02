"""
******************************************************************************
* Purpose: Takes two double arguments t and v from user and prints the wind chill.
* @author:  Krishna Murthy A V
* @version: 1.0
* @since:   28-2-2019
*
******************************************************************************
"""

from  Utilities.utility import FunctionalCode

wc = FunctionalCode

class WindChill:
    try:
        print("Enter The Air Temperature :")
        t = int(input())
        while t > 50:
            t = int(input("Enter The Air Temperature Value Less Than 50 "))

        print("Enter The Wind Speed value: ")
        v = int(input())
        while v > 130 or v < 3:
            v = int(input("Enter The Wind Speed value grater than 3 and less than 130"))

        wc.resultOfWindChill(t, v)

    except ValueError:
        print("oops Something Went Wrong.........")
