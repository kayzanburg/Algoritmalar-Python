def binarySearch(liste, value):
    

    """binary search for sorted array (sirali liste)""" 

    first_index = 0
    last_index = len(liste) - 1
    
    found = False
    
    while first_index <= last_index and not found:
    
        middle_index = int((first_index + last_index)/2)
        if liste[middle_index] == value:
            found = True
        else:
            # Lower half
            if value < liste[middle_index]:
                last_index = middle_index - 1
                print ("lower half")
            # upper half
            else:
                first_index = middle_index +1
                print("upper half")
    return found

 

liste = [3,6,11,12,18,21,34]

print(binarySearch(liste,18))