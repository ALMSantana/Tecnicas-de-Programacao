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

def main():
    listaAlunos = []
    
    listaAlunos.append(criarAluno())
    listaAlunos.append(criarAluno())
    listaAlunos.append(criarAluno())

    exibirNomesAlunosLista(listaAlunos)

if __name__ == "__main__":
    main()