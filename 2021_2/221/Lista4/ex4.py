#Crie uma função que receba como parâmetro um valor, verifique se este valor é negativo, e 
#neste caso converta ele para positivo retornando-o ao usuário

def converterParaPositivoV1(numero : float):
    if (numero < 0):
        return numero * -1
    return numero

def converterParaPositivo(numero : float):
    return abs(numero)



valor = int(input("Digita um número aí: "))
print(converterParaPositivo(valor))
print(converterParaPositivoV1(valor))