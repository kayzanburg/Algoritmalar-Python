class DynamicArray:
    def __init__(self):
        self.capacity = 1  # Başlangıçta kapasiteyi 1 olarak ayarlayalım
        self.length = 0    # Başlangıçta dizi boş olduğu için uzunluk 0 olacak
        self.arr = self.make_array(self.capacity)  # Kapasiteye göre bir dizi oluşturalım

    def __len__(self):
        return self.length

    def __getitem__(self, index):
        if not 0 <= index < self.length:
            return IndexError('Geçersiz dizin!')
        return self.arr[index]

    def append(self, element):
        if self.length == self.capacity:
            # Kapasite dolu olduğunda, kapasiteyi iki katına çıkaran ve mevcut elemanları kopyalayan bir fonksiyon çağrısı yapalım
            self.resize(2 * self.capacity)

        self.arr[self.length] = element
        self.length += 1

    def resize(self, new_capacity):
        new_arr = self.make_array(new_capacity)
        for i in range(self.length):
            new_arr[i] = self.arr[i]

        self.arr = new_arr
        self.capacity = new_capacity

    def make_array(self, capacity):
        return [None] * capacity

# Kullanım örneği:
dyn_array = DynamicArray()
dyn_array.append(1)
dyn_array.append(2)
dyn_array.append(3)
dyn_array.append(4)

print("Dinamik dizi elemanları:", end=" ")
for i in range(len(dyn_array)):
    print(dyn_array[i], end=" ")
