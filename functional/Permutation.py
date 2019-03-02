"""
******************************************************************************
* Purpose: Write static functions to return all permutation of a String
            using Recursion method.
*@author:  Krishna Murthy A V
* @version: 1.1
* @since:   27-2-2019
*
******************************************************************************
"""

from Utilities.utility import FunctionalCode

u = FunctionalCode

def permut():
    word = list(input("Enter the string \n")) # take string input
    for p in u.permutation(word):
        print(p) # print the permutation
    u.permutation(word)

if __name__ == "__main__":
    permut()
