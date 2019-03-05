"""
******************************************************************************
* Purpose: Takes two double arguments t and v from user and prints the wind chill.
* @author:  Krishna Murthy A V
* @version: 1.0
* @since:   28-2-2019
*
******************************************************************************
"""

from  Utilities.utility import FunctionalCode

windchill = FunctionalCode

class WindChill:
    flag = 0
    while flag == 0:
        try:
            temperature = float(input("Enter The Air Temperature :"))
            type(temperature) == float
            while temperature > 50:
                temperature = float(input("Enter The Air Temperature Value Less Than 50 "))
            flag = 1
        except:
            print("Enter valid Temperature ")
            continue

    while flag ==1:
        try:
            wind = float(input("Enter The Wind Speed value: "))
            while wind > 130 or wind < 3:
                wind = float(input("Enter The Wind Speed value grater than 3 and less than 130"))
            flag = 2
        except:
            print("Enter valid wind speed")
            continue

    try:
        windchill.resultOfWindChill(temperature, wind)

    except ValueError:
        print("oops Something Went Wrong.........")
