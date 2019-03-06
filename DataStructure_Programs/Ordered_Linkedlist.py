from DataStructure_Utility.Datastructure_Operations import LinkedList

l1 = LinkedList()


class OrderedLinkedList:

    try:
        n1 = " "
        new_file = open("testO.txt", "r+")
        words = new_file.read()
        my_word = words.split()
        my_list = []
        new_file.close()

        print("**************************** After Reading From The File: *********************************")
        for i in my_word:
            print(i, end=" ")
        print()

        print("***************************** Ordered Linked List ***************************************")
        for i in my_word:
            my_list.append(int(i))
        for i in my_list:
            str = l1.orderedAdd(i)

        l1.display()
        print()

        print("***************************** Enter the number to search **********************************")
        number = input()
        while not number.isdigit():
            number = input()
        number1 = int(number)
        result = l1.search(number1)

        if result is True:
            result = l1.remove(number1)
        else:
            l1.orderedAdd(number1)

            print(number1, "is added to the list")

        print("\n****************************** Updated Linnked List ****************************************")
        number2 = l1.display()
        print()

        # new_file = open("testO.txt", "r+")
        # new_file.truncate(0)
        # new_file.close()
        # print("\n hi")
        # new_file = open("testO.txt","r+")
        # for n in number2:
        #     n1 = str(n) + " "
        #     new_file.write(n1)
        # new_file.close()
        # my_list.clear()
        l1.append()
    except Exception as e:
        print(e)
