#Crie uma função que receba o nome e o sobrenome de uma pessoa e 
# retorne os dois nomes concatenados (nome completo)

def gerarNomeCompleto(nome, sobrenome):
    return nome + " " + sobrenome

def main():
    print(gerarNomeCompleto("Bolinho da Silva", "Sauro")) 

if __name__ == "__main__":
    main()

    