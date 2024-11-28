array = [10,9,8,7,6,5,4,3,2,1]

def ordenar(array):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
ordenar(array)
print("Lista ordenada:", array)
