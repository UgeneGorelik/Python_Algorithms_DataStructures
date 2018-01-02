#implementation of Node of liked list

class Node:
    def __init__(self,data):
        self.data=data
        self.next =None

    def getData(self):
        return self.data

    def setData(self,data):
        self.data

    def setNext(self,next_Node):
        self.next=next_Node


#implementation of linked list iteslf

class LinkedList:
    def __init__(self):
        self.head=None

    def isEmpy(self):
        return  self.head==None

    def Add(self,item):
       tmp=Node(item)
       tmp.setNext(self.head)
       self.head=tmp

    def getNext(self):
        return self.next

    def size(self):
        current=self.head
        counter=0
        while current.next is not None:
            counter+=1
            current=current.getNext()

    def search(self,item):
        current=self.head
        found=False
        while current!=None and found!=True:
            if current.getData==item:
                return True
            else:
                current=current.getNext()
        return False











