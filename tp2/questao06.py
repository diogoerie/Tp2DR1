def contar_impares(pilha):
    contagem = 0
    pilha_temporaria = []
    impares = []
    while pilha:
        pedido = pilha.pop()
        pilha_temporaria.append(pedido)
        if pedido % 2 != 0:
            contagem += 1
            impares.append(pedido)
    while pilha_temporaria:
        pilha.append(pilha_temporaria.pop())
    return contagem, impares
pilha = [11, 12, 15, 18, 11, 17, 25, 93, 42]
quantidade_impares, impares = contar_impares(pilha)
print("Quantidade de pedidos ímpares:", quantidade_impares)
print("Ids dos pedidos ímpares que entraram em promoção:", impares)


