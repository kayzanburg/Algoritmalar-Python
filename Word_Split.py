def wordSplit(liste):
    
    word = list((liste[0])) # "deeplearning" => ["d","e"...]
    d = liste[1].split(",") # ["d","dll","a","deep","dee","base","lear","learning"]
    
    for i in range(1,len(word)):
        
        c = word[:]
        c.insert(i," ")
        x , y = "".join(c).split() # "d", "eeplearning" "de","eplearning"
        
        if x in d and y in d:
            
            return x + " , "+ y
        
    return "bulamadim (no way)"


print(wordSplit(["deeplearning", "d,dll,a,deep,dee,base,lear,learning"]))
print(wordSplit(["deeplear2ning", "d,dll,a,deep,dee,base,lear,learning"]))
print(wordSplit(["deeplear2ning", "d,dll,a,deep,dee,base,lear,lear2ning"]))