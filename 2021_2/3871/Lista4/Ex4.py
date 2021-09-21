#Crie uma função que receba como parâmetro um valor, verifique se este valor é 
# negativo, e neste caso converta ele para positivo retornando-o ao usuário
def converterSeNegativoV1(numero : float) -> float:
    if (numero < 0):
        numero = numero * -1
    return numero

def converterSeNegativo(numero : float) -> float:
    return abs(numero)

def main():
    converterSeNegativo(-3)

if __name__ == "__main__":
    main()