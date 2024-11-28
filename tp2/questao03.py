def verificar_lento(array):
    n = len(array)
    for i in range(n):
        for j in range(i + 1, n):
            if array[i] == array[j]:
                return True
    return False

array = [1, 2, 3, 4, 5, 6, 7, 8, 2]
resultado = verificar_lento(array)
if resultado == True:
    print("A lista contém itens duplicados.")
else:
    print("A lista não contém itens duplicados.")


def verificar_rapido(array):
    seen = set()
    for item in array:
        if item in seen:
            return True
        seen.add(item)
    return False
resultado = verificar_rapido(array)
if resultado == True:
    print("Duplicado encontrado!")
else:
    print("Sem duplicados.")
