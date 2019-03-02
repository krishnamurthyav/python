"""
******************************************************************************
* Purpose:  Take N integer number from user and find the prime factorization of
             the taken number.
*
* @author:  Krishna Murthy A V
* @version: 1.0
* @since:   27-2-2019
*
******************************************************************************
"""

from Utilities.utility import FunctionalCode

p1 = FunctionalCode

class Prime_Factors:
    try:
        print("Enter a Number to find its Prime Factors")
        num = int(input())
        if num < 0:
            num = int(input("Enter positive number"))

        p1.prime_Factors(num)

    except RuntimeError:
        print("Something went wrong")