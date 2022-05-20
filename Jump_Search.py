import math # Karekok Almak Icin Matematik Kutuphanesini Import Ettik

def Jump_Search(List, Value):# Liste Ve Aranacak Olan Degeri Fonksiyona Parametre Olarak Ekledik
    
    Liste_Uzunlugu = len(List) # Listenin Uzunlugunu Aliyoruz
    
    Step = math.sqrt(Liste_Uzunlugu) # Atlanacak Degeri Buluyoruz
    # Sonrasinda Ise Bu Deger Indexlede Atlama Yapacagi Icin Surekli Arttiriyoruz Ve Arama Yapmasini Sagliyoruz.
    Prev = 0 # Arama Yaparken Bir Onceki Bulundugu Konum
    # Listenin Icerisinde Belirtilen Atlama Sayisi Kadar Atlama Yaparak Sirali Liste Icerisinde Arama Yapmaya Baslar.
    # Eger Aranacak Olan Degerin Index Degeri Gecildi Ise ( Liste Sirali Oldugundan Anlasilir Bu Durum) Geri Doner
    # Ve En Son Atlama Yaptigi Degerin Bir Sag Tarafindan Linear Bir Sekilde Arama Yapmaya Baslar.
    while List[int(min(Step, Liste_Uzunlugu)-1)] < Value:
        
        
        Prev = Step # Atlama Yapilan Deger Bir Onceki Gecilen Index'e Esitlenir.
        
        # Atlama Yapacak Olan Deger Arttirilir.
        Step += math.sqrt(Liste_Uzunlugu)
        
        # Asagidaki if Yapidi Liste Icerisinde Aranan Deger Bulunamaz Ve Aranan Deger Listedeki Tum Elemanlardan Buyuk Ise Calisir.
        if Prev >= Liste_Uzunlugu:
            return -1
    # Liste Icerisinde Linear Arama Yapar
    while List[int(Prev)] < Value:
        Prev += 1
        # Bir sonraki Atlanacak Olan Degere Ulasildi Ise Veya Array'in Son Index'ine Ulastiysak
        # Ve Aranan Deger Bulunamadi Ise Asagidaki Code Blogu Calisir.
        if Prev == min(Step, Liste_Uzunlugu):
            return -1
    
    # Aranan Degerin Bulundugu Ve Index Degerinin Ekrana Yazdirildigi Yer.
    if List[int(Prev)] == Value:
        return int(Prev)
    # Asagidaki deger linear Arama Yapilip Bulunamadigi Veya Degerin Negatif Bir Deger Oldugu Taktirde Return Edilir.
    return -1


List = [0,1,2,3,4,5,6,7,8,18,21,44]

print(Jump_Search(List, 18))