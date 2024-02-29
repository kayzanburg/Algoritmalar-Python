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
    def deletenode(self,key):
        temp=self.head
        
        if temp is not None:
             if temp.data==key:
              self.head=temp.next
              temp=None
             
        while  temp is not None:
            if temp.data==key:
                break
            prev=temp
            temp=temp.next
        prev.next=temp.next
        temp=None
        

    def print(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next
            
        
        
        
        
        
        