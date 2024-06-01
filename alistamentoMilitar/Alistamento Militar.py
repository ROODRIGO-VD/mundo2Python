from datetime import date
ano = int(input("Em que ano você nasceu? "))
idade = date.today().year - ano
if idade < 18:
    print(f"Você possui {idade} anos, portando falta {18 - idade} anos para seu Alistamento Militar.")
elif idade > 18:
    print(f"Você possui {idade} anos, portando já passou {idade - 18} anos do seu Alistamento Militar, procure uma junta Militar.")
elif idade == 18:
    print(f"Você possui {idade} anos, portando deve se apresentar a uma junta Militar.")

