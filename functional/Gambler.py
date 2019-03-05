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

gambler = FunctionalCode


class Gambler:
    flag = 0
    while flag == 0:
        try:
            stake = float(input("Enter stake amount"))
            type(stake) == float
            flag = 1
        except:
            print("Re-Enter stake value")
            continue

    while flag == 1:
        try:
            goal = float(input("Enter the goal amount"))
            type(goal) == float
            flag = 2
        except:
            print("Re-Enter goal value")
            continue

    while flag == 2:
        try:
            count = int(input("Enter Number of times to play"))
            type(count) == int
            flag = 3
        except:
            print("Re_enter Integer value")
            continue

        try:
            gambler.gambler_Game(stake, goal, count)

        except RuntimeError:
            print("Error occured")
