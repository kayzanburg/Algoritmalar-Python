import random

def shell_sort(dizi):
    n = len(dizi)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = dizi[i]
            j = i
            while j >= gap and dizi[j - gap] > temp:
                dizi[j] = dizi[j - gap]
                j -= gap
            dizi[j] = temp
        gap //= 2

# Rastgele 10000 sayı oluştur
sayilar = [random.randint(1, 1000) for _ in range(10000)]

# Sırala
shell_sort(sayilar)

# İlk 20 sayıyı yazdır
for i in range(20):
    print(sayilar[i])
