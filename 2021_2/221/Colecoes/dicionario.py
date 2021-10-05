# Criar um dicionário
listaAlunos = []
jefferson = {"nome":"Jefferson Dantas", "idade": 22, "cor":"vermelho", "nota": 10.0}

# Ver todas a chave
print(jefferson.keys())

# Ver todos o valores
print(jefferson.values())

# Acessar o conteúdo de uma chave
print(jefferson["nome"])
print(jefferson.get("nome"))

# Adicionar uma chave nova?
jefferson["turma"] = "221"