"""
****************************************************************************************
* Purpose: It Contains All The Static Methods To Perform Operation On User Input
*
* @author:  Krishna Murthy A V
* @version: 1.0
* @since:   5-03-2019
*
****************************************************************************************
"""

from Utilities.utility import FunctionalCode

from DataStructure_Programs.Node import Node


class LinkedList:

    def __init__(self):

        self.first = None
        self.last = None
        self.size = 0
        self.top = None
        self.front = None
        self.rear = None

    '''-------------------- Function to add element to a list------------------------------'''

    def add(self, data):
        n = Node(data)

        if self.size == 0:
            self.first = n
            self.last = n
        else:
            self.last.next=n
            self.last=n
        self.size += 1


    '''---------------------Function to search  a Word -------------------------------------'''

    def search(self, item):
        temp = self.first
        result = None

        while temp is not None:
            if temp.data == item:
                result = True
                break
            else:
                result = False
            temp = temp.next

        if result is True:
            print("Element ", item, " found")
            return True
        else:
            print("Element not found")
            return False

    '''--------------------------- Function To Find List Size -----------------------------------'''

    def sizeOf(self):
        print("Size of List is ", self.size)

    '''--------------------------- Function To Check Empty List ------------------------------------'''

    def isEmpty(self):
        if self.size == 0:
            print("List is Empty ")
        else:
            print("List contains ", self.size, " elements")

    '''---------------------------- Function to Display Elements -----------------------------------'''

    def display(self):
        my_list = []
        temp = self.first

        while temp is not None:  # it loops util temp == Null
            print(temp.data, "->", end=" ")
            my_list.append(temp.data)
            temp = temp.next
        return my_list

    '''---------------------------- Function to remove an Element ---------------------------------'''

    def remove(self, item):  # it takes item as parameter
        temp = self.first  # temp is pointing to first
        prev = None  # prev is pointing to Null
        if temp.data == item:  # if element is found at 1st position only then return true else loop over until null
            self.first = temp.next  # first = temp.next
            temp.next = self.first  # temp.next = first
            self.size -= 1
            return True
        else:
            while temp:  # it loops util temp == Null
                if temp.data == item:  # check first node data == item if true set True else temp points to next node
                    prev.next = temp.next
                    temp.next = None
                    return True
                    break
                else:
                    prev = temp
                    temp = temp.next
            self.size -= 1  # Decrement Size value


    ''' ---------------------------- Function to insert() Implementation --------------------------------'''

    def insert(self, data, pos):  # it takes two parameter as data and position
        prev = None  # prev is pointing to Null
        temp = self.first  # temp is pointing to first
        new_node = Node(data)  # creating Node class object and passing data

        if pos > 0 or pos < self.size:  # if pos > 0 and < size then insert node in between two nodes
            for i in range(0, self.size):
                if i == pos:  # if pos==i then we got position
                    self.size += 1  # increment size value
                    new_node.next = temp  # set new node to temp
                    prev.next = new_node  # prev to new node
                    break
                else:  # else point temp and prev to next node
                    prev = temp  # prev = temp
                    temp = temp.next  # temp = temp.next


    '''---------------------------- Function to add Ordered linked list ----------------------------------'''

    def orderedAdd(self, data):  # it takes Data as parameter
        node = Node(data)  # creating Node class object and passing data
        temp = self.first  # temp is pointing to first
        if self.size == 0:  # if size == 0 Add node at 1 position
            self.first = node
            self.last = node
        else:  # if size !=0 then add it to next
            while temp is not None:  # it loops util temp == Null
                if temp.data > data:  # if temp.data > data use bubble sort technique to swap it
                    d1 = node.data
                    node.data = temp.data
                    temp.data = d1

                temp = temp.next
            self.last.next = node
            self.last = node

        self.size += 1  # increment size value

    '''---------------------------------------       contine      -------------------------------------'''

    def append(self):
        global output
        try:
            with open("testO.txt","w") as output:
                p = self.first
                while p is not None:
                    output.write(str(p.data)+" ")
                    p.next
        except Exception as e:
            print(e)
        finally:
            output.close()

    ''''--------------------------------Stack Implementation  ------------------------------------------------'''

    '''--------------------------- Implementation of push method --------------------------------------------'''
    my_list = []
    cap = -1
    head = -1

    def push(self, expression):
        if self.head == self.cap:
            self.head += 1
            self.my_list.append(expression)
            self.cap += 1

        return self.my_list

    '''--------------------------- Implementation of pop method --------------------------------------------'''

    element = 0
    def pop(self):
        if self.head != -1:
            self.element = self.my_list[self.head]
            self.my_list.remove(self.my_list[self.head])
            self.head -= 1
            self.cap -= 1

        return self.element

    '''--------------------------- Implementation of pop method --------------------------------------------'''

    def peek(self):
        if self.head != 1:
            print("Top most element present is :",self.my_list[len(self.my_list)-1])
        else:
            print("No Element is present")

    '''--------------------------- Implementation of size method --------------------------------------------'''

    def size(self):
        print("Size of Stzck is",self.cap)

    '''--------------------------- Checking isEmpty Condition -----------------------------------------------'''

    def stackIsEmpty(self):
        if self.cap == 0:
            print("Stack is Empty")
        else:
            print("Stack is Not empty")

    '''------------------------------------ Queue Implementation ---------------------------------------------'''

    f = -1
    r = -1
    capacity = 5
    min_bal = 1000
    my_list = []

    def quePush(self, amount):
        if self.f == -1:
            self.f += 1
            self.r += 1
            self.my_list.append(amount)

            self.capacity -= 1
            self.min_bal += amount
            return self.min_bal
        elif self.capacity != 0:
             self.r += 1
             print(self.r)
             self.my_list.append(amount)

             self.capacity -= 1
             self.min_bal += amount
             return self.min_bal
        else:
            print("Queue is Full", self.min_bal)


    '''---------------------------------------- Queue POP Operation -----------------------------------------'''

    def queuePop(self):
        if self.capacity != 0:
            self.r -= 1
            self.capacity +=1
            for i in range(len(self.my_list)):
                self.my_list.remove(self.my_list[i])
                break

            for i in self.my_list:
                print(i, end="->")
                print()
                return self.my_list


    '''--------------------------------- add() method implementation of Queue ----------------------------------'''

    def enQueue(self, data):
        node = Node.data
        if self.r is None:
            self.f = node
            self.r = node
        else:
            self.r.next = node
            self.r = self.r.next
