class Vertex:
    def __init__(self,key):
        self.id=key
        self.connetedto={}
        
    def addneigbour(self,neigbour,weight=0):
        self.connectedto[neigbour]=weight
    def __str__(self):
        return str(self.id)+"connectedvto:"+str([x.id for x in self.connectedto])
    def getconnections(self):
        return self.connectedto.keys()
    def getid(self):
        return self.id
    def getweight(self,neighbour):
        return self.neighbour[neighbour]
    
class Graph:
    def __init__(self):
        self.vertlidt={}
        self.numvert=0
        
    def addvertex(self,key):
        self.numvert+=1
        newvertex=Vertex(key)
        self.vertlist[key]=newvertex
        return newvertex
    
    def getvertex(self,n):
        if n in self.vertlist:
            return self.vertlist[n]
        else:
            return None
        
    def addedge(self,f,t,cost=0):
        if f not in self.vertlist:
            nv=self.addvertex(f)
        if t not in self.vertlist:
            nv=self.addvertex(t)
        self.vertlist[f].addneighbour(self.vertlist[t],cost)
        
    def getvertices(self):
        return self.vertlist.keys()
    
    def __iter__(self):
        return iter(self.vertist.values())
    
        
            
        
        
    
        
        
        
        
        
        
        
        
        