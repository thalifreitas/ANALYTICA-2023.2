# PROBLEMA 2 - MOVIMENTACAO DO CAVALO NO XADREZ

def movimentacao(x, y):

    if (x == 1 and y == 2) or (x == 2 and y == 1):
        print("VÁLIDO")

    else:
        print("INVÁLIDO")


def main():

    while True:
        entrada = input("> ").lower()

        if entrada == 'f':
            break

        try:

            posicoes = entrada.replace(" ", "")  # retirar espaços digitados
            lista_pos = list(posicoes)  # lista com cada caractere digitado

            # cada entrada, apos ser colocada em uma lista, estara no formato
            # [letra, numero, letra, numero], onde o primeiro par 'letra, numero'
            # eh referente a posicao inicial, e o segundo par 'letra, numero'
            # eh referente a posicao final

            # conversao tabela ASCII das letras digitadas
            pos1 = ord(lista_pos[0]) - 96
            pos3 = ord(lista_pos[0 + 2]) - 96

            # conversao para int dos numeros digitados
            pos2 = int(lista_pos[0 + 1])
            pos4 = int(lista_pos[0 + 3])

            # No xadrez, um cavalo pode se movimentar da seguinte forma:
            # dando 2 passos na vertical/eixo y + 1 passo na horizontal/eixo x -> [2,1]
            # OU dando 2 passos na horizontal/eixo x + 1 passo na vertical/eixo y - [1,2]
            # Com isso, para saber se foi feita uma movimentacao valida, basta saber se
            # a diferenca entre a posicao inicial e final no eixo x eh igual a 2 (1) E
            # se a diferenca entre a posicao inicial e final do eixo y eh igual a 1 (2).
            dif_x = abs(pos1 - pos3)
            dif_y = abs(pos2 - pos4)

            movimentacao(dif_x, dif_y)

        except Exception as erro:
            print("Erro: Input inválido!")
            continue


if __name__ == "__main__":
    main()
