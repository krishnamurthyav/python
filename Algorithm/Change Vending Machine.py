"""
******************************************************************************
* Purpose: There is 1, 2, 5, 10, 50, 100, 500 and 1000 Rs Notes which can be
           returned by Vending Machine. Write a Program to calculate the minimum
           number of Notes as well as the Notes to be returned by the Vending
           Machine as a Change.
* @author:  Krishna Murthy A V
* @version: 1.1
* @since:   28-2-2019
*
******************************************************************************
"""

from Utilities.utility import FunctionalCode

vm = FunctionalCode

class Vending_Machine:
    try:
        notes = [2000,500,200,100,50,20,10,5,2,1]
        print("Enter the amount to get change")
        amt = int(input())
        while amt < 0:
            amt = int(input("Enter the valid amount"))

        vm.VendingMachine(amt,notes)

    except RuntimeError:
        print("Erroir occured")