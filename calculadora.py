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

   
