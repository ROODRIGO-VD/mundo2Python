from datetime import date
totmaior = 0
totmenor = 0
for grupo in range(1, 8):
    ano = int(input(f"Em que ano a {grupo}ª pessoa nasceu? "))
    idade = date.today().year - ano
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print(f"No total tivemos {totmaior} pessoas MAIORES de idade")
print(f"No total tivemos {totmenor} pessoas MENORES de idade")




