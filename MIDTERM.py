
##1 Bubble Sort

from random import *
n=[]
for i in range(0,50):
    x=randint(1, 50)
    if x not in n:
        n.append(x)

def Bubble(n):
    for i in range(len(n)-1, 0, -1):
        for i in range(i):
            if n[i] >n[i + 1]:
               n[i], n[i + 1] = n[i + 1], n[i]
    return n
print("Unsorted array having random number 1 to 50",*n)
print("Sorted array using Bubble Sort",*Bubble(n))

##2. Linked List

class Container:
        def __init__(self, data):
                self.data = data
                self.next = None

class Pod:
        def __init__(self):
                self.head = None

        #insert a new Container at the beginning
        def push(self, new_data):
                new_Container = Container(new_data)
                new_Container.next = self.head
                self.head = new_Container

        
        # delete the first occurrence of key in linked list
        def removeContainer(self, key):
                temp = self.head
                if (temp is not None):
                        if (temp.data == key):
                                self.head = temp.next
                                temp = None
                                return

                while(temp is not None):
                        if temp.data == key:
                                break
                        prev = temp
                        temp = temp.next
                if(temp == None):
                        return
                prev.next = temp.next

                temp = None

        def printList(self):
                temp = self.head
                while(temp):
                        print (" %d" %(temp.data)),
                        temp = temp.next



List = Pod()
List.push(7)
List.push(1)
List.push(3)
List.push(2)

print ("Pod created: ")
print("\nPod after adding of Conatiner")
List.printList()
List.removeContainer(1)
print ("\nPod after remove of Conatiner:")
List.printList()
