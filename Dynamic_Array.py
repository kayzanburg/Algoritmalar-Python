import ctypes # yeni array yaratmak icin kullanacagiz

class DynamicArray(object):
    
# initialize (constructor)
    def __init__(self):
        self.n = 0 # eleman sayisi
        self.capacity = 1 # kapasite
        self.A = self.make_array(self.capacity)
        
    def __len__(self):
        """
        return array icerisinde eleman sayisi
    """
        return self.n
    
    def __getitem__(self,k):
        """
        return index k'da ki eleman(value)
        """
        if not 0 <= k < self.n:
            return IndexError("k is out of bounds !")
        return self.A[k]
    
    def append(self,eleman):
        """
        array'e eleman ekler
        """
        # eger kapasite dolu ise kapasiteyi iki katina cikar
        if self.n == self.capacity:
            self._resize(2*self.capacity)
        self.A[self.n] = eleman # eleman ekleme
        self.n += 1 # eleman sayisi bir arttir
            
    def _resize(self,new_cap):
        """
        array kapasitesini arttir
        """
        B = self.make_array(new_cap) # yeni array yap
        # eski array (A) icerisindeki degerleri yeni arraye(B) icine tasi
        for k in range(self.n):
            B[k] = self.A[k]
        self.A = B # arrayi guncelle
        self.capacity = new_cap # kapasite guncelle
            
    def make_array(self,new_cap):
        """
        return yeni array
        """
        return (new_cap*ctypes.py_object)()







# obje tanimla
arr = DynamicArray()
# append new element 1
arr.append(1)
print(arr[0])
# append new element 1 , 3
arr.append(3)
print(arr[0],arr[1])
# append new element 1 , 3 ,5
arr.append(5)
print(arr[0],arr[1],arr[2])