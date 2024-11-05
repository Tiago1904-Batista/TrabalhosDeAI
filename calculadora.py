# Função de soma
def soma(x, y):
    return x + y

# Função de subtração
def subtração(x, y):
    return x - y

# Função de multiplicação
def multiplicação(x, y):
    return x * y

# Função de divisão
def divisão(x, y):
    return x / y

#O histórico começa numa lista vazia
historico = []

def calculadora():

    def adicionar_ao_historico(operacao):
        # Se o histórico já tiver 5 elementos, o mais antigo será removido (primeiro)
        if len(historico) >= 5:
            historico.pop(0)
            # Adiciona a nova operação ao final
        historico.append(operacao)

#Apresenta, no histórico a conta toda e não apenas o resultado
    def mostrar_historico():
        print("Histórico de operações:")
        for conta in historico:
            print(conta)
 
    #Começar a calculadora informa o que o utilizador pode fazer
    print("Escreva o sinal da conta que deseja realizar ou escreva ""Histórico"" para ver as últimas 5 contas que realizou")

    #Permitir que digite o sinal da operação (+; -; *; /)
    operacao = input("Digite o sinal da operação: ")

    # Se escolher o sinal "+", digita os dois números, dá o resultado e a conta (no total) vá para o histórico
    if operacao == "+":
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo digito: "))
        result = soma(num1, num2)
        conta = str(num1) + "+" + str(num2) + "=" + str(result)
        print("Resultado da soma: " + str(result))
        adicionar_ao_historico(conta)
        calculadora()

    # Se escolher o sinal "-", digita os dois números, dá o resultado e a conta (no total) vá para o histórico
    elif operacao == "-":
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        result = subtração(num1, num2)
        conta= str(num1) + "-" + str(num2) + "=" + str(result)
        print("Resultado da subtração: " + str(result))
        adicionar_ao_historico(conta)
        calculadora()

    # Se escolher o sinal "*", digita os dois números, dá o resultado e a conta (no total) vá para o histórico
    elif operacao == "*":
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        result = multiplicação(num1, num2)
        conta = str(num1) + "*" + str(num2) + "=" + str(result)
        print("Resultado da multiplicação: " + str(result))
        adicionar_ao_historico(conta)
        calculadora()

    ## Se escolher o sinal "/", digita os dois números, dá o resultado e a conta (no total) vá para o histórico
    elif operacao == "/":
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        if num2 !=0:
            result = divisão(num1, num2)
            conta = str(num1) + "/" + str(num2) + "=" + str(result)
            print("Resultado da divisão: " + str(result))
            adicionar_ao_historico(conta)
            calculadora()

        #Se o divisor for 0, apresenta uma impossíbilidade pois é impossivel dividir qualquer nº por 0
        else:
            print("Impossivel dividir por0")
            calculadora()

        #Se o utilizador digitar "Histórico" mostra as 5 mais recentes contas
    elif operacao == "Histórico":
        mostrar_historico()
        calculadora()

    #Se for escrito qualquer outra coisa dá um aviso para alterar o sinal escrito
    else:
        print("Sinal de operação não existente. Por favor altere.")
        calculadora()

calculadora() 
           

   
