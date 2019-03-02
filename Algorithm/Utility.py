"""
******************************************************************************
* Purpose:  Utility Class write
*    binarySearch method for integer
*    binarySearch method for String
*    insertionSort method for integer
*   insertionSort method for String
*   bubbleSort method for integer
*   bubbleSort method for String
* @author:  Krishna Murthy A V
* @version: 1.2
* @since:   1-3-2019
*
******************************************************************************
"""

from Utilities.utility import FunctionalCode

b1 = FunctionalCode

class SearchAndSort:
    try:
        print("Enter Array Size :")
        size = int(input())     # Reading Array Size

        while size <= 0:  # Validating Size might not be  Negative Value
            size = int(input("Please Provide Valid Value(Positive Number)\n"))

        print("**************************First Just Try With Integers Only******************************")
        print("Enter The Array Elements : ")
        arr = []  # Empty List To store Array Elements as Integer numbers
        for i in range(size):   # it loops until to reach to array size
            arr.append(int(input()))  # reading Array Elements and Storing it into list

        print("**********************Sorted list Of Elements: Using Insertion Sort*****************")
        sort = b1.Insertion_Sort(arr)        # Invoking function it takes One arguments As list
        print(sort)
        print("Enter The Element To Search :")
        ele = int(input())  # Reading Number To Search
        b1.searchElement(sort, ele)     # Invoking function it takes Two arguments As list,Integer
        print("***********************Sorted list Of Elements: Using Bubble Sort******************")
        barr = b1.bubbleSort(arr)   # Invoking function it takes One arguments As list
        print(barr)

        print("***************************Now Try With String Input*****************")
        print("Enter The Array Elements : ")
        arr = []    # Empty List To store Array Elements as Strings
        for i in range(size):   # it loops until to reach to array size
            arr.append(input())     # reading Array Elements and Storing it into list
        print("**********************Sorted list Of Elements: Using Insertion Sort*****************")
        sort = b1.Insertion_Sort(arr)    # Invoking function it takes One arguments As list
        print(sort)
        print("Enter The Element To Search :")
        ele = input()   # Reading Word To Search
        b1.searchElement(sort, ele)     # Invoking function it takes Two arguments As list,Integer
        print("***********************Sorted list Of Elements: Using Bubble Sort******************")
        barr = b1.bubbleSort(arr)   # Invoking function it takes One arguments As list
        print(barr)
    except ValueError:
        print("...........oops Something Went Wrong.........")