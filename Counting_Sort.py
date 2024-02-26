def counting_sort(arr):
    # En büyük elemanı bul
    max_element = max(arr)
    
    # Elemanları saymak için bir sayıcı dizisi oluştur
    count = [0] * (max_element + 1)
    
    # Sayıcı dizisini güncelle
    for element in arr:
        count[element] += 1
    
    # Yeniden oluşturulmuş sıralanmış diziyi oluştur
    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i] * count[i])
    
    return sorted_arr

# Test
dizi = [4, 2, 2, 8, 3, 3, 1]
siralanmis_dizi = counting_sort(dizi)
print("Sıralanmış dizi:", siralanmis_dizi)
