from minhasopercoes import soma, subtracao, multiplicacao, divisao, exibir_resultado 

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
