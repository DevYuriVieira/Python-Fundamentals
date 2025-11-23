nome = (input("Digite seu nome: "))
concessionaria = (input("Digite o nome da concessionária: "))
idade = int(input("Digite sua idade: "))


if idade >= 18:
    print(F"{nome},Está convidado(a) para vir conhecer os veículos da {concessionaria} e fazer um test-drive!")

else:
    print(F"{nome},Infelizmente não possui idade para conhecer os veículos da {concessionaria}!")
