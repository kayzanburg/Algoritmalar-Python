import math
def jumpSearch(arr,value):
    n=len(arr) #diziniz zunluğunu n değişkenine atadık.
    step=math.sqrt(n)# atlanacak adım sayısını buluyoruz.
    prev=0
    while arr[int(min(step,n)-1)] <value:# burda arana değerin bulunduğu bloğu buluruz.
        prev=step#step sayısını prev değişkenine atadık.
        step += math.sqrt(n)#step değişkenini diziniz kareköküyle arttırıyoruz.
        
        if prev >= n:#eğer adım sayımız n 'den büyük olursa -1 değerini döndürürüz.
            return -1
        
    while arr[int(prev)]<value:#eğerki prev  değerinin indeksinde bulunan eleman aradığımız değerden 
    #küçükse previ 1 er 1 er arttırarak doğrusal bir arama yaparız.
        prev += 1
        
        if prev == min(step,n):#eğer prev stepe eşit olursa -1 değerini döndürürüz.
            return -1
        
    if arr [int(prev)] == value:#eğerki prev indeksindeki eleman aradığımız değere eşitse 
    #indeksi yazdırırız.
        return int(prev)
    
    return -1 #aranan değer bulunamadıysa -1 değeri döner.

arr =[0,1,2,3,4,5,6,7,8,18,21,44]
jumpSearch(arr,44)

    