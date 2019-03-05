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

prime = FunctionalCode

class Prime_Factors:
    flag = 0
    while flag == 0:
        try:
            number = int(input("Enter a Number to find its Prime Factors"))
            type(number) == int
            flag = 1
        except:
            print("Enter integer number")
            continue

        try:
            prime.prime_Factors(number)

        except RuntimeError:
            print("Something went wrong")