def square_sum1(n):
    return (n*(n+1)*(2*n+1))/6

square_sum2(3)


%timeit square_sum1(3)


#%%

import numpy as np

array = np.array([[1,2,3,4,5]]) # vector 1D
print(array)
print("Boyut: ",array.shape)

#%%

array2D = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(array2D)
print("boyut: ",array2D.shape)
print("2. satır 4. sütun: ",array2D[1,3])