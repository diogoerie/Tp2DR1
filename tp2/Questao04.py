
def ordenar_notas(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

array = [75, 85, 25, 90, 47, 82, 90]
ordenar_notas(array)
print("Lista de notas ordenadas:", array)
