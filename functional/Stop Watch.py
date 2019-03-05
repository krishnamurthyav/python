"""
******************************************************************************
* Purpose: Write a Stopwatch Program for measuring the time that elapses
             between the start and end clicks.
*@author:  Krishna Murthy A V
* @version: 1.1
* @since:   27-2-2019
*
******************************************************************************
"""

from Utilities.utility import FunctionalCode

obj = FunctionalCode

class StopWatchTimer:
    try:
        print("Enter 1 To Start :")
        choice1 = int(input())
        while choice1 != 1:
            choice1 = int(input("Please Provide Valid Input(Enter 1 Only)\n"))
        start = obj.startWatch(choice1)

        print("Enter 2 To StopWatch :")
        choice2 = int(input())
        while choice2 != 2:
            choice2 = int(input("Please Provide Valid Input(Enter 2 Only)\n"))
        obj.stopWatch(choice2, start)

    except ValueError:
        print('oops Something Went Wrong......... Please Provide Only Integer Values.......')