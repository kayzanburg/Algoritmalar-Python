class Node:
    def __init__(self,key):
        self.val=key
        self.right=None
        self.left=None
        
def insert(root,node):
    if root is None:#eğer root boş ise node değeri roota atanır.
        root=node
        
    else:
        if root.val<node.val:#eğer tootun değeri node un değerinden küçük
        #ise koşula girer.
            if root.right is None:#root.right boş ise node root righta atanır.
                root.right=node
            else:#eğer root.right dolu ise özyinelemeli şekilde 
            #rootumuz root.right olacak şekilde yine kontrol edilir.
                insert(root.right,node)
        else:#nodeun değeri roottan büyük ise bu koşula girer.
            if root.left is None:#root.left boş ise node root.lefte atanır.
                root.left=node 
            else:#root.left dolu ise özyinelemeli olarak işlem devam eder.
                insert(root.left,node)
                