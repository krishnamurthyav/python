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

permutation = FunctionalCode

def permut():
    flag = 0
    while flag == 0:
        try:
            word = list(input("Enter the string \n")) # take string input
            type(word) == str
            flag = 1
        except:
            print("Enter string only")


        for string1 in permutation.permutation(word):
            print(string1) # print the permutation

        permutation.permutation(word)

if __name__ == "__main__":
    permut()
