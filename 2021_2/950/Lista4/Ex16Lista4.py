

def lerNumero() -> int:
    return int(input("Digite um número inteiro: "))

def tabuada(numero: int) -> None:
    contador = 1
    while (contador <= 10):
        print("{}x{} = {}".format(numero, contador, numero*contador))
        contador = contador + 1

def main() -> None:
    valor = lerNumero()
    tabuada(valor)

if __name__ == "__main__":
    main()