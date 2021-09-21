# Solicite ao usuário sua idade e se ele possuí ou não, carteira de 
# habilitação (CNH).  Caso ele tenha 18 anos de idade e possua CNH
# Então, exiba a mensagem: Você pode dirigir! Caso ele tenha 18 anos de idade
# Mas não tenha CNH, exiba a mensagem, você precisa tirar a CNH primeiro
# Por fim, caso não tenha completado 18 anos de idade, exiba a mensagme
# Você ainda é menor de idade.

idade = int(input("Digite a sua idade:"))
temCNH = input("Digite S se você tem CNH ou N caso não tenha: ").lower()

if (idade >= 18):
    if(temCNH == "s"):
        print("Você pode dirigir!")
    else:
        print("Você tem que tirar a CNH primeiro!")
else:
    print("Você ainda é menor de idade!")