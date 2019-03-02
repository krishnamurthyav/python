"""
******************************************************************************
* Purpose:  Take 2 string input from user and print it is anagram or not.
* @author:  Krishna Murthy A V
* @version: 1.1
* @since:   28-2-2019
*
******************************************************************************
"""

from Utilities.utility import FunctionalCode

a1 = FunctionalCode

class anagram:
    try:
        print("Program top check if two strings are in anagram format")
        print("Enter 1st string")
        str1 = input()
        print("enter second string")
        str2 = input()

        a1.anagram_Str(str1,str2)

    except RuntimeError:
        print("Runtime Error")