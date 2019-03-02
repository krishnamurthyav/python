"""
******************************************************************************
* Purpose:  Take a range of 0 - 1000 Numbers and find the Prime numbers
            in that range.
* @author:  Krishna Murthy A V
* @version: 1.2
* @since:   28-2-2019
*
******************************************************************************
"""
from Utilities.utility import FunctionalCode

pn = FunctionalCode


class PrimeNumber:
    try:
        print("Enter The Range :")
        n = int(input())  #

        while n < 0:
            n = int(input("Please Enter Positive Number Only"))

        my_list = pn.PrimeNumbers(n)
        print("Prime numbers are : ",my_list)
        my_list1 = pn.anagramPrime(my_list)

        print("\n...................List Of All Prime's Palindrome Numbers................")
        for i in range(len(my_list)):
            temp = int(my_list[i])
            res = pn.palindrome(temp)
            if res is not None:
                print(temp, res)

    except ValueError:
        print("Please Provide Only Integer Values")