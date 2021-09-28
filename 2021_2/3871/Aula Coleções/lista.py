# Como eu crio uma lista vazia
listaCores = []

# Como eu crio uma lista com elementos pré-definidos
listaPedrasPreciosas = ["Rubi", "Safira"]

# Eixibindo o conteúdo de uma lista
print("Conteúdo da Lista de Cores: ", listaCores)
print("Conteúdo da Lista de Pedras Preciosas: ", listaPedrasPreciosas)

# Verificando o tamanho da lista com o método len()
print("Tamaho da lista de cores é: ", len(listaCores))
print("Tamanho da lista de pedras preciosas é: ", len(listaPedrasPreciosas))

# Acessando um elemento por sua posição
print("Elemento na primeira posição: ", listaPedrasPreciosas[0]) ##Acesso o primeiro elemento, ou seja, Rubi
print("Elemento na segunda posição: ", listaPedrasPreciosas[1]) ##Acesso o segundo elemento, ou seja, Safira

# Adicionando pedras preciosas em uma lista
listaPedrasPreciosas.append("Ametista")
listaPedrasPreciosas.append("Citrino")
listaPedrasPreciosas.append("Diamante")
listaPedrasPreciosas.append("Diamante")
print("Versão nova da lista: ", listaPedrasPreciosas)

# Count para verificar quantas cópias eu tenho de um elemento na minha coleção
print("Quantos diamante existem na lista: ", listaPedrasPreciosas.count("diamante"))
print("Quantos Diamante existem na lista: ", listaPedrasPreciosas.count("Diamante"))

# Sort
listaPedrasPreciosas.sort()
print("Lista ordenada: ", listaPedrasPreciosas)

# Remover a primeira cópia do elemento especificado por parâmetro
listaPedrasPreciosas.remove("Ametista") ## Caso existe este elemento, remove da coleção
print("Lista após a remoção: ", listaPedrasPreciosas)

print("\n\nResultado do ForEach\n")
# Percorrendo e imprimindo todos os elementos da lista
for umaPedraPreciosa in listaPedrasPreciosas:
    print(umaPedraPreciosa)