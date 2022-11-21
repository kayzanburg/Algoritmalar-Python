# Singly Linked List

class Node(object):
    def __init__(self, Value):
        self.Value = Value
        self.Next_Node = None
        
    def Set_Next_Node(self, Node):
        
        self.Next_Node = Node
        
    
    def Get_Next_Node(self):
        
        return self.Next_Node
    
    def Get_Node_Value(self):
        
        return self.Value


Canakkale = Node("17")
Tekirdag = Node("59")
Istanbul = Node("34")

Canakkale.Set_Next_Node(Tekirdag)

print("Canakkale'den Sonraki Gelecek Olan Ilin Plakasi : ", Canakkale.Get_Next_Node().Get_Node_Value())

Tekirdag.Set_Next_Node(Istanbul)

print("Tekirdag'dan Sonraki Gelecek Olan Ilin Plakasi : ", Tekirdag.Get_Next_Node().Get_Node_Value())

print("Canakkale'nin Iki Sonraki Gelecek Olan Ilin Plakasi : ", Canakkale.Get_Next_Node().Get_Next_Node().Get_Node_Value());

#%%

class Doubly_Linked_List_Node:
    
    def __init__(self, Value):
        
        self.Value = Value
        self.Next_Node = None
        self.Prev_Node = None
        
        
    def Set_Next_Node(self, Node):
        
        self.Next_Node = Node
    
    def Set_Prev_Node(self, Node):
        
        self.Prev_Node = Node
    
    def Get_Next_Node(self):
        
        return self.Next_Node
    
    def Get_Prev_Node(self):
        
        return self.Prev_Node
    
    def Get_Node_Value(self):
        
        return self.Value
    
    
    
Ankara = Doubly_Linked_List_Node("06")

Corum = Doubly_Linked_List_Node("19")

Samsun = Doubly_Linked_List_Node("55")





Ankara.Set_Next_Node(Corum)

Corum.Set_Next_Node(Samsun)


Samsun.Set_Prev_Node(Corum)

Corum.Set_Prev_Node(Ankara)

print("Corumdan Onceki Il : ", Corum.Get_Prev_Node().Get_Node_Value())

print("Ankaradan Sonraki Il : ", Ankara.Get_Next_Node().Get_Node_Value())

print("\n")


print("Corumdan Sonraki Il : ", Corum.Get_Next_Node().Get_Node_Value())

print("Samsundan Onceki Il : ", Samsun.Get_Prev_Node().Get_Node_Value())

#%%

# Linked List Node Eklemek

class Node(object):
    
    def __init__(self, data):
        self.data = data
        self.next = None




class LinkedList(object): # linked list class
    
    def __init__(self):
        
        self.head = None
    
    def push(self, new_data):
        
        new_node = Node(new_data)
        
        new_node.next = self.head
        
        self.head = new_node

    def insertAfter(self, prev_node, new_data):
        
        if prev_node is None:
            print("boyle bir node yok")
            return
        
        new_node = Node(new_data)
        
        new_node.next = prev_node.next
        
        prev_node.next = new_node
    
    def append(self, new_data):
        
        new_node = Node(new_data)
        
        if self.head is None:
            self.head = new_node
            return
        
        last = self.head
        while last.next:
            last = last.next
        
        last.next = new_node
    
    def printLinkedList(self):
        
        temp = self.head
        print("Linked list : ")
        while temp:
            print(temp.data)
            temp = temp.next




linked_list = LinkedList()
linked_list.push("tail")
linked_list.push("15")
linked_list.push("25")
linked_list.push("head")
linked_list.printLinkedList()

print("-------------")

linked_list.insertAfter(linked_list.head, 100)
linked_list.printLinkedList()

print("-------------")

linked_list.append("sona eklenen eleman")
linked_list.append("en sona node ekle")
linked_list.printLinkedList()

#%%

# Linked Linst node silmek

class Node(object):
    
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object): # linked list class
    
    def __init__(self):
        
        self.head = None
        
    def push(self, new_data):
    
        new_node = Node(new_data)
    
        new_node.next = self.head
    
        self.head = new_node

    def deleteNode(self, key):
        
        temp = self.head
        
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        
        prev.next = temp.next
        temp = None
    
    def printLinkedList(self):
        
        temp = self.head
        print("Linked list : ")
        while temp:
            print(temp.data)
            temp = temp.next





linked_list = LinkedList()
linked_list.push("ankara")
linked_list.push("bolu")
linked_list.push("istanbul")
linked_list.printLinkedList()

print("-------------")

linked_list.deleteNode("bolu")
linked_list.printLinkedList()
