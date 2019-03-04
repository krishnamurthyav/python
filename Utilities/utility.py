import random
import math
import time
from symbol import break_stmt

"""
****************************************************************************************
* Purpose: It Contains All The Static Methods To Perform Operation On User Input
*
* @author:  Krishna Murthy A V
* @version: 1.0
* @since:   25-02-2019
*
****************************************************************************************
"""
class FunctionalCode:

    '''*************************************************************************************************************'''
    '''--------------------------------- 1: Function To Replace String Template---------------------------------------'''

    @staticmethod
    def strReplace(name):   # It's Static Function That Accepts String as Parameter
        while len(name) <= 3 or name.isdigit():
            name = input("enter valid name\n")
        temp = "Hello <<UserName>>, How are you?"
        str = temp.replace("<<UserName>>", name)    # <<UserName>> its Replace with user input by using replace() function
        print(str)

    '''*************************************************************************************************************'''
    '''--------------------------------- 2: Function To print Percentage of Coin Flip----------------------------------'''


    @staticmethod
    def coin_Flip(n):    # Its takes integer as argument
        count = 0
        heads = 0
        tails = 0
        print(n)
        while count < n:    # While loop executes Until count should be less than N
            val = random.randint(0, 1)  # Generating Random numbers
            count += 1
            if val < 0.5:   # if the random number is less than 0.5 it will increments tails else increments heads
                tails += 1
            else:
                heads += 1

        print("heads count = ", heads)
        print("Tails count = ", tails)
        print("percentage of heads : ", heads / n * 100)  #  # To Calculate Percentage of Heads [ ,(comma) to print int ]
        print("Percentage of tails : " + str(tails / n * 100))  # +(plus) to concaat string


    '''*************************************************************************************************************'''
    '''--------------------------------- 3: Function To test Leap Year-----------------------------------------------'''

    @staticmethod
    def test_LeapYear(year):     # it accepts Integer as parameter
        if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:    # if Year is completely Divisible by 4 or 100 or 400
            print("Its a Leap Year")
            return True
        else:
            print("Not a Leap Year")
            return False


    '''*************************************************************************************************************'''
    '''--------------------------------- 5: Function To calculate Harmonice Value-----------------------------------'''

    @staticmethod
    def harmonic_Num(n):     # it accepts Integer As parameter
        sum = 0.0
        for i in range(1, n + 1):    # It loop until to reach n+1 value
            sum = sum + 1.0 / i      # logic is like this 1/1 + 1/2 + 1/3 + ... + 1/N
            print("Harmonic value of ", i, " is : ", sum)


    '''*************************************************************************************************************'''
    '''--------------------------------- 4: Function To generate Power's of Two-------------------------------------'''

    @staticmethod
    def power_Of_two(n):    # it accepts Integer As parameter
        for i in range(0, n + 1):   # It loop until to reach n value
            print("2^", i, "is :", pow(2, i))   # finding 2 power (1 - n-1) using math class pow() function


    '''*************************************************************************************************************'''
    '''--------------------------------- 6: Function To generate Prime Factor's-------------------------------------'''

    @staticmethod
    def prime_Factors(n):   # it accepts Integer As parameter
        p = 2
        print("Prime factors are : ")
        while n >= p * p:   # While loop executes Until N should be less than p*p
            if n % p == 0:  # if N is completely Divisible By P then only control Enter into if loop
                print(p)
                n = n // p
            else:
                p += 1  # if N is not Divisible By p then Increment P value with 1

        print(n)


    '''*************************************************************************************************************'''
    '''----------------------------------- 7: Function To Play Gambler ---------------------------------------------'''

    @staticmethod
    def gambler_Game(stake, goal, count):    # It Takes 3 Parameters as Integer
        win = 0
        loss = 0
        cnt = count
        while cnt > 0:  # While loop executes Until N should be > 0
            val = random.random()    # Generating Random numbers
            if val < 0.5:      # if generated random number is > 0.5 increment win by 1
                win += 1
            else:
                loss += 1       # else generated random number is > 0.5 increment win by

            cnt -= 1    # decrement N by 1
        print("Winning count : ", win)
        print("Loosing count : ", loss)

        wins = win / count * 100  # To Calculate Percentage of win
        lose = 100 - wins  # To Calculate Percentage of lose

        print("Winning percentage : ", wins)
        print("Loosing percentage : ", lose)


    '''*************************************************************************************************************'''
    '''--------------------------------- 8: Function To Generate Coupon Numbers----------------------------------'''

    @staticmethod
    def generateCouponNumbers(n):   # it takes one parameter as integer
        count = 0
        # print("start")
        list = []       # Empty Array list to store Distinct coupon
        while len(list) < n:     # while loop executes until len(arr) should be < N
            randvalue = random.randint(1, n)
            count += 1      # Increment count by 1
            if randvalue not in list:    # if generated number is not in array list control enters into loop
                list.append(randvalue)  # generated number added lo array at the end

        print("Generated random numbers")
        print(list)
        print("Number of Iterations ", count)


    '''*************************************************************************************************************'''
    '''--------------------------------- 9: Function To Print Two Dimensional Array --------------------------------'''

    @staticmethod
    def MatrixArray(matrix, row, col):  # it accepts three parameters as list,Integers
        for i in range(row):    # it executes until i reach to row value
            for j in range(col):    # it executes until j reach to col value
                print(matrix[i][j], " ", end="")    # to print matrix format
            print()


    '''*************************************************************************************************************'''
    '''--------------------------------- 10: Function To Find Triplets ---------------------------------------------'''

    @staticmethod
    def SumOfThree(arr):        # it Accepts Array list As parameter
        my_triplets = []
        for i in range(len(arr)):   # it executes until i reach to len(arr) value
            for j in range(i + 1, len(arr)):
                for k in range(j + 1, len(arr)):
                    if arr[i] + arr[j] + arr[k] == 0:   # if a[i]+a[j]+a[k]=0 these are triplet numbers
                        if arr[i] not in my_triplets or arr[j] not in my_triplets or arr[k] not in my_triplets:
                            my_triplets.append(arr[i])  # if triplets numbers not in array add it to array list
                            my_triplets.append(arr[j])
                            my_triplets.append(arr[k])
                            print(
                                "The Distinct Triplets : " + str(arr[i]) + " " + str(arr[j]) + " " + str(arr[k]) + " ")
        count = len(my_triplets) / 3    # to get number of distinct numbers
        print("Number Of Distinct Triplets :", int(count))


    '''*************************************************************************************************************'''
    '''--------------------------------- 11s: Function To Calculate Euclidean Distance -------------------------------'''

    @staticmethod
    def findEuclideanDistance(x, y):    # it Accepts Two   Number As parameter
        px = pow(x, 2)
        py = pow(y, 2)
        res = px + py
        result = math.sqrt(res) # logic is sqrt (x*x + y*y)
        print(result)


    '''*************************************************************************************************************'''
    '''--------------------------------- 13: Function To Simulate Stopwatch Program --------------------------------'''

    @staticmethod
    def startWatch(choice): # it Accepts Number As parameter
        if choice == 1:
            start_time = time.time()    # time() returns time as a floating point number expressed in seconds
        return start_time

    @staticmethod
    def stopWatch(choice, start):   # it takes 2 parameters As Integer And Float
        if choice == 2:
            end_time = time.time() - start  # to calculate Elapsed time
        print("Elapsed time :", end_time, "Secs")


    '''*************************************************************************************************************'''
    '''--------------------------------- 16: Function To Calculate Wind Chill Value --------------------------------'''

    @staticmethod
    def resultOfWindChill(temp, ws):  # It Takes Two parameters as Integers
        pws = math.pow(ws, 0.16)  # Find Power of speed

        res = 35.74 + 0.6215 * temp
        res2 = 0.4275 * temp - 35.75 * pws
        result = res + res2  # its Based On Formula
        print("Wind Chill :", result,"kilocalories/hour per square metre")


    '''*************************************************************************************************************'''
    '''--------------------------------- 15: Function To Solve Quadratic Equation ----------------------------------'''

    @staticmethod
    def rootsOfEquation(a, b, c):   # it takes 3 parameters as integer
        delta = pow(b, 2) - 4 * a * c   # calculating delta value
        deno = 2 * a
        try:
            r1 = (-b + math.sqrt(delta)) / deno     # formula Root 1 of x = (-b + sqrt(delta))/(2*a)
            r2 = (-b - math.sqrt(delta)) / deno     # formula Root 1 of x = (-b - sqrt(delta))/(2*a)
            print(r1, r2)

        except ValueError:
            print("Enter valid number")


    '''*************************************************************************************************************'''
    '''------------------------------------ Algo 1: Function To Find Anagram string --------------------------------'''

    @staticmethod
    def anagram_Str(s1, s2):    # it Accepts Two parameters As Strings
        s1 = s1.lower()
        s2 = s2.lower()

        if (sorted(s1) == sorted(s2)):  # condition to check if both the strings are same and equal
            print("Entered Strings are in anagram format")
        else:
            print("Strings are not in Anagram format")


    '''*************************************************************************************************************'''
    '''------------------------------------ Algo 3: Function To Find Anagram Number --------------------------------'''

    @staticmethod
    def anagramPrime(my_list):  # it takes list as parameter
        my_list1 = []

        for i in range(len(my_list)):    # i=0 to length of list
            for j in range(i + 1, len(my_list)):    # j=i+1 to length of list
                # print(my_list[j]+"")
                if sorted(my_list[i]) == sorted(my_list[j]):    # if a[i] & a[j] are equal then anagram Number
                    if my_list[i] not in my_list1:
                        my_list1.append(my_list[i]) # print(my_list[i])

        return my_list1

    '''*************************************************************************************************************'''
    '''--------------------------------------------Function to find Palindrome----- --------------------------------'''

    @staticmethod
    def palindrome(n):      # it accepts 1 parameter as Integer
        rev = 0
        temp = n
        while n > 0:        # loop executes until N > 0
            rem = n % 10    # hold remainder
            rev = rev * 10 + rem    # to get reverse of Number
            n = n // 10

        if rev == temp:     # if booth are == then Number is Palindrome
            return temp

    '''*************************************************************************************************************'''
    '''------------------------------------ Algo 2: Function To Calculate Prime Num --------------------------------'''
    @staticmethod
    def PrimeNumbers(n):    # it accepts 1 parameter as Integer
        my_list = []
        pm_list = []
        for i in range(0, n):   # it loops until i reach to N
            if i > 1:
                result = True
                for j in range(2, i):   # it loops until J reach to i
                    if i % j == 0:      # if i completely divisible by j then its not prime number
                        result = False
                        break

                if result:       # if result == to True then its prime number
                    pm_list.append(i)
                    my_list.append(str(i))
        # print(pm_list)
        return my_list


    '''*************************************************************************************************************'''
    '''------------------------------------ Algo 5: Function To Guess Number --------------------------------'''

    @staticmethod
    def guessNumber(list, low, high):
        n = 0
        n1 = 0
        res = True
        mid = int((low + high) / 2) # to get middle position

        if low == high:     # if low == high than this is your number
            print("Guessed Number is : ", list[mid])
        else:
            print("Guessed Number is : ", list[mid])
            print("YES = 0 / NO =1")
            n = int(input())        # reading input as number

        if n == 1:      # if num = 1 this is not a guessed number else this is guessed Number
            print("Is Your Number greather than ", list[mid], " enter 0 / small than ", list[mid], "enter 1 ")
            n1 = int(input())   # reading input as number
            res = True
        else:
            print("Your Guessed Number is ", list[mid])
            res = False

        if res:     # if res is True then guess number is > middle number else < middle number
            if n1 == 0:
                low = mid + 1
                f1.guessNumber(list, low, high)
            else:
                high = mid - 1
                f1.guessNumber(list, low, high)


    '''*************************************************************************************************************'''
    '''------------------------------------ Algo 8: Function To Perform Bubble Sort --------------------------------'''

    @staticmethod
    def bubbleSort(arr):        # it takes list as parameter
        start = f1.startWatch(1)
        for i in range(len(arr)):   # it loops i=0 to length of list
            for j in range(i + 1, len(arr)):    # it loops j=i+1 to length of list
                if arr[i] > arr[j]:     # if a[i] > a[j] then it swap the value
                    temp = arr[j]
                    arr[j] = arr[i]
                    arr[i] = temp
        f1.stopWatch(2, start)
        return arr



    '''*************************************************************************************************************'''
    '''------------------------------------ Algo 7: Function To Perform Insertion sort ------------------------------'''

    @staticmethod
    def Insertion_Sort(slist):      # it takes list as parameter
        print("Before Sorting",slist)
        slen = len(slist)

        for i in range(0, slen):  # it loops from 0 to len of list
            for j in range(i - 1, -1, -1):
                if slist[j] > slist[j + 1]:  # compares to previous index value
                    slist[j], slist[j + 1] = slist[j + 1], slist[j]  # swap values
        print("After Sorting ",slist)
        return slist

    '''**************************************************************************************************************'''
    '''------------------------------------ Algo 14: Function To Calculate Square Root ------------------------------'''

    @staticmethod
    def findSquareRoot(number):     #it takes number as Argument
        epsilon = 1e-15     # initialise Newton's method
        t = number

        while math.fabs(t - number / t) > epsilon * t:     # it Executes until abs(t-number/t) >epsilon
            t = (number / t + t) / 2.0       # calculating average of c/t and t
        print("Square Root of '", number, "'is :", t)

    # code to tempe Conversion
    '''*************************************************************************************************************'''
    '''------------------------------- Algo 12: Function To Calculate Temp Conversion ------------------------------'''

    @staticmethod
    def temperatureConversion(choice):  # it takes one argument as Integer
        if choice == 1:     # if choice == 1 Fahrenheit to Celsius else Celsius to Fahrenheit
            print("Enter Value for Fahrenheit:")
            f = int(input())    # reading input
            c = (f - 32) * 5 // 9   # formula to convert Celsius
            print("Temperature Conversion Fahrenheit to Celsius:", c,"°C")
        elif choice == 2:
            print("Enter The Value For Celsius :")
            c = int(input())    # reading input
            f = (c * 9 // 5) + 32   # formula to convert Fahrenheit
            print("Temperature Conversion Celsius to Fahrenheit:", f,"°F")
        elif choice == 3:
            exit()

        choice = int(input("Select choice \n"))
        f1.temperatureConversion(choice)


    '''*************************************************************************************************************'''
    '''--------------------------------- Algo 11: Function To Calculate Day Of WEEk --------------------------------'''
    @staticmethod
    def dayOfTheWeek(month, day, year):
        months = {1: 'jan', 2: 'Feb', 3: 'March', 4: 'April', 5: 'May', 6: 'Jun', 7: 'July', 8: 'Aug', 9: 'Sept',
                  10: 'Oct', 11: 'Nov', 12: 'Dec'}
        weeks = {0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday'}
        y = year - (14 - month) // 12
        x = y + y // 4 - y // 100 + y // 400
        m = month + 12 * ((14 - month) // 12) - 2
        d = (day + x + 31 * m // 12) % 7    #calculates weekday
        print("Day Of The Week : ", weeks[d], "-", months[month], "-", year)
        return d


    '''*************************************************************************************************************'''
    '''----------------------------- Algo 15: Function To Convert Decimal to Binary ---------------------------------'''

    def covertDecimalToBinary(num):  # it takes number as parameter
        my_list = []
        list = []
        while num > 0:      # loop until reach to N > 0
            rem = num % 2
            my_list.append(rem)
            num = num // 2
        my_list.reverse()
        for i in range(len(my_list), 8):  # Adding 0 to empty position
            list.append(0)
        str1 = ""
        for j in my_list:
            str1 = str1 + str(j)
        str2 =""
        for k in list:
            str2 = str2 + str(k)
        str3 = str2 + str1   # to marge all numbers into single number

        return str3

    @staticmethod
    def covertDecimal(num):  # it takes number as parameter
        my_list = []
        while num > 0:  # loop until reach to N > 0
            rem = num % 2
            my_list.append(rem)
            num = num // 2
        my_list.reverse()
        for i in range(len(my_list), 8):  # Adding 0 to empty position
            my_list.append(0)
        str1 = ""
        for j in my_list:  # to marge all numbers into single number
            str1 = str1 + str(j)

        return str1

    '''*************************************************************************************************************'''
    '''------------------------------------  Function To Convert Binary to Decimal ---------------------------------'''

    @staticmethod
    def binaryToDecimal(number):    # it takes number as parameter
        dec_value = 0
        base = 1
        temp = number
        while temp:     # loop executes until a number is present
            last_digit = temp % 10  # Extracting last digit of a number
            temp = int(temp / 10)

            dec_value += last_digit * base  #calculate value with reapect to its position
            base = base * 2
        return dec_value


    '''*************************************************************************************************************'''
    '''----------------------------------- Algo 13: Function To Calculate Monthly Payment --------------------------'''

    @staticmethod
    def MonthPay(P, Y, R):
        total_months = 12 * Y  # formula to calculate payment
        month_rate = R / (12 * 100)
        payment = P * month_rate / 1 - ((1 + month_rate) ** (-total_months))
        print("Payment : ", payment)


    '''*************************************************************************************************************'''
    '''------------------------------------ Algo 10: Function To generate change -----------------------------------'''

    @staticmethod
    def VendingMachine(Money, notes):   # it takes number and list as arguments
         try:
            total = 0
            if Money == 0:
                return -1
            else:
                for i in notes:     # it loops till i not in a list
                   if Money >= i:   # it loops till money greaterthan i
                        notes_count = Money // i
                        Money = Money % i
                        total += notes_count    # calculate number of notes
                        print(i, ":", notes_count, " Notes")
                print("Total Number of notes:", total)
         except RecursionError:
            print("Recursion error occured")

    '''*************************************************************************************************************'''
    '''------------------------------------ Algo 16: Function To CHeck Power of 2 ----------------------------------'''

    @staticmethod
    def isPowerOfTwo(n):    # it takes decimal Number as parameter
        if (n == 0):
            return False
        while (n != 1):     # it loops until Number becomes one
            if (n % 2 != 0):    # Checks if number is divisible by two
                return False
            n = n // 2

        return True
    '''*************************************************************************************************************'''
    '''------------------------------------ Algo 6: Function To Search Word in a List ----------------------------------'''

    @staticmethod
    def searchElement(arr1, ele):  # It accepts 2 parameters as list,Integer Or String
        arr = sorted(arr1)  # sort the Array
        low = 0
        h = len(arr) - 1
        flag = True
        while low <= h:  # loop executes until low <= high
            m = (low + h) // 2  # get middle element position

            if arr[m] == ele:  # if element == a[m] then element found
                print("Element '", arr[m], "' Found At position of", m)
                flag = False
            if arr[m] < ele:  # if a[m] < element the set low = m + 1 else high = m - 1
                low = m + 1
            else:
                h = m - 1

        if flag:  # if flag == True then Element Not Found
            print("Element Is Not Found")

#
    '''*************************************************************************************************************'''
    '''------------------------------------ Algo 9: Function To Merge Sort ---------------------------------------'''


# code Merge sort one
    @staticmethod
    def MergeSort(data):
        length = len(data)
        if length < 2:  # if length less than 2 ,+ it return
            return
        Mid = length // 2  # Calculate the mid
        left = []
        right = []

        for i in range(Mid):  # Take range from 0 to mid
            left.append(data[i])
        for j in range(Mid, length):  # Take range from mid to length
            right.append(data[j])
        # print(left, right)

        f1.MergeSort(left)  # Sort left side data
        f1.MergeSort(right)  # Sort right side data
        # print(left, right)  # Print sorted left and right data
        f1.Merging(left, right, data)
        # print(data)

    @staticmethod
    def Merging(left, right, data):
        i, j, k = 0, 0, 0  # Initialize the value of i,j,k
        ll = len(left)  # left side list
        lr = len(right)  # right side list

        while i < ll and j < lr:
            if left[i] < right[j]:
                data[k] = left[i]
                i += 1
            else:
                data[k] = right[j]
                j += 1
            k += 1

        while i < ll:  # Copy the remaining element of left[] if there are any
            data[k] = left[i]
            i += 1
            k += 1

        while j < lr:  # Copy the remaining element of right[] if there are any
            data[k] = right[j]
            j += 1
            k += 1



    '''**************************************************************************************************************'''
    '''----------------------------- 12: Function to Perform Permutation of a String --------------------------------'''

    @staticmethod
    def permutation(lst):
        if len(lst) == 0:  # if there is empty list then permutation is not done
            return []
        if len(lst) == 1:  # if there is only one element present in list then only one permutation is done
            return [lst]
        l = []  # empty list that will store current permutation
        for i in range(len(lst)):  # Iterate the input and calculate the permutation
            m = lst[i]
            #print("m = " ,m)
            rem = lst[:i] + lst[i + 1:]  # Extract word[i](remWord is remaining words)
            #print("rem =" ,rem)
            for p in f1.permutation(rem):  # Generating all permutation
                l.append([m] + p)

        return l

    '''**************************************************************************************************************'''
    '''----------------------------- A6 : Binary Word Search --------------------------------------------------------'''

    @staticmethod
    def Search_Word():
        try:
            file = open("./demo.txt")  # Open the file
            data = file.read().split(",")  # Read and split the words in file
            print(data)
            word = input("\nEnter the string")  # Take input
            data[-1] = data[-1].strip()  # Remove the spaces
            f1.BinarySearch_string(word, data)  # give file data and key to Binary search algorithm

        except FileNotFoundError:
            print("File not found")

    @staticmethod
    def BinarySearch_string(key, slist):
        slist.sort()  # works on sorted list
        print("Sorted list: ", slist)
        start = 0
        sll = len(slist)
        # while start < sll:
        for i in range(start, sll):  # from 0 to length of given list
            mid = start + (sll - start) // 2  # calculate mid

            if slist[mid] == key:  # checks key is mid value or not
                print("found at ", mid, " index ")
                break

            elif key > slist[mid]:  # id key is greater than mid value
                start = mid

            else:
                sll = mid  # else set end is mid value
        else:
            print("String not in the list")



f1 = FunctionalCode
