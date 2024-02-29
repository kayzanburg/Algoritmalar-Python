class Node(object):
    def __init__(self,data):
         self.data=data
         self.node=None
         
class Linkedlist(object):
    def __init__(self):
        self.head=None
        
    def push(self,ndata):
        nnode=Node(ndata)
        
        nnode.next=self.head
        
        self.head=nnode
    def insertafter(self,prevnode,ndata):
        if prevnode is None:
            print("-1")
            return
        
        nnode=Node(ndata)
        nnode.next=prevnode.next
        prevnode.next=nnode
        
    def append(self,ndata):
        nnode=Node(ndata)
        if self.head is None:
             self.head=nnode
             return 
        last=self.head
        while last.next:
         last=last.next
         
        last.next=nnode
        
    def print(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        