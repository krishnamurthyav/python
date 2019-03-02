from Utilities.utility import FunctionalCode

b1= FunctionalCode

class Binary:
    try:
        print("Enter The Number :")
        num = int(input())

        while num <= 0:
            num = int(input("Please Provide Valid Value\n"))

        res = b1.covertDecimal(num)
        var = int(res)
        len = len(res)
        len1 = len // 2
        str1 = res[0:len1]
        str2 = res[len1:len]
        str3 = str2 + str1
        print("Decimal To Binary and \n ")
        print("Before Swapping")
        for c in reversed(res):
             print(c, end='')
        print("\nAfter Swapping  :", var)
        res1 = b1.binaryToDecimal(var)
        print("Binary To Decimal", res1)
        flag = b1.isPowerOfTwo(res1)
        if flag:
            print(res1, "is Power Of 2 Yes")
        else:
            print(res1, "is Not a Power Of 2 ")
    except RuntimeError:
        print("--Error Occured--.")