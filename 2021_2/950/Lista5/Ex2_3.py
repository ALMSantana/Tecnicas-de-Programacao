#Crie uma coleção que suportará nomes de cidades. Após isso, interaja com o usuário questionando-o a 
#respeito de quantos elementos deseja inserir nesta lista. Em sequência, adicione nomes de cidades
#tantas quanto o número informado pelo usuário. Ao final, exiba a lista de cidades

def mostrarCidades(listaCidades):
    for umaCidade in listaCidades:
        print(umaCidade)


def mostrarCidadesComMais7Letras(listaCidades):
    for umaCidade in listaCidades:
        if(len(umaCidade) > 7):
            print(umaCidade)

def adicionarCidadeLista(listaCidades):
    cidade = input("Informe o nome da cidade que você deseja adicionar na coleção: ")
    listaCidades.append(cidade)

# dados primitivos


def main():
    lista = []

    listaCidades = []
    qtdCidades = int(input("Informe quantas cidades você deseja adicionar na coleção: "))

    while(qtdCidades != len(listaCidades)):
        adicionarCidadeLista(listaCidades)

    mostrarCidadesComMais7Letras(listaCidades)

if __name__ == "__main__":
    main()
