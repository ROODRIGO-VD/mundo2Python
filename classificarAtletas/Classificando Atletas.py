from datetime import date
ano = int(input("Em que ano você nasceu: "))
idade = date.today().year - ano
if idade <= 9:
    print(f"Você possui {idade}, logo está na categoria MIRIM")
elif idade <=14:
    print(f"Você possui {idade}, logo está na categoria INFANTIL")
elif idade <= 19:
    print(f"Você possui {idade}, logo está na categoria JUNIOR")
elif idade <=20:
    print(f"Você possui {idade}, logo está na categoria SÊNIOR")
else:
    print(f"Você possui {idade}, logo está na categoria MASTER")