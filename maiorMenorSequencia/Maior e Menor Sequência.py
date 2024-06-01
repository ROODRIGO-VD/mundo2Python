
pesomaior = 0
pesomenor = 0
for pessoa in range(1, 6):
    peso = float(input(f"Peso da {pessoa}ª pessoa do grupo? "))
    if peso > pesomaior:
        pesomaior = peso
    if pesomenor == 0 or pesomenor > peso:
        pesomenor = peso


print(f"O maior peso foi o {pesomaior}")
print(f"O menor peso foi o {pesomenor}")


