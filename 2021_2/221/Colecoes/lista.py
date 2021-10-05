# Como criamos variáveis?

idade  = 30 # inteiro
salario = 15000.0 # real
nomeTurma = "Técnicas de Programação  - 221"# texto
aprovados = True # lógico

# Lista
 
listaNomes = [] #criando vazia
listaNomes = list() #criando vazia
listaPedrasPreciosas = ["Rubi", "Safira"] #criando com dados

# Exibir os dados de uma lista
print(listaPedrasPreciosas)
print(listaPedrasPreciosas[0])
print(listaPedrasPreciosas[1])

# Tamanho -> comprimento de uma lista ou de uma coleção -> length
print(len(listaPedrasPreciosas))

# Adicionando elementos na lista
listaPedrasPreciosas.append("Ametista")
print(listaPedrasPreciosas)
listaPedrasPreciosas.insert(2, "Pérola")
print(listaPedrasPreciosas)

listaPedrasPreciosas2 = ["Peridote" ,  "Lapis Lazuli"]
listaPedrasPreciosas.extend(listaPedrasPreciosas2)
print(listaPedrasPreciosas)

# quantas peridotes tem na lista?
print(listaPedrasPreciosas.count("Peridote"))

# Como saber se um elemento faz parte da coleção
print("Pérola" in listaPedrasPreciosas)

if("Pérola" in listaPedrasPreciosas):
    print("Existe Pérola!")

if(listaPedrasPreciosas.count("Pérola") > 0):
    print("Existe Pérola!")

# Removendo um elemento da lista
copiaDados = listaPedrasPreciosas.copy()
print("Lista Original: ", listaPedrasPreciosas)
print("Cópia: ", copiaDados)

copiaDados.clear()

print("Lista Original: ", listaPedrasPreciosas)
print("Cópia: ", copiaDados)

# Removendo um único elemento
listaPedrasPreciosas.append("Diamante Rosa")
print("Lista Completa: ", listaPedrasPreciosas)
listaPedrasPreciosas.remove("Diamante Rosa")
print("Lista Completa (Pós-Remoção): ", listaPedrasPreciosas)

elementoRemovido = input("Digite o nome do elemento que deseja remover: ")

if(elementoRemovido in listaPedrasPreciosas):
    listaPedrasPreciosas.remove(elementoRemovido)
else:
    print("O elemento não está na lista!")

# Ordenar elementos
listaPedrasPreciosas.sort(reverse=True)
print("Lista Ordenada: ", listaPedrasPreciosas)

contador = 0

# Como percorrer uma lista?
for umaPedra in listaPedrasPreciosas:
    print(umaPedra)
  
    if (umaPedra == "Safira"):
        contador = contador + 1
    elif(umaPedra == "Rubi"):
        contador = contador + 1
    
    if(contador == 2):
        listaPedrasPreciosas.append("Garnet")
        contador = 0



