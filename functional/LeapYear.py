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

leapyear = FunctionalCode()


class LeapYear:
    flag = 0
    while flag == 0:
        try:
            year = int(input("Enter year "))
            type(year) == int
            while year < 999 or year > 10000:
                year = int(input("Enter year greaterthan 999 and lessthan 10000"))
            flag = 1
        except:
            print("Enter valid year \n")
            continue

        try:
            leapyear.test_LeapYear(year)

        except ValueError:
            print("Something gone wrong")
