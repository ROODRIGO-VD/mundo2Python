numero = int(input("Digite um número inteiro: "))
opcoes = int(input("Escolha qual será sua base de conversão:\n [ 1 ] Binário\n [ 2 ] Octal\n [ 3 ] Hexadecimal\n "
                   "OPÇÃO:  "))
if opcoes == 1:
    print(f"{numero} convertido para BINÁRIO é igual a {bin(numero)[2:]}")
elif opcoes == 2:
    print(f"{numero} convertido para OCTAL é igual a {oct(numero)[2:]}")
elif opcoes == 3:
    print(f"{numero} convertido para HEXADECIMAL é igual a {hex(numero)[2:]}")
else:
    print("Opção inválida, tente novamente!")