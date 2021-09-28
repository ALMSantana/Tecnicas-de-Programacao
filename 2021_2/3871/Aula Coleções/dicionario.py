# Dicionários são formados por pelo menos dois elementos
# Uma chave e um valor

# Criando um dicionário vazio
dicionarioAluno = {} ##dicionario
listaAlunos = [] ##lista

# Criando um dicionario com conteúdo
valdir = {"nome":"Valdir Augusto de Carvalho", "idade":18, "corFavorita":"Verde"}
andreSantana = {"nome":"André Luiz Maciel Santana", "idade":30, "corFavorita":"Rosa"}

# Atualizando o valor de uma chave
valdir["nome"] = "Valdir A. Carvalho"

# Exibindo o conteúdo de um dicionário
print("\nColeção Valdir:", valdir)

# Acessar o conteúdo de uma chave específica
print("\nAcessando a chave 'nome' no dicionário: ", valdir['nome'])

# Ver todas as chaves existentes em um dicionario
print("\nAs chaves neste dicionário são: ", valdir.keys())

# Ver todos os valores em um dicionario
print("\nTodos os valores do dicionário são: ", valdir.values())

# Ver todos os items na coleção
print("Ver todos os items na coleção: ", valdir.items())

print ("\n\nDicionário de Dicionários \n")

turma221 = { "141414": {"nome": "André Santana", "mediaFinal": 9.0}, "101010": {"nome": "Luiz Santana", "mediaFinal": 6.0} }

print(turma221["141414"]["nome"])
print(turma221["101010"]["nome"])

#Verificando se uma chave existe em um dicionário
# Como temos "141414" a resposta para o teste será True
# No caso de 99999 será false
print("141414" in turma221)
print("99999" in turma221)