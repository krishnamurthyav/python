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

flipcoin = FunctionalCode


def flip():
    flag = 0
    while flag == 0:
        try:
            number = int(input("Enter number of time to flip a coin"))
            type(number) == int
            flag = 1
        except:
            print("Enter valid integer value\n")
            continue

    try:
        flipcoin.coin_Flip(number)

    except RuntimeError:
        print("Error occured")


if __name__ == "__main__":
    flip()
