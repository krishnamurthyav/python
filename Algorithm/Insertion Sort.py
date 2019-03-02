"""
******************************************************************************
* Purpose:  Reads in strings from standard input and prints them in sorted order.
            Uses insertion sort.
* @author:  Krishna Murthy A V
* @version: 1.1
* @since:   28-2-2019
*
******************************************************************************
"""

from Utilities.utility import FunctionalCode

c1 =FunctionalCode

def insertion_sort():
    data = list(input("Enter the words separated by space").split(" "))  # Take input word which is separated by space
    c1.Insertion_Sort(data)  # sorting the data


if __name__ == "__main__":
    insertion_sort()