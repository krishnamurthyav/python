"""
******************************************************************************
* Purpose:  Take given number and find the power of 2 of the
             the given number.
*
* @author:  Krishna Murthy A V
* @version: 1.1
* @since:   27-2-2019
*
******************************************************************************
"""

from Utilities.utility import FunctionalCode

power = FunctionalCode

class PowerTwo:
    flag = 0
    while flag == 0:
        try:
            number = int(input("Enter power value"))
            type(number) == int
            while number < 0 or number >= 32:
                number = int(input("Enter value between 0 to 31"))
            flag = 1
        except:
            print("Enter only integer value")
            continue

        try:
            power.power_Of_two(number)

        except RuntimeError:
            print("Error occured")