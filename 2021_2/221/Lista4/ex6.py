#Crie uma função que receba o nome e o sobrenome de uma pessoa e exiba (sem retornar) o 
#nome concatenado (nome completo)

def exibirNomeCompleto(nome : str, sobrenome : str):
    print("Nome Completo: " + nome + " " + sobrenome)


name = input("Digite o seu nome: ")
surName = input("Digite o seu sobrenome: ")
exibirNomeCompleto(name, surName)

