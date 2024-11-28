def contar_impares(lista):
    contagem = 0
    lista_temporaria = []
    impares = []
    while lista:
        pedido = lista.pop()
        lista_temporaria.append(pedido)
        if pedido % 2 != 0:
            contagem += 1
            impares.append(pedido)
    while lista_temporaria:
        lista.append(lista_temporaria.pop())
    return contagem, impares
entrada = input("Coloque os identificadores:")
lista = list(map(int, entrada.split()))
quantidade_impares, impares = contar_impares(lista)
print("Quantidade de pedidos ímpares:", quantidade_impares)
print("Ids dos pedidos ímpares que entraram em promoção:", impares)

