Temperatura = float(input("Digite a temperatura atual em Celsius: "))

if Temperatura <=10:
   print("O clima está frio, se agasalhe")

elif Temperatura <=20:
   print("O clima está agradável, leve um casaco fino")

elif Temperatura <=30:
   print("O clima está quente, se hidrate")

else:
   print("O clima está muito quente, se hidrate bastante")


while True:
    entrada = input("Digite a temperatura atual em Celsius (ou 'sair' para encerrar): ")
    
    if entrada.lower() == "sair":
        print("Encerrando o programa...")
        break
    
    try:
        temp = float(entrada)
        # Detectar escala
        if temp > 100:  
            print("Parece Kelvin. Convertendo para Celsius...")
            temperatura = temp - 273.15
        elif temp > 45:  
            print("Parece Fahrenheit. Convertendo para Celsius...")
            temperatura = (temp - 32) * 5/9
        else:  
            temperatura = temp
    
        if temperatura <= 10:
            print("O clima está frio, se agasalhe.")
        elif temperatura <= 20:
            print("O clima está agradável, leve um casaco fino.")
        elif temperatura <= 30:
            print("O clima está quente, se hidrate.")
        else:
            print("O clima está muito quente, se hidrate bastante.")
            
    except ValueError:
        print("Por favor, digite um número válido ou 'sair'.")

