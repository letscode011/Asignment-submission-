# Assignment No.4
# Q.1
# Sachin Dharankar.
# Linked List

class node:
    def __init__(self,data):
        self.data = data 
        self.next = None

class sll:
    def __init__(self):
        self.head = None

    def InsertBeg(self,data):
        newnode = node(data)
        newnode.next = self.head
        self.head = newnode 

    def deleteEnd(self): 
        if self.head == None:
            print("Empty Linked list nothing to delete")
            return
        temp = self.head
        while temp.next.next != None:
            temp = temp.next
        temp.next = None    

    def display(self):
        if self.head == None:
            print("Linked list is empty nothing to display")
            return
        temp = self.head 
        while temp != None:
            print(temp.data, end=" ")
            temp = temp.next

obj = sll()
obj.InsertBeg(20)
obj.InsertBeg(10) 
obj.InsertBeg(30)
obj.InsertBeg(40) 
obj.deleteEnd() 
obj.display()                  