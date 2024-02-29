def ortalama(n):
 toplam =0    # 1 kere çalışır.
 sayac=0      #1 kere çalışır.
 for sayi in range (1,n+1):   #n kere çalışır.
   
   toplam = toplam + sayi     #n  kere çalışır.
   sayac +=1                  #n kere çalışır.
 print('Ortalama',(toplam/sayac))   #1  kere çalışır
   
ortalama(122)    #Big-o su :O(n) 'dir.