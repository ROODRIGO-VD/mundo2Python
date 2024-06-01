def um_quinhetos():
    s = 0
    for i in range(0, 500+1):
        if i % 3 == 0 and i % 2 != 0:
            s += i
    print(s)

def tabuada():
    n = int(input("Tabuada de: "))
    for i in range(0, 10+1):
        print(f"{n} x {i} = {i*n}")

s = 0
c = 0
for i in range(1, 7):
    num = int(input(f"{i}° valor: "))
    if num % 2 == 0:
        s += num
        c += 1

print(f"Você informou {c} números pares, e a soma deu {s}")