#sırasız listede arama
def linearsearch(liste,value):
    index=0
    found=False
    while index<len(liste) and  not found:
        if liste[index]==value:
            found=True
            
        else:
            index+=1
    return (found,index)
    
liste=[5,7,2,3,15,8,100,12]
found,index=linearsearch(liste,15)
print(found)
print(index)

#sıralı listede arama
def linearsearchs(liste,value):
    index=0
    found=False
    stop=False
    while index<len(liste) and not found and not stop:
        if liste[index]==value:
            found=True
            
        else:
            if value<liste[index]:
                stop=True
            else:
               index+=1
    return (found,index)

liste=[2,3,5,7,8,12,15,100]
found,index=linearsearchs(liste,11)
print(found)
print(index)






        
        
        
                