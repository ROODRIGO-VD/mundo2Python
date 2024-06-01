import random
def lin():
    print("-=" * 5)
    print("JOKENPÔ")
    print("-=" * 5)

escolha = input("Selecione entre PEDRA, PAPEL ou TESOURA: ").upper()
lin()
lista = ["PEDRA", "PAPEL", "TESOURA"]
maquina = random.choice(lista)

#USUARIO GANHAR
if escolha == "PEDRA" and maquina == "TESOURA":
    print(f"Você escolheu {escolha} e a máquina {maquina}, Pedra ganha da Tesoura, parabéns!")
elif escolha == "TESOURA" and maquina == "PAPEL":
    print(f"Você escolheu {escolha} e a máquina {maquina}, Tesoura ganha do Papel, parabéns!")
elif escolha == "PAPEL" and maquina == "PEDRA":
    print(f"Você escolheu {escolha} e a máquina {maquina}, Papel ganha da Pedra, parabéns!")
elif escolha == maquina:
    print(f"Você escolheu {escolha} e a máquina {maquina}, vocês empataram!")

#MAQUINA GANHAR
if maquina == "PEDRA" and escolha == "TESOURA":
    print(f"A máquina escolheu {maquina} e você {escolha}, Pedra ganha da Tesoura, você perdeu!")
elif maquina == "TESOURA" and escolha == "PAPEL":
    print(f"A máquina escolheu {maquina} e você {escolha}, Tesoura ganha da Papel, você perdeu!")
elif maquina == "PAPEL" and escolha == "PEDRA":
    print(f"A máquina escolheu {maquina} e você {escolha}, Papel ganha da Pedra, você perdeu!")
elif maquina == escolha:
    print(f"A máquina escolheu {maquina} e você {escolha}, vocês empataram!")