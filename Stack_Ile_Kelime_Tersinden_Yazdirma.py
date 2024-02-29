def createstack():
    stack=[]
    return stack
def push(stack,item):
  return   stack.append(item)
    
def pop(stack):
   return stack.pop()
def reverse(string):
    n=len(string)
    stack=createstack()
    for i in range(n):
         push(stack,string[i])
    newstring=" "
    for i in range(n):
        newstring +=stack.pop()
    return newstring
print("Python:",reverse("Python"))