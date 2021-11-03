import random

SALA_DESTINO = 9
TENTATIVAS_MAXIMAS = 7
CAMINHO_VERMELHO = 1
CAMINHO_PRETO = 2

def validarRotaSala(salaAtual, caminhoEscolhido):
    return not(salaAtual == 6 and caminhoEscolhido == CAMINHO_VERMELHO)
    
def desenharErroSala6(salaAtual, caminhoEscolhido):
    print("Você está na sala ", salaAtual, " e o caminho ", caminhoEscolhido, " não é válido!")

def desenharMenu(salaAtual):
    print("Você está na sala {}".format(salaAtual))
    print("[1] - Caminho Vermelho")
    print("[2] - Caminho Preto")

def escolherCaminho(salaAtual):
    desenharMenu(salaAtual)
    caminhoEscolhido = int(input())

    while(not(validarRotaSala(salaAtual, caminhoEscolhido))):
        desenharErroSala6(salaAtual, caminhoEscolhido)
        desenharMenu(salaAtual)
        caminhoEscolhido = int(input())

    return caminhoEscolhido

def verificarResultadoGame(salaAtual):
    return salaAtual == SALA_DESTINO

def exibirRestultado(salaAtual, qtdInteracoes):
    if(verificarResultadoGame(salaAtual)):
        print("Você venceu, com {} tentativas.".format(qtdInteracoes))
    else:
        print("Você utilizou {} interações, desta forma perdeu!".format(qtdInteracoes))


def game():
    salaAtual = 1
    qtdInteracoes = 0
    while(salaAtual != SALA_DESTINO and qtdInteracoes < TENTATIVAS_MAXIMAS):
        escolhaUsuario = escolherCaminho(salaAtual)

        while(escolhaUsuario < 1 or escolhaUsuario > 2):
            escolhaUsuario = escolherCaminho(salaAtual)

        if(escolhaUsuario == CAMINHO_VERMELHO and salaAtual != 6):
            salaAtual += 1
        elif(escolhaUsuario == CAMINHO_PRETO and salaAtual != 8):
            salaAtual += 2
        else:
            salaAtual = random.randint(1, 5)
            qtdInteracoes -= 1

        qtdInteracoes += 1

    exibirRestultado(salaAtual, qtdInteracoes)

def main():
    game()

if __name__ == "__main__":
    main()
