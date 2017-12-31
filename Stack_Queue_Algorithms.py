#implementation of a stack

class Stack:
    def __init__(self):
        self.items=[]


    def isEmpty(self):
        return  self.items==[]

    def push(self,item):
        self.items.append(item)


    def pop(self):
        popped_item=self.items.pop()
        return popped_item

    def peek(self):
          return self.items[len(self.items)-1]


#implementation of a stack that holds record of a minimal Value

class MinStack:
    def __init__(self):
        self.items=[]
        self.minitems=[]

    def isEmpty(self):
        return  self.items==[]

    def push(self,item):
        self.items.append(item)

#this implementation of stack is designed  to return the
# minimal element so on push we push the minimal element too
        if len(self.minitems)!=0 and self.minitems[len(self.minitems)-1]>item:
            self.minitems.append(item)
        elif len(self.minitems) == 0:
            self.minitems.append(item)

    def pop(self):
        popped_item=self.items.pop()
# stack is designed to return the minimal element
        if (popped_item==self.minitems[len(self.minitems)-1]):
            self.minitems.pop()
            return popped_item

    def peek(self):
    #returns also the minimal elemnt
        return self.items[len(self.items)-1],self.minitems[len(self.minitems)-1]


class Queue:

    def __init__(self):
        self.items=[]

    def is_empty(self):
        return (self.items==[])

    def push(self,item):
        self.items.insert(0,item)

    def pop(self):
        return self.items.pop()

#implement a queue using 2 stacks
class QueueUsingStack:
    def __init__(self):
        self.ourstack = Stack()
        self.helpstack=Stack()

    def is_empty(self):
        return (self.ourstack.isEmpty())

    def push(self, item):
        self.ourstack.push(item)

    def pop(self):
        while not self.ourstack.isEmpty():
            self.helpstack.push(self.ourstack.pop())

        popped_item=self.helpstack.pop()

        while not self.helpstack.isEmpty():
            self.ourstack.push(self.helpstack.pop())

        return popped_item

    def peek(self):
        print(self.ourstack.peek())


#implementation of a stack using 2 queues
class StackUsingQueues:
    def __init__(self):
        self.ourQueue=Queue()
        self.helpQueue = Queue()



    def isEmpty(self):
        return  self.ourQueue.is_empty()

    def push(self,item):
       self.helpQueue.push(item)
       while not self.ourQueue.is_empty() :
            self.helpQueue.push(self.ourQueue.pop())

       self.ourQueue=self.helpQueue
       self.helpQueue=Queue()


    def pop(self):
        popped_item=self.ourQueue.pop()
        return popped_item




#check if the parenthesis are balanced using stack
def check_parenthesis(st):
    s=Stack()
    for x in st:
        if x=='(':
            s.push(x)
        else:
            s.pop()

    return (s.isEmpty())




# s=Stack()
#
# s.push(2)
# s.push(2)
# s.push(1)
# s.push(3)
#
# print(s.peek())

# print(check_parenthesis('((())'))

s=QueueUsingStack()

s.push(1)
s.push(2)
s.push(3)
print(s.pop())





