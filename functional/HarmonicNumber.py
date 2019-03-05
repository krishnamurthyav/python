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

harmonic = FunctionalCode()


class HarmonicNum:
    flag = 0
    while flag == 0:
        try:
            number = int(input("Enter the value of N"))
            type(number) == int
            flag = 1
        except:
            print("Invalid number \n")
            continue

        try:
            harmonic.harmonic_Num(number)

        except RuntimeError:
            print("Error occured")
