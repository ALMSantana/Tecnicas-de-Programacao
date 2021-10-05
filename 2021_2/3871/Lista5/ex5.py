# Crie uma coleção que armazenará apenas as notas de alunos de uma turma. Após isso, crie algumas 
# funções que permitirão (i) cadastrar notas dos alunos (ii) exibir todas as notas (iii) calcular a média das 
# notas, retornando o valor da média e (iv) exiba a média.

def solicitarNotaAluno():
    nota = float(input("Digite o valor da nota do aluno: "))
    return nota

def calcularMediaLista(listaNotasAlunos):
    somaNotas = 0

    for umaNota in listaNotasAlunos:
        somaNotas = somaNotas + umaNota
    
    return somaNotas / len(listaNotasAlunos)

def calcularMediaListaV2(listaNotasAlunos):
    return sum(listaNotasAlunos) / len(listaNotasAlunos)

def main():
    notasAlunos = []
    qtdNotas = int(input("Informe quantas notas você deseja: "))

    while(len(notasAlunos) != qtdNotas):
        notasAlunos.append(solicitarNotaAluno())

    print("Média: ", calcularMediaLista(notasAlunos))
    print("Média: ", calcularMediaListaV2(notasAlunos))

if (__name__ == "__main__"):
    main()