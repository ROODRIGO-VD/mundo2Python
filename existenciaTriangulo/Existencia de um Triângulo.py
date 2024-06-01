print(("=-"*15), "Analisador de Triângulos", ("=-"*15))
a = float(input("1° Segmento: "))
b = float(input("2° Segmento: "))
c = float(input("3° Segmento: "))

if a < b + c and b < a + c and c < a + b:
    print("Os segmentos PODEM formar um triângulo ", end="")
    if a == b == c:
        print("EQUILÁTERO!")
    elif a != b != c != a:
        print("ESCALENO!")
    else:
        print("ISÓSCELES!")
else:
    print("Os segmentos NÃO PODEM formar um triângulo!")
