#Crie uma função que receba o nome e o sobrenome de uma pessoa e 
# retorne os dois nomes concatenados (nome completo)
def gerarNomeCompleto(nome : str, sobrenome : str) -> str:
    return nome + sobrenome  

def main():
    userName = input("Digite o seu nome: ")
    surName = input("Digite o seu sobrenome: ")
    print(gerarNomeCompleto(userName, surName))

if __name__ == "__main__":
    main()
