"""
******************************************************************************
* Purpose:  Takes a date as input and prints the day of the week that date.
* @author:  Krishna Murthy A V
* @version: 1.2
* @since:   28-1-2019
*
******************************************************************************
"""

from Utilities.utility import FunctionalCode
obj =FunctionalCode

class DayOfWeek:
    try:
        print("Enter Value for Month:")
        m = int(input())

        while m <= 0:
            m = int(input("Please Provide Valid Value(Month)\n"))

        print("Enter Value for Day:")
        d = int(input())
        while d <= 0:
            d = int(input("Please Provide Valid Value(Day)\n"))

        print("Enter Value for Year:")
        y = int(input())
        while y <= 999:
            y = int(input("Please Provide Valid Value(Year)\n"))
        obj.dayOfTheWeek(m, d, y)

    except ValueError:
        print("-------Please Provide Valid input(Positive Number)")