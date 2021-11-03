#Crie uma coleção que suportará nomes de cidades. Após isso, interaja com o usuário 
# questionando-o a 
#respeito de quantos elementos deseja inserir nesta lista. Em sequência, adicione nomes de 
# cidades
#tantas quanto o número informado pelo usuário. Ao final, exiba a lista de cidades.

def mostrarCidades(listaCidades:list):
    print("Lista Completa\n")
    for umaCidade in listaCidades:
        print(umaCidade)

def mostrarCidadesMais7Letras(listaCidades : list):
    print("Lista com mais de 7 letras \n")
    for umaCidade in listaCidades:
        if(len(umaCidade) > 7):
            print(umaCidade)

def main():
    listaCidades = []
    qtdCidades = int(input("Digite a quantiadade de cidades: "))

    while (qtdCidades != len(listaCidades)):
        cidade = input("Digite a cidade que você deseja armazenar: ").lower()
        listaCidades.append(cidade)

    mostrarCidades(listaCidades)
    mostrarCidadesMais7Letras(listaCidades)

if (__name__ == "__main__"):
    main()