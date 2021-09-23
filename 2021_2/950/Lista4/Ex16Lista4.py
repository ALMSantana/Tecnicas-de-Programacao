

def lerNumero():
    return int(input("Digite um número inteiro: "))

def tabuada(numero):
    contador = 1
    while (contador <= 10):
        print("{}x{} = {}".format(numero, contador, numero*contador))
        contador = contador + 1

def main():
    valor = lerNumero()
    tabuada(valor)

if __name__ == "__main__":
    main()