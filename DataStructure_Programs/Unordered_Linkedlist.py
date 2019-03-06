from DataStructure_Utility.Datastructure_Operations import LinkedList

l1 = LinkedList()

class Linked_List:
    try:
        newfile = open("test.txt", "r+")  # File IO open() function to Opens the file with read mode
        words = newfile.read()  # reading file data and it converts to single String
        my_list = words.split()  # It splits the Given String Sentence into Words(by Space)
        newfile.close()  # close the file
        print("****************************After Reading From The File:*************************************")
        for i in words:
            print(i, end="", )
        print()

        print("\n*******************************UnOrdered Linked List Elements**********************************")
        # print(my_list)
        for i in my_list:
            new_list = l1.add(i)  # Invoking add Method to add element to linked list
        l1.display()
        print()

        print("\n***************************Enter The Word To Search******************************************")
        word = str(input())  # reading word to search in LinkedList
        while not str.isalpha(word):
            print("Please Enter Only String")
            word = str(input())

        res = l1.search(word)  # Invoking search() Method to search element in linked list

        if res is True:  # if element present in linked list  else not present
            result = l1.remove(word)  # Invoking remove() Method to remove element from linked list
        else:
            l1.add(word)  # Invoking add Method to add element to linked list
            print()
            print(word, "Its Added To Linked List \n")
        # l1.display()

        print("\n*************************Updated Linked list Is ***************************")
        words2 = l1.display()  # Invoking display() Method to print element of linked list
        print()

        newfile = open("test.txt", "r+")  # open file in read and write mode
        newfile.truncate(0)  # file IO truncate() method to remove all tha data from file
        newfile.close()  # close file

        newfile = open("test.txt", "r+")  # open file in read and write mode
        for words1 in words2:
            word3 = str(words1) + " "
            newfile.write(word3)  # file IO write() to write data into file
        newfile.close()  # close file
        my_list.clear()
    except FileNotFoundError:
        print("File Not Found Check File is there Or Not")
