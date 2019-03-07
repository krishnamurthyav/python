from DataStructure_Utility.Datastructure_Operations import LinkedList

l1 = LinkedList()


class BinaryTree:
    while True:
        try:
            print("Enter the Number:")
            num = int(input())  # read input

            fact = l1.BinaryTree(num)   # # Invoking binaryTree() method to get factorial of number
            fact1 = l1.BinaryTree(num*2)
            fact3 = l1.BinaryTree(num+1)
            res = fact3*fact    # holding (N+1)! * N!
            result = fact1 // res   # final ans (N*2)!//(N+1)! * N!
            print(result)   # print result
            break
        except ValueError:
            print("Please Provide Only Numbers")
            continue