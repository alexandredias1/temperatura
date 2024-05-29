#Conversão de temperatura

#Tratamento de erros
try: 
    while True :
        temp = float(input("Diga a temperatura atual: "))
        #Para o usuário escolher uma opção
        conversao = int(input("Converter a temperatura para\n1 - Celsius\n2 - Kelvin\n3 - Fahreheint\n4 - Celsius_para_Fahreheint\n5 - Kelvin_para_Fahreheint\n6 - Fahreheint_para_Kelvin\n7 - Sair: "))

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
            print(f"A temperatura convertida para Celsius ficaria de {Fahreheint}°C")
        elif conversao == 4:
            celsius = (temp - 32 / 1.8)
            print(f"A temperatura convertida para Fahreheint ficaria de {celsius}°F")
        elif conversao == 5:
            Kelvin = (temp - 273.15) * 1.8 + 32
            print(f"A temperatura convertida para Fahreheint ficaria de {Kelvin}°F") 
        elif conversao == 6:
            Fahreheint = (temp - 32) / 1.8 + 273.15
            print(f"A temperatura convertida para kelvin ficaria de {Fahreheint}°K") 

        elif conversao == 7:
            break
        else:
            print("Numero inserido inválido")

except ValueError:
    print("Valor inserido inválido")