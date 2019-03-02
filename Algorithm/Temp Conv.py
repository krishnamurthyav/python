"""
******************************************************************************
* Purpose:  given the temperature in fahrenheit as input outputs the temperature
            in Celsius or viceversa using the formula
           Celsius to Fahrenheit:   (°C × 9/5) + 32 = °F
           Fahrenheit to Celsius:   (°F − 32) x 5/9 = °C
* @author:  Krishna Murthy A V
* @version: 1.2
* @since:   1-3-2019
*
******************************************************************************
"""
from Utilities.utility import FunctionalCode

c1 =FunctionalCode

class TemperatureConversion:
    try:
        print("Enter Your Input Choice :\n1 - Fahrenheit\n2 - Celsius \n3 -Exit")
        choice = int(input())

        while choice <= 0:
            choice = int(input("Please Provide Valid Value\n"))

        c1.temperatureConversion(choice)
    except ValueError:
        print("...........oops Something Went Wrong.........")