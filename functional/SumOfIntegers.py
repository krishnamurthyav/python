"""
******************************************************************************
* Purpose:  Take N integers from user and counts the number of
              triples that sum to exactly 0.
*
* @author:  Krishna Murthy A V
* @version: 1.0
* @since:   27-2-2019
*
******************************************************************************
"""

from Utilities.utility import FunctionalCode

si =FunctionalCode

class SumOfInt:
    try:
        print("Enter The Array Size :")
        n = int(input())

        while n < 0:
            n = int(input("Please Provide +ve Number only"))

        arr = []
        print("Enter The Array Elements\n")
        for x in range(n):
            arr.append(int(input()))

        si.SumOfThree(arr)
    except ValueError:
        print("oops Something Went Wrong......... Please Provide Only Integer Values........")