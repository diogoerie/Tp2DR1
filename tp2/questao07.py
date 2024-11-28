def contar_pares(pilha):
    contagem = 0
    pilha_temporaria = []
    pares = []
    while pilha:
        pedido = pilha.pop()
        pilha_temporaria.append(pedido)
        if pedido % 2 == 0:
            contagem += 1
            pares.append(pedido)
    while pilha_temporaria:
        pilha.append(pilha_temporaria.pop())
    return contagem, pares
pilha = [11, 12, 15, 18, 11, 17, 25, 93, 42]
quantidade_pares, pares = contar_pares(pilha)
print("Quantidade de pedidos pares:", quantidade_pares)
print("Ids dos pedidos pares:", pares)
