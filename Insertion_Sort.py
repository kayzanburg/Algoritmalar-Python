def insertionsort(arr):
    for i in range(1,len(arr)):
        currentval=arr[i]
        position=i
        
        while position>0 and arr[position-1]>currentval:
            arr[position]=arr[position-1]
            position-=1
        arr[position]=currentval
    return arr
arr=[3,2,13,4,6,5,7,8,1,20]
print(insertionsort(arr))
            