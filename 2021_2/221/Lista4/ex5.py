#Crie uma função que receba o nome e o sobrenome de uma pessoa e retorne os dois nomes 
# concatenados (nome completo)
#Ex.: envio André e envio Santana e a função retorna André Santana
def concatenarNome(nome : str, sobrenome : str):
    return nome + " " + sobrenome 

def main():
    name = input("Digite o seu nome: ")
    surName = input("Digite o seu sobrenome: ")

    nomeCompleto = concatenarNome(name, surName)
    print("O nome completo é: " + nomeCompleto)
    print("O nome completo é: {}".format(nomeCompleto))

if __name__ == "__main__":
    main()
   