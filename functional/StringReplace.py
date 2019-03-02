"""
******************************************************************************
* Purpose: User Input and Replace String Template “Hello <<UserName>>, How are you?”
* @author:  Krishna Murthy A v
* @version: 1.0
* @since:   27-2-2019
*
******************************************************************************
"""

from Utilities.utility import FunctionalCode

s1 = FunctionalCode()

def run():
    try:
        print("Enter the user name")
        name = input()
        s1.strReplace(name)
    except RuntimeError:
        print("connection Lost")


if __name__ == "__main__":
    run()
