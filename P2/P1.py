# PROBLEMA 1 - CALCULADORA DE ANGULOS ENTRE PONTEIROS DO RELOGIO

import re


def calcula_angulo(horario):

    minutos = int(horario[1])/5
    # para saber para qual valor, que vai de 1 a 12 no relogio, o ponteiro dos minutos
    # estara apontando

    angulo_horas = ((int(horario[0])-minutos)*30)
    # calcula o angulo entre os ponteiros das horas e dos minutos

    angulo_minutos = ((int(horario[1])*30)/60)
    # quando inserimos horarios que nao estejam no formato hh:00
    # sempre teremos um pequeno angulo formado pelo ponteiro das horas
    # Aqui calculamos esse pequeno angulo

    angulo = angulo_horas + angulo_minutos
    # ao somar os angulos calculados anteriormente, achamos o angulo total formado
    # pelos ponteiros das horas e minutos

    if angulo > 180:
        angulo = abs(360 - angulo)
        # certificando que sera o menor angulo possivel

    return angulo


def main():

    while True:
        entrada = input("\nDigite um horário no formato 'hh:mm': ").lower()

        if entrada == 'f':
            print("Fim...")
            break

        try:

            if re.match(r'^[0-2][0-9]:[0-5][0-9]$', entrada):
                # confere se a entrada esta no formato hh:mm

                angulo = calcula_angulo(entrada.split(':'))
                # chama funcao que calculara o angulo de acordo com a entrada inserida
                print(f"O menor ângulo é de {angulo}º")

            else:
                raise Exception()

        except Exception:
            print("Erro: Input inválido!")
            continue


if __name__ == "__main__":
    main()
