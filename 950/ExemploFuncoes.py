# Criar uma função que verifica se um número é negativo ou positivo
# Caso seja negativo, deve retornar para quem "a chamou" o valor False
# Caso seja positivo, deve retornar para quem "a chamou" o valor True

def verificarSeEhPositivo(numero):
    if(numero >= 0):
        return True
    else:
        return False

# numero = 5
def verificarSeEhPositivoAvancada(numero):
    if(numero >= 0):
        return True
    return False

#numero = -5
def verificarSeEhPositivoSuperAvancada(numero):
    return numero >= 0

def exibirMenu():
    print("Olá! Este é o Super Game do Labirinto - V1.0")
    print("Digite 1 para ir para direita.")
    print("Digite 2 para ir para esquerda.")

    print("Fim")

numero = int(input("Digita um número inteiro aí: "))
numero2 = int(input("Digita outro numero: "))

print(verificarSeEhPositivoAvancada(numero))
print(verificarSeEhPositivoAvancada(numero2))

interacoes = 0
while(interacoes <= 7):
    exibirMenu()
    interacoes = interacoes + 1


