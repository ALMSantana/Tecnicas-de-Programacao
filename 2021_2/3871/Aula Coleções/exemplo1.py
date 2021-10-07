# Desejo guarda nome de alunos e suas respectivas notas. Adicionar RA por conveniencia
# Dicionário com dicionários (?) - by Valdir
# Listas junto com dicionários (?) - Allan

def criarAluno():
    novoAluno = {}
    novoAluno["nome"] = input("Digita o nome do Aluno: ")
    novoAluno["RA"] = input("Digite o seu RA: ")
    novoAluno["nota"] = float(input("Digite a nota do aluno: "))
    return novoAluno

def exibirNomesAlunosLista(listaAlunos : list):
    for umAluno in listaAlunos:
        print(umAluno["nome"])

def desenharMenu():
    print("0 - para sair")
    print("1 - Cadastrar um usuário")
    print("2 - Exibir todos os usuário")

def main():
    listaAlunos = []
    
    desenharMenu()
    opcao = int(input("Digite a opcao desejada: "))

    while(opcao != 0):
        if(opcao == 1):
            listaAlunos.append(criarAluno())
        elif(opcao == 2):
            exibirNomesAlunosLista(listaAlunos)

if __name__ == "__main__":
    main()