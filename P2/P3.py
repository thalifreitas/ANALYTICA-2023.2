# PROBLEMA 3 - CALCULADORA DE TROCO

import re


def calculadora(valor):
    notas = [10000, 5000, 2000, 1000, 500, 200]  # valores das notas em centavos
    moedas = [100, 50, 25, 10, 5, 1]  # valores das moedas em centavos

    # dicionarios vazios para armazenar a quantidade de cada nota e moeda
    qtd_notas = {}
    qtd_moedas = {}

    valor_cent = int(valor*100)  # passando o valor digitado para centavos

    for nota in notas:
        qtd_n = valor_cent // nota  # quantidade de cada nota
        valor_cent %= nota  # valor restante apos retirar a quantidade de notas já calculada

        qtd_notas[nota] = int(qtd_n)  # adicionando no dicionario a quantidade de cada nota respectivamente

    for moeda in moedas:
        qtd_m = valor_cent // moeda  # quantidade de cada moeda
        valor_cent %= moeda  # valor restante apos retirar a quantidade de moedas já calculada

        qtd_moedas[moeda] = int(qtd_m)  # adicionando no dicionario a quantidade de cada moeda respectivamente

    print("NOTAS:")
    for nota, qtd in qtd_notas.items():
        print(f'{qtd} nota(s) de R$ {nota/100:.2f}')

    print("\nMOEDAS:")
    for moeda, qtd in qtd_moedas.items():
        print(f'{qtd} moeda(s) de R$ {moeda/100:.2f}')


def main():

    while True:
        entrada = input("> ")

        try:

            if re.match(r'^\d+\.\d{2}$', entrada):  # conferindo se o input inserido possui duas casas decimais
                calculadora(float(entrada))
                break

            else:
                raise Exception  # input inserido nao possui duas casas decimais

        except Exception:
            print("Input inválido!")
            continue


if __name__ == "__main__":
    main()
