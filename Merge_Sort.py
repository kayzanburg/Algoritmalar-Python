def mergesort(arr):
    if len(arr)>1:
        mid=int(len(arr)/2)
        lefthalf=arr[:mid]
        righthalf=arr[mid:]
        mergesort(lefthalf)
        mergesort(righthalf)
         
        i=0
        j=0
        k=0
        while i<len(lefthalf) and j<len (righthalf):
            if lefthalf[i]<righthalf[j]:
                arr[k]=lefthalf[i]
                i+=1
            else:
               arr[k]=righthalf[j]
               j+=1
               
            k+=1
        while i<len(lefthalf):
            arr[k]=lefthalf[i]
            i+=1
            k+=1
        while j<len(righthalf):
            arr[k]=righthalf[j]
            j+=1
            
            k+=1
    return arr

               
# Kullanım örneği:
arr = [12, 11, 13, 5, 6, 7]
sorted_arr = mergesort(arr)
print("Sıralanmış dizi:", sorted_arr)