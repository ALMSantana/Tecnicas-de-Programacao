# "Batata"
# é uma string | é cuma constante | 6 caracteres | A repete três vezes | Tem duas letras t

# Como crio variaveis em Python
qtdAlunosPresentes = 48
maiorNota950N1 = 10.0
nomeDisciplina = "Técnicas de Programação"

print(type(qtdAlunosPresentes))

# Criando uma lista em Python
listaAlunos = [] #criei uma lista vazia
listaPedrasPreciosas = ["Ametista", "Safira", "Rubi"]

# adicionando elementos na lista
listaPedrasPreciosas.append("Pérola") #adicionando no final da lista

novaPedraPreciosa = input("Digite o nome de uma pedra preciosa: ") #adicionando com input
listaPedrasPreciosas.append(novaPedraPreciosa) #adicionando uma variavel

# exibindo o conteúdo de uma lista
print(listaPedrasPreciosas)

# inserindo com insert
listaPedrasPreciosas.insert(2, "Diamante Rosa")
listaPedrasPreciosas.insert(2, "Diamante Rosa")
print(listaPedrasPreciosas)

# remover um elemento, utilizando um conteúdo
deletarPedraPreciosa = input("Informe a pedra preciosa você deseja remover: ")

if (deletarPedraPreciosa in listaPedrasPreciosas):
    listaPedrasPreciosas.remove(deletarPedraPreciosa)

## lista atual
print("\n\n")
print(listaPedrasPreciosas)

listaPedrasPreciosas.sort()

print("\nPós-Sort")
print(listaPedrasPreciosas)

for umaPedraPreciosa in listaPedrasPreciosas:
    if("Safira" == umaPedraPreciosa):
        print("Encontrou a safira!")

#['Ametista', 'Diamante Rosa', 'Esmeralda', 'Pérola', 'Rubi', 'Safira']
# para identificar um elemento em uma lista pelo índice, faço este tipo de acesso
print(listaPedrasPreciosas[2])
 
tunico = listaPedrasPreciosas[2] ## atribuindo a uma variável um elemento da lista
print(tunico)