"""
******************************************************************************
* Purpose:  Take N number input from user and find the harmonic series
            as well as value of the harmonic series.
* @author:  Krishna Murthy A V
* @version: 1.0
* @since:   26-2-2019
*
******************************************************************************
"""

from Utilities.utility import FunctionalCode

h1 = FunctionalCode()


class HarmonicNum:
    try:
        print("Enter the value of N")
        number = int(input())
        while number == 0:
            number = int(input("Enter positive value"))

        h1.harmonic_Num(number)

    except RuntimeError:
        print("Error occured")
