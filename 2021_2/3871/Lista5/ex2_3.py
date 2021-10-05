# Crie uma coleção que suportará nomes de cidades. Após isso, interaja com o usuário questionando-o a 
# respeito de quantos elementos deseja inserir nesta lista. Em sequência, adicione nomes de cidades
# tantas quanto o número informado pelo usuário. Ao final, exiba a lista de cidades

def mostrarCidades(listaCidades):
    for umaCidade in listaCidades:
        print(umaCidade)

def main():
    listaCidades = []
    qtdCidades = int(input("Digite a quantidade de cidades que você deseja adicionar a sua coleção: "))

    while(len(listaCidades) != qtdCidades):
        novaCidade = input("Digite o nome da cidade: ")
        listaCidades.append(novaCidade)

    mostrarCidades(listaCidades)

if (__name__ == "__main__"):
    main()
