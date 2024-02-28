class Node:
    def __init__(self, key):
        self.val = key
        self.right = None
        self.left = None
        
def insert(root, node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)
                
def search(root, key):
    if root is None or root.val == key:
        return root
    elif root.val < key:
        return search(root.right, key)
    else:
        return search(root.left, key)
            
r = Node(1)     
insert(r, Node(65))  
insert(r, Node(99))  
insert(r, Node(55))  
insert(r, Node(40))  
insert(r, Node(20))       

# Düzgün bir şekilde ekledikten sonra arama yapılıyor
print(search(r, 40).val)  # 40 çıktısını bekliyoruz
