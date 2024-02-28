def binarysearch(liste,value):
    firstindex=0
    lastindex=len(liste)-1
    found=0
    while firstindex<=lastindex and not found:
        midindex=int((firstindex+lastindex)/2)
        if liste[midindex]==value:
            found=True
        else:
            if value<liste[midindex]:
                lastindex=midindex-1
                print("lower half")
                
                
            else:
                firstindex=midindex+1
                print("upper half")
                
    return found
liste=[3,6,11,12,18,21,34]
binarysearch(liste,18)