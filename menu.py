import calculadora

# git commit -am "ap01(git-python): opção somar implementada"
# git commit -am "ap01(git-python): opção subtrair implementada"
# git commit -am "ap01(git-python): opção multiplicar implementada"
# git commit -am "ap01(git-python): opção divisao implementada"



def menu():
    while True:
        print("\nEscolha uma opção:")
        print("1 para Somar")
        print("2 para Subtrair")
        print("3 para Multiplicar")
        print("4 para Dividir")
        print("0 para Sair")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == '1':
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            print("Resultado:", calculadora.somar(a, b))
        elif opcao == '2':
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            print("Resultado:", calculadora.subtrair(a, b))
        elif opcao == '3':
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            print("Resultado:", calculadora.multiplicar(a, b))
        elif opcao == '4':
            a = float(input("Digite o primeiro número: "))
            b = float(
                input("Digite o segundo número (não pode ser zero): "))
            print("Resultado:", calculadora.divisao(a, b))
        elif opcao == '0':
            print("Saindo...")
            break
        

menu()
