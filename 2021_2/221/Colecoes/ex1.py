# crie uma solução para armazenar as notas de estudantes da turma, e além disso, \
# salvar o ra e nome dos estudante.

def criarAluno():
    alunoTemp = {}
    alunoTemp["nome"] = input("Digite o nome do aluno: ")
    alunoTemp["RA"] = input("Digite o RA do aluno: ")
    alunoTemp["nota"] = float(input("Digite a nota do aluno: "))
    return alunoTemp

def mostrarNomesAlunos(listaAlunos):
    for aluno in listaAlunos:
        print(aluno["nome"])

def main():
    listaAlunos = []
    qtdAlunos = int(input("Informe quantos alunos você deseja salvar na lista: "))
    contador = 0

    while(contador < qtdAlunos):
        alunoTemp = criarAluno()
        listaAlunos.append(alunoTemp)
        contador = contador + 1
    
    mostrarNomesAlunos(listaAlunos)

if(__name__ == "__main__"):
    main()
