def Interpolation_Search(List, First, Last, Value):

    if (First <= Last and Value >= List[First] and Value <= List[Last]): # Aracak Sayi Listenin Ilk Elemanindan Buyuk, Son Elemandan Kucukmu Diye Kontrol Ediyoruz.
       
        Ort_Konum = int(First + ((Last - First) / (List[Last] - List[First]) * (Value - List[First]))) # Formule Gore Ortalama Baslama Noktasi Belirlenir.

        if List[Ort_Konum] == Value: # Eger Aranan Deger Ort_Konum'daysa Return Ettirilir.
            return Ort_Konum

        if List[Ort_Konum] < Value: # Eger Aranan Deger Ort_Konum daki Degerden Buyukse , Ort_Konumun Sag Tarafi Yeni Liste Olur.
            return Interpolation_Search(List, Ort_Konum + 1, Last, Value)

        if List[Ort_Konum] > Value: # Eger Aranan Deger Ort_Konum daki Degerden Kucukse , Ort_Konumun Sol Tarafi Yeni Liste Olur.
            return Interpolation_Search(List, First, Ort_Konum - 1, Value)

    return -1 # Eleman Listde Bulunamaz Ise -1 Degeri Return Ettirilir.

List = [3, 7, 11, 15, 22, 41, 42, 47, 55, 67, 84, 89, 92, 93, 96]

Liste_Uzunlugu = len(List) # Listenin Eleman Sayisini Aldik.

Value = 89 # Arama Yapilacak Degerimiz

Deger = Interpolation_Search(List, 0, Liste_Uzunlugu - 1, Value)

if Deger != -1: # Eger Aranan Deger Liste Icerisinde Ise Index Degerini Ekrana Yazdiracaktir, Bulamaz Ise Bulunamadi Yazdiracaktir.
    print("Aranan Ifadenin Index Degeri :", Deger)

else:
    print("Liste Icerisinde Aranan Deger Bulunamadi.")