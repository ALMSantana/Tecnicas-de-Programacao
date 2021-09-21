# Leia uma nota de um usuário (de 0 a 10)
# Caso a nota seja 10, armazene um conceito A
# Caso a nota seja maior ou igual a 9 e menor que 10, armazene conceito B
# Caso a nota seja maior ou igual a 8 e menor que 9, armazene o conceito C

nota = float(input("Digite a sua nota: "))
conceito = "I"

if(nota == 10):
    conceito = "A"
elif(nota >=9 and nota < 10):
    conceito = "B"
elif(nota >=8 and nota < 9):
    conceito = "C"
elif(nota >= 7 and nota < 8):
    conceito =  "D"
elif(nota >= 6 and nota < 7):
    conceito = "F"
elif(nota >=0 and nota < 6):
    conceito = "-F"
else:
    conceito = "I"
    print("Você digitou uma nota inválida!")    
print(conceito)
    
