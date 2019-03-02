"""
******************************************************************************
* Purpose:  Take positive integer number from user and print percentage of Heads
             and Tails.
* @author:  Krishna Murthy A V
* @version: 1.0
* @since:   26-2-2019
*
******************************************************************************
"""

from Utilities.utility import FunctionalCode

c1 = FunctionalCode


def flip():
    try:
        print("Enter number of time to flip a coin")
        n = int(input())
        while n < 0:
            n = input("Enter valid number")

        c1.coin_Flip(n)

    except ValueError:
        print("Error occured")


if __name__ == "__main__":
    flip()