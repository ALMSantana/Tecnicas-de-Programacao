def buscarUsuario(nome, listaUsuarios):
    for usuario in listaUsuarios:
        if (usuario["nome"] == nome):
            return usuario


andre = {"nome": "André Santana"}
valdir = {"nome": "Valdir Augusto"}
ruan = {"nome": "Ruan Lima"}

listaUsuarios = [andre, valdir, ruan]
listaUsuarios.append({"nome": "Murtada Mobarak"})

print(buscarUsuario("André Santanaa", listaUsuarios))