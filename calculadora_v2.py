saida = ''

def adicao(a,b):
    return a + b

def subtracao(a,b):
    return a - b

def multiplicacao(a,b):
    return a * b

def divisao(a,b):
    if b == 0:
        return "Não foi possível realizar a divisão por 0"
    else:
        return a / b

def calculadora(num1, num2, operacao):
    resultado = None
    if operacao == '+' or operacao == 'adição':
        resultado = adicao(num1, num2)
    elif operacao == '-' or operacao == 'subtração':
        resultado = subtracao(num1, num2)
    elif operacao == '*' or operacao == 'multiplicação':
        resultado = multiplicacao(num1, num2)
    elif operacao == '/' or operacao == 'divisão':
        resultado = divisao(num1, num2)
    else:
        resultado = "Operação inválida"
    return resultado

while saida.lower() != 'n':
    try:
        primeiro_numero = float(input("Digite o primeiro número: "))
        segundo_numero = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação matemática (+, -, *, / ou nome da operação): ").strip().lower()
        
        resultado = calculadora(primeiro_numero, segundo_numero, operacao)
        
        print(f"Resultado da operação: {resultado}")
        
        saida = input("Deseja continuar? (S/N): ").strip().lower()
        
    except ValueError:
        print("Entrada inválida. Por favor, insira números válidos.")

print("Programa encerrado.")
