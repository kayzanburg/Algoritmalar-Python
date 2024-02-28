def interpolationSearch(arr,lo,hi,x):#fonksiyon oluşturuldu.
    if (lo <= hi and x >= arr[lo] and x <= arr[hi]):#bu koşul sağlandıkça dizimizi bölerek aranan
    #bulmaya çaışacağız.
    
        pos = int(lo + ((hi - lo) /(arr[hi] - arr[lo]) * (x - arr[lo])))#interpolation formülü kullanılarak 
        #bir konum bulundu.
        if arr[pos] == x:#eğer buluna konumdaki değer aradığımız değere eşitse konum değeri döndürülür.
            return pos
        if arr[pos] < x: #eğer konum değerimizdeki sayı aradığımız değerden küçük ise dizimizin sağ tarafına 
        #bakmamızı sağlayacak işlem döndürülür.
            return interpolationSearch(arr, pos + 1,hi, x)#burda lo değerini pos+1 yaparsak diziniz ilk elemanı pos+1 konumundaki
          #eleman olur.Böylelikle arama yapılacak dizi küçülür ve pos elemanının sağ tarafında arama yapılır.
                                                
        if arr[pos] > x:#eğer konum değerimizdeki sayı aradığımız değerden büyükse dizimizin sol tarafına 
        #bakmamızı sağlayacak işlem döndürülür.
            return interpolationSearch(arr, lo,pos - 1, x)#burda hi değerimizi pos-1 yaparsak dizimiziz son elemanı pos-1 
        #konumundaki eleman olur.Böylelikle arama yapılacak dizi küçülür ve pos elemanının sol tarafında arama yapılır.
                                     
    return -1 #eğer aranan değer bölme işlemlerinden sonra bulunamazsa -1 değeri döndürülür.

arr = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
n = len(arr)
x = 33
index = interpolationSearch(arr, 0, n - 1, x)
 
if index != -1: # index değeri -1 e eşit değilse yani eleman bulunduysa bu koşul çalışır.
    print("Eleman bulundu", index)
else: #if koşulu sağlanmadığı durumlarda else ifadesi içindeki işlem yapılır.
    print("Eleman bulunamadı.")