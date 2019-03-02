from  Utilities.utility import FunctionalCode

f1 = FunctionalCode

class QuestionToFindYourNumber:
    try:
        my_list = []
        print("Enter the N value")
        num = int(input())

        while num < 0:
            print("Please Provide Positive Number(only)")
            num = int(input())

        for i in range(1, pow(2, num-1)):
            my_list.append(i)
        print("think of a number between 0 and ", len(my_list)-1)
        print(my_list)
        low = 0
        high = len(my_list)-1
        f1.guessNumber(my_list, low, high)
    except RuntimeError:
        print(".....................oops Something Went Wrong.........")