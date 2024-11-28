FilaAtendimento = []

def adicionar_cliente(nome):
    FilaAtendimento.append(nome)
    return "Adicionado com sucesso"

def atender_cliente():
    atendendo = FilaAtendimento.pop()
    return f"Atendendo: {atendendo}"

def tamanho_fila():
    return len(FilaAtendimento)

print(adicionar_cliente(input("Adionar cliente:")))
print("O tamanho atual da fila é ",tamanho_fila())
print("Atendendo atualmente, já foi removido da fila",FilaAtendimento)

