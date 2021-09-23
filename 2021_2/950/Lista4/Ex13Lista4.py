#13) Escreva um programa que leia o raio de um círculo e faça duas funções: uma função chamada 
#area que calcula e retorna a área do círculo e outra função chamada perimetro que calcula e 
#retorna o perímetro do círculo.

#Área = π * r2
#Perímetro = π * 2 * r

PI = 3.1415926535897932384626433

def calcularAreaCirculo(raio :float) -> float:
    return (PI * (raio ** 2))


def calcularPerimetroCirculo(raio : float) -> float:
    return PI * 2 * raio

def main():
    raio = float(input("Digite o raio do círculo: "))
    areaCirculo = calcularAreaCirculo(raio)
    print(areaCirculo)

if (__name__ == "__main__"):
    main()