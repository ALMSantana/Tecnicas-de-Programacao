# guardar em uma coleção estudantes da turma 950 e suas respectivas notas da n1


def criarAluno():
    novoAluno = {}
    novoAluno["nome"] = input("Digita o nome do aluno: ")
    novoAluno["RA"] = input("Digite o RA do aluno: ")
    novoAluno["nota"] = float(input("Informe a nota do aluno: "))
    return novoAluno


def main():
    listaAlunos = []
    qtdAlunos = int(input("Informe quantos alunos você deseja adicionar a sua lista: "))

    while(qtdAlunos != len(listaAlunos)):
        umAluno = criarAluno()
        listaAlunos.append(umAluno)

    print(listaAlunos[0]["nome"])

if __name__ == "__main__":
    main()