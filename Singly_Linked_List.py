# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 14:41:28 2022

@author: Lenovo
"""
class Node(object):
    def __init__(self,value):
        self.value=value
        self.nextnode=None
        
    def setnextnode(self,node):
        self.nextnode=node
   
    def getnextnode(self):
       return self.nextnode
   
    def getnodevalue(self):
        return self.value
          
ankara=Node("06")
çorum=Node("19")
samsun=Node("55")
        
