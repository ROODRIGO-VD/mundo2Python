print("=" * 23)
print("10 TERMOS DE UMA PA")
print("=" * 23)
primeiro = int(input("Primeiro termo: "))
raz = int(input("Razão: "))
decimo = primeiro + (10 - 1) * raz
for c in range(primeiro, decimo + raz, raz):
    print(c, end="→ ")
print("ACABOU")
