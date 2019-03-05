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

triplets =FunctionalCode

class SumOfInt:
    flag = 0
    while flag == 0:
        try:
            size = int(input("Enter The Array Size :"))
            type(size) == int
            flag = 1
        except:
            print("Re-Enter array size")
            continue

    arr = []
    while flag == 1:
        try:
            for number in range(size):
                elements = int(input("Enter The Array Elements\n"))
                type(elements) == int
                arr.append(elements)
                flag = 2
        except:
            print("Enter integer values only")
            continue

    try:
        triplets.SumOfThree(arr)
    except Exception:
        print("oops Something Went Wrong......... Please Provide Only Integer Values........")