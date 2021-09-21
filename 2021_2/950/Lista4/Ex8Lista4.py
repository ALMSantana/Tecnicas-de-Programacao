#Crie uma função que receba dois dados do mesmo tipo e troque o 
# valor entre eles.

def swap(valor1, valor2):
    auxiliar = valor1
    valor1 = valor2
    valor2 = auxiliar
    return valor1, valor2

numero1 = 7
numero2 = 8

numero1, numero2 = swap(numero1, numero2)

print(numero1)
print(numero2)