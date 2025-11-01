import random 

for i in range(3):
    escolha_do_usuario_num = int(input("Escolha uma opção: 1-Pedra, 2-Papel, 3-Tesoura, 4-sair: \n"))
    escolha_do_usuario = ""

    if escolha_do_usuario_num == 1:
        escolha_do_usuario ="Pedra"

    elif escolha_do_usuario_num == 2:
        escolha_do_usuario ="Papel"

    elif escolha_do_usuario_num == 3:
        escolha_do_usuario ="Tesoura"
    elif escolha_do_usuario_num == 4:
        break
   
    else:
        print("Escolha uma opção válida: ")


    escolha_do_computador = random.choice(["Pedra", "Papel", "Tesoura"])
    print("A escolha do computador é: ",escolha_do_computador)

    if escolha_do_usuario == escolha_do_computador:
        print("Empate")

    elif escolha_do_usuario == "Papel" and escolha_do_computador == "Pedra" or escolha_do_usuario == "Tesoura" and escolha_do_computador == "Papel" or escolha_do_usuario == "Pedra" and escolha_do_computador == "Tesoura":
        print("Vitória")

    else:
        print("Derrota")
    




