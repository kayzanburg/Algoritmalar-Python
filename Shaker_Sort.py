def shaker_sort(arr):
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1
    
    while swapped:
        # Sağa doğru geçiş
        swapped = False
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        if not swapped:
            break
        
        # Sağa doğru geçişte bir eleman yer değiştirdiyse end'i bir azalt
        end -= 1
        
        # Sola doğru geçiş
        swapped = False
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        if not swapped:
            break
        
        # Sola doğru geçişte bir eleman yer değiştirdiyse start'ı bir artır
        start += 1
    
    return arr

# Test
dizi = [64, 25, 12, 22, 11]
siralanmis_dizi = shaker_sort(dizi)
print("Sıralanmış dizi:", siralanmis_dizi)
