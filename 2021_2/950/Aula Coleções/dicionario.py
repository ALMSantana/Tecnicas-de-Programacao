# criando uma lista
listaFrutas = ["Manga", "Maçã", "Banana"]

# criando um dicionário
dicionarioPokemons = {"001":"Bulbasaur", "002":"Ivysaur", "003":"Venusaur"}

henrique950 = {"RA": "02020203", "nome":"Henrique Barbosa", "email": "henrique.barbosa@anhembi.edu.br"}

# exibindo um dicionário
print(dicionarioPokemons)

# consultar chaves do dicionário
print(dicionarioPokemons.keys())

# consultar só valores no dicionário
print(dicionarioPokemons.values())

for pokemon in dicionarioPokemons.values():
    print(pokemon)

# adicionar um novo elemento
dicionarioPokemons["004"] = "Charmander"

for pokemon in dicionarioPokemons.values():
    print(pokemon)


# Dicionario de Alunos
print("\n")
dicionarioAlunos = {"01010101":"Renato Silva", "02020202": "Caio Victor"}
print(dicionarioAlunos["01010101"])