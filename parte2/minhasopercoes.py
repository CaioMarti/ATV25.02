def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: divisão por zero não é permitida."
    return a / b

def exibir_resultado(operacao, resultado):
    print(f"Resultado da operação {operacao}: {resultado}")

# main.py
from minhasopercoes import soma, subtracao, multiplicacao, divisao, exibir_resultado # type: ignore

def main():
    operacao = input("Escolha a operação (+, -, *, /): ")
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    
    if operacao == '+':
        resultado = soma(a, b)
    elif operacao == '-':
        resultado = subtracao(a, b)
    elif operacao == '*':
        resultado = multiplicacao(a, b)
    elif operacao == '/':
        resultado = divisao(a, b)
    else:
        print("Operação inválida.")
        return
    
    exibir_resultado(operacao, resultado)

if __name__ == "_main_":
    main()
