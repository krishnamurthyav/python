"""
******************************************************************************
* Purpose: Read in a list of words from File. Then prompt the user to enter
          a word to search the list. The program reports if the search word
          is found in the list.
* @author:  Krishna Murthy A V
* @version: 1.2
* @since:   28-2-2019
*
******************************************************************************
"""

from Utilities.utility import FunctionalCode

b1 = FunctionalCode

def BinSearchWord():

    b1.Search_Word()  # call the method from utility


if __name__ == "__main__":
    BinSearchWord()