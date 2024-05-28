#Conversão de temperatura

#Tratamento de erros
try: 
    while True :
        temp = float(input("Diga a temperatura atual: "))
        #Para o usuário escolher uma opção
        conversao = int(input("Converter a temperatura para\n1 - Celsius\n2 - Kelvin\n3 - Fahreheint :  "))

        temp = float(temp)

    #Conversão para celsius
        if conversao == 1:
            celsius = (temp + 273.15)
            print(f"A temperatura convertida para Kelvin ficaria de {celsius}°K")
    #Conversão para Kelvin
        elif conversao == 2:
            Kelvin = (temp - 273.15)
            print(f"A temperatura convertida para Celsius ficaria de {Kelvin}°C")
        elif conversao == 3:
            Fahreheint = (temp * 1.8 + 32)
            print(f"A temperatura convertida para Fahreheint ficaria de {Fahreheint}°F")
        elif conversao == 4:
            break
        else:
            print("Valor inserido inválido")

except ValueError:
    print("Valor inserido inválido")