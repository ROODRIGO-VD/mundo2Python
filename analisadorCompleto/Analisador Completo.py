somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ""
for p in range(1, 5):
    print(f"----- {p}° PESSOA -----")
    nome = input("Nome:").strip()
    idade = int(input("Idade: "))
    sexo = input("Sexo [M/F]: ").strip()
    somaidade += idade
    if p == 1 and sexo in "Mn":
        maioridadehomem = idade
        nomevelho = nome
    if
mediaidade = somaidade / 4
print(f"A média de idade desse grupo é de {mediaidade} anos.")


