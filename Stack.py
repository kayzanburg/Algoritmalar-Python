class Stack():
    def __init__(self):
        self.items=[]
    def  isempty(self):
        return self.items==[]
    
    def push(self,item):
        self.items.append(item)
        
    def pop(self):
        self.items.pop()
        
    def top(self):
        return self.items[ len(self.items)-1]
    def size(self):
         return len(self.items)        