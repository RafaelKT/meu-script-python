print("Calculadora Aprendizado")

# Solicita ao usuário que digite os valores a serem calculados e a operação desejada
valor_1 = float(input("Digite o primeiro valor: "))
valor_2 = float(input("Digite o segundo valor: "))
operacao = input("Digite o tipo de operação (Soma, Subtracao, Divisao, Multiplicacao): ").lower().strip()

# Inicializa a variável resultado como None para validar se uma operação válida foi realizada
resultado = None

# Verifica a operação escolhida e realiza o cálculo correspondente
if operacao == "soma":
    resultado = valor_1 + valor_2
elif operacao == "subtracao":
    resultado = valor_1 - valor_2
elif operacao == "multiplicacao":
    resultado = valor_1 * valor_2
elif operacao == "divisao":
    # Verifica se o segundo valor é diferente de zero antes de dividir
    if valor_2 != 0:
        resultado = valor_1 / valor_2
    else:
        print("Erro: divisão por zero não é permitida.")
else:
    print("Operação inválida. Tente: Soma, Subtracao, Divisao ou Multiplicacao.")

# Exibe o resultado caso a operação tenha sido válida
if resultado is not None:
    print(f"O resultado da {operacao} é: {resultado}")


print("Fiz uma alteração no meu código para testar a feature_2")


print("Fiz mais uma alteração para criação de uma nova feature_03")

#Criado uma nova branch para novo teste que eu acho que é o pullrequest que eu não sei para que serve esta merda

