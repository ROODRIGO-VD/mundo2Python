nota1 = float(input("Qual foi sua 1° nota: "))
nota2 = float(input("Qual foi sua 2° nota: "))

media = nota1 + nota2 // 2

if media < 5:
    print("Você foi reprovado!")
elif 5 < media < 6.9:
    print("Você está de recuperação!")
elif media >= 7:
    print("Você está aprovado!")