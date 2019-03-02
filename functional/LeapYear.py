"""
******************************************************************************
* Purpose:  Take four digit number of year from user and find it is leap year or not.
* @author:  Krishna Murthy A V
* @version: 1.0
* @since:   26-2-2019
*
******************************************************************************
"""

from Utilities.utility import FunctionalCode

l1 = FunctionalCode()


class LeapYear:
    try:
        print("Enter year ")
        year = int(input())
        l1.test_LeapYear(year)

    except ValueError:
        print("Something gone wrong")
