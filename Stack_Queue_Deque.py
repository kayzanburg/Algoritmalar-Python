# Stack Yapisi

class Stack:
    
    def __init__(self):
        
        """
        initialize (constructor)
        """
        
        self.items=[]


    def isEmpty(self):
        
        """
        bos olup olmadigini kontrol eder
        """
        
        return self.items==[] # boolean operation


    def push(self,item):
        
        """
        stack'e item ekler
        """
        
        self.items.append(item)

    def pop(self):
        """
        stack'ten item cikarma
        """

        return self.items.pop()


    def top(self):
        
        """
        stack icerisindeki son item'i gosterir
        """

        return self.items[len(self.items)-1]


    def size(self):
        
        """
        size of stack
        """
        
        return len(self.items)



stack=Stack()
print(stack.isEmpty())

stack.push("ankara")
print(stack.top())

stack.push("istanbul")
print(stack.top())

stack.push("izmir")
print(stack.top())

print(stack.size())

stack.pop()
print(stack.top())

stack.pop()
print(stack.top())

print(stack.isEmpty())

stack.pop()
print(stack.isEmpty())


#%%


class Queue:
    def __init__(self):
        
        """
        initialize (constructor)
        """
        
        self.items=[]
        
        
    def isEmpty(self):
        
        """
        bos olup olmadigini kontrol et
        """
        
        return self.items==[] # bool operation
    
    
    def enqueue(self,item):
        
        """
        queue item ekler
        """
        
        self.items.insert(0,item)
        
        
    def dequeue(self):
        
        """
        queue dan item cikartir
        """
        
        return self.items.pop()
    
    
    def size(self):
        
        """
        length of items(queue)
        """
        
        return len(self.items)




queue = Queue()

print(queue.isEmpty())

queue.enqueue("ankara")
queue.enqueue("istanbul")
print("size: ",queue.size())

queue.dequeue()
print("size: ",queue.size())

queue.dequeue()
print("size: ",queue.size())
queue.isEmpty()

#%%

class Deque:
    def __init__(self):
        
        """
        initialize (constructor)
        """
        
        self.items=[]
        
        
    def isEmpty(self):
        
        """
        bos olup olmadigini kontrol et
        """
        return self.items==[]# bool operation
    
    
    def addFront(self,item):
        
        """
        deque ya front kismindan item ekler
        """
        self.items.append(item)
        
        
    def addRear(self,item):
        
        """
        deque ya rear kismindan yeni item ekler
        """
        self.items.insert(0,item)
        
        
    def removeFront(self):
        
        """
        deque front kismindan item cikartir
        """
        
        return self.items.pop()
    
    
    def removeRear(self):
        
        """
        deque rear kismindan iterm cikart
        """
        
        return self.items.pop(0)
    
    
    def size(self):
        
        """
        length of deque
        """
        
        return len(self.items)




deque=Deque()
print(deque.isEmpty())
deque.addFront("deep")
deque.addRear("learning")
print("size: ",deque.size())
print(deque.isEmpty())
deque.removeFront()
deque.removeRear()
print(deque.isEmpty())


#%%

"""Stack Kullanarak String'in Tersini Bulmak"""



# define stack metod
def createStack(): 
    
    stack=[]
    return stack


# stack size
def size(stack):
    
    pass


# stack top method
def top(stack):
    
    pass


# isEmpty
def isEmpty(stack):
    
    pass


# push method
def push(stack,item):
    
    stack.append(item)


# pop method
def pop(stack):
    
    return stack.pop()


# find reverse as using stack
def reverse(string):
    
    n=len(string)
    stack=createStack() # stack
    
    
    # string icerisindeki her bir harfi stack icerisine depola
    for i in range(n):
        push(stack,string[i]) # "d","a","t","a","i" stack = ["d","a","t","a","i"]
    new_string=""
    
    
    # pop
    for i in range(n):
        
        new_string+=pop(stack) # "i", "a",... # new_string = "iatad"
        
    return new_string


print("datai: ",reverse("datai"))
print("machine learning: ",reverse("machine learning"))



#%%


"""Python da Listeyi Stack ve Queues Gibi Kullanmak"""

# liste kullanarak stack yapmak
stack=["datai","ml","ai"] # liste
stack.append("deep")
stack.append("learning") # append = push
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)

#%%

# liste ve deque kullanarak queue yapmak
from collections import deque
queue=deque(["datai","ml","ai"])
print(queue)
queue.insert(0,"deep")
print(queue)
queue.insert(0,"learning")
print(queue)
queue.pop()
print(queue)
queue.pop()
print(queue)
# insert yerine append ve pop yerine popleft

#%%

"""İki Stack Kullanarak Queue yaratmak"""


class Queue2Stack(object):
    
    def __init__(self):
        
        """
        initialize 2 stacks
        """
        
        self.stack1=[]
        self.stack2=[]
        
        
    def enqueue(self,item):
        
        """
        stack'e item eklemek ama queue yaratmak icin
        """
        self.stack1.append(item)
        
        
    def dequeue(self):
        
        """
        stack1'in icinden pop yaparak stack2 nin icine item yollamak
        """
        if not self.stack2:
            while len(self.stack1)>0:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()



# queue object
queue=Queue2Stack()
queue.enqueue("1")
queue.enqueue("2")
queue.enqueue("3")
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())