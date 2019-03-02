
"""
******************************************************************************
* Purpose:  Reads in integers prints them in sorted order using Bubble Sort
* @author:  Krishna Murthy A V
* @version: 1.1
* @since:   28-2-2019
*
******************************************************************************
"""

from  Utilities.utility import FunctionalCode

c1 = FunctionalCode

class BubbleSort:
    try:
        print("Enter The Integer Numbers Only And Also Enter The How many Numbers u need(Size):")
        size = int(input())     # Reading Size of the Array

        while size <= 0:    # Validating Size might not be  Negative Value
            size = int(input("Please Provide Valid Value\n"))

        num = []  # Empty List To Store The Array Elements
        print("Enter The Integer Numbers:")
        for i in range(size):   # it loops until to reach to array size
            num.append(int(input()))    # reading Array Elements And Storing Into list
        print("Before Sorting:", num)
        sort = c1.bubbleSort(num)   # Invoking function it takes One arguments As list
        print("After Sorting:", sort)

    except ValueError:
        print("....................oops Something Went Wrong......... Please Provide Only Integer Values........")