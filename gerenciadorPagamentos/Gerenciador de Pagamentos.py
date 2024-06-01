valor = float(input("Qual o valor do produto: R$"))
opcoes = int(input("Selecione uma opção de pagamento:\n [ 1 ] À vista no Dinheiro / Cheque\n [ 2 ] À vista no cartão"
                   "\n [ 3 ] Em até 2x no cartão\n [ 4 ] Em até 3x ou mais no cartão\n OPÇÃO: "))
if opcoes == 1:
    print(f"Pagando à vista no dinheiro / chegue, o valor de cai {valor}R$, para {valor - (valor * 0.1)}R$")
elif opcoes == 2:
    print(f"Pagando à vista no cartão, o valor cai de {valor}R$, para {valor - (valor * 0.05)}R$ ")
elif opcoes == 3:
    print(f"Pagando em até 2x no cartão, o valor se mantém em {valor}R$")
elif opcoes == 4:
    print(f"Pagando em 3x ou mais no cartão, o valor vai de {valor}R$, para {valor * 1.2}R$")
