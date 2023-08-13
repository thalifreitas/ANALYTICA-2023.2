# PROBLEMA 4 - FREQUENCIA DE NUMEROS


def frequencia(valores):
    frequencias = {}  # dicionario vazio

    for num in valores:
        frequencias[num] = frequencias.get(num, 0) + 1  # calcula a frequencia de cada valor na lista de valores

    return frequencias


def main():
    valores = []  # lista para guardar os valores digitados

    while True:
        entrada = input("> ")  # recebe qualquer tipo de dado

        if entrada == 'f':
            break  # encerra o programa caso o input recebido seja 'f'

        try:
            valor = int(entrada)  # converte o valor recebido para int
            valores.append(valor)  # adiciona esse valor para a lista de valores

        except ValueError:
            pass  # ignora casos em que é recebido um input inválido

    freq_valores = frequencia(valores)  # utiliza a funcao 'frequencia' para calcular a frequencia dos valores digitados

    for valor, freq in freq_valores.items():
        if freq == 1:
            print(f'O número {valor} apareceu {freq} vez.')
        else:
            print(f'O número {valor} apareceu {freq} vezes.')

    print("Fim...")


if __name__ == "__main__":
    main()
