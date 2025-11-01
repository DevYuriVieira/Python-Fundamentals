nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
nota3 = float(input("Digite sua terceira nota: "))

media_final = (nota1 + nota2 + nota3) / 3

if media_final>=7:
    print("Aprovado")
elif media_final>=5:
    print("Em recuperação")
else:
    print("Reprovado")


