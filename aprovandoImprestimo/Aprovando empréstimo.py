v_casa = float(input("Qual o valor da casa: R$"))
v_salario = float(input("Qual o seu salário: R$"))
anos = int(input("Por quantos anos você pagará pela casa: "))
prestacao = v_casa / (anos * 12)


if prestacao <= 0.3 * v_salario:
    print(f"Você deseja comprar uma casa no valor de R${v_casa:.2f}, com um salário de R${v_salario:.2f}, em {anos} anos."
          f" Realizando alguns calculos a prestação ficou em {prestacao}.Determinou-se a APROVAÇÃO do seu caso.")
else:
    print(f"Você deseja comprar uma casa no valor de R${v_casa:.2f}, com um salário de R${v_salario:.2f}, em {anos} anos."
          f" Realizando alguns calculos a prestação ficou em R${prestacao:.2f}.Determinou-se a NEGAÇÃO do seu caso.")
