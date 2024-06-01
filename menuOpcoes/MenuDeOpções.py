from time import  sleep
a = int(input("Primeiro Valor: "))
b = int(input("Segundo Valor: "))
opcao = 0
while opcao != 5:
    print("=-" * 15)
    print("=-" * 15)
    print("MENU DE OPÇÕES:")
    print(" [ 1 ] Somar\n [ 2 ] Multiplicar\n [ 3 ] Maior\n [ 4 ] Novos Números\n [ 5 ] Sair do programa")
    opcoes = int(input("OPÇÃO: "))
    if opcoes == 1:
        soma = a + b
        print(f"A soma de {a} com {b} resulta em {soma}")
        sleep(2)
    elif opcoes == 2:
        multi = a * b
        print(f"A multiplicação de {a} com {b} resulta em {multi}")
        sleep(2)
    elif opcoes == 3:
        if a > b:
            print(f"O maior valor é o {a}")
            sleep(2)
        else:
            print(f"O maior valor é o {b}")
            sleep(2)
    elif opcoes == 4:
        print("Informe os números novamente")
        a = int(input("Primeiro Valor: "))
        b = int(input("Segundo Valor: "))
    elif opcoes == 5:
        print("Finalizando...")
        sleep(1)
        break
    else:
        print("Opção inválida, tente novamente !")
        break