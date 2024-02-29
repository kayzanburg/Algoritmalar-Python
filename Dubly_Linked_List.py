class Doblynode(object):
    def __init__(self,value):
        self.value=value
        self.nextnode=None
        self.prevnode=None
        
    def setnextnode(self,node):
        self.nextnode=node
        
    def setprevnode(self,node):
        self.prevnode=node
        
    def getnextnode(self):
         return self.nextnode
     
    def getprevnode(self):
            return self.prevnode
        
    def getnodevalue(self):
        return self.value
    
ankara= Doblynode("06")
corum= Doblynode("19")
samsun= Doblynode("55")

     