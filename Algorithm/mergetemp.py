""""
******************************************************************************
* Purpose: Write a program with Static Functions to do Merge Sort of list
            of Strings.
* @author:  Krishna Murthy A V
* @version: 1.3
* @since:   28-2-2019
*
******************************************************************************
"""
from Utilities.utility import FunctionalCode

u = FunctionalCode

class Merge_Sort:
    data = list(input("Enter the element separated by space").split(" "))  # Take input word which is separated by space
    u.MergeSort(data)  # Sort the data
    print(data)