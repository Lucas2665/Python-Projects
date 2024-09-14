def menu():
    print("*-------------------------*")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Divisão")
    print("4 - Multiplicação")
    print("5 - Raís")
    print("0 - Sair")
    print("*-------------------------*")

    while True:
        n = int(input("Escolha uma das opções: "))
        if 0 <= n <= 5:
            return n
        else:
            print("Opção inválida! Escolha uma das opções acima.")


def operacao(opcao, x, y):
    match opcao:
        
        #SOMA
        case 1:
            return x + y
        
        #SUBTRAÇÃO
        case 2:
            return x - y

        #DIVISÃO
        case 3:
            return x / y

        #MULTIPLICAÇÃO
        case 4:
            return x * y

        #RAIS
        case 5:
            return x

def subtracao(x, y):
    return x - y

