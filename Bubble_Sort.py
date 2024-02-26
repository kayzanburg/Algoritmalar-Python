def bubble_sort(array):
    for i in range(1, len(array)):
        for j in range(len(array) - i):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
    
    return array

numbers = [1, 12, 2, 5, 6, 1, 8, 55, 8, 8, 2, 17]

print("Sıralanmış array: {}".format(bubble_sort(numbers)))