altura = float(input("Qual sua altura em M: "))
peso = float(input("Qual seu peso em KG: "))

imc = peso // (altura ** 2)

if imc <= 18.5:
    print(f"Seu IMC é {imc}, logo você está ABAIXO DO PESO recomendado.")
elif 18.5 < imc < 25:
    print(f"Seu IMC é {imc}, logo você está no PESO IDEAL")
elif 25 < imc < 30:
    print(f"Seu IMC é {imc}, logo você está em SOBREPESO")
elif 30 < imc < 40:
    print(f"Seu IMC é {imc}, logo você está OBESO")
else:
    print(f"Seu IMC é {imc}, logo você está em OBESIDADE MÓRBIDA")