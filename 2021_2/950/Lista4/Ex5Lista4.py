#Crie uma função que receba o nome e o sobrenome de uma pessoa e 
# retorne os dois nomes concatenados (nome completo)

def gerarNomeCompleto(nome, sobrenome):
    return nome + " " + sobrenome

def italoEdition(nome:str, sobrenome:str):
  return "{} {}".format(nome,sobrenome)

#no input edition
nomeCompleto = gerarNomeCompleto("André Luiz", "Maciel Santana")

#input edition
nome = input("Digite o seu nome: ")
sobrenome = input("Digite o seu sobrenome: ")
nomeCompleto = gerarNomeCompleto(nome, sobrenome)
print(nomeCompleto)