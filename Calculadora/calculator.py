import Calculadora.Modules_Calc as mod

print("Bem Vindo!\n\n")

escolha = mod.menu()

num1 = float(input("\nInsira o primeiro número: "))
num2 = float(input("Insira o segundo número: "))

resultado = mod.operacao(escolha, num1, num2)

print(f"O resultado é: {resultado}")