"""
******************************************************************************
* Purpose:  Simulates a gambler who start with $stake and place fair $1 bets until he/she goes broke
   (i.e. has no money) or reach $goal. Keeps track of the number of times he/she wins and the number
   of bets he/she makes. Run the experiment N times, averages the results, and prints them out.
* @author:  Krishna Murthy A v
* @version: 1.0
* @since:   27-2-2019
*
******************************************************************************
"""


from Utilities.utility import FunctionalCode

g1 = FunctionalCode


class Gambler:
    try:
        print("Enter the amount")
        stake = int(input())
        print("Enter the goal amount")
        goal = int(input())
        print("Enter Number of times to play")
        count = int(input())
        while stake < 0:
            stake = int(input("enter positive amount"))

        while goal < 0:
            goal = int(input("enter target amount "))

        while count < 0:
            count = int(input("Enter positive count"))

        g1.gambler_Game(stake, goal, count)

    except RuntimeError:
        print("Error occured")
