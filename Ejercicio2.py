dias = int(input("Ingrese los días \n"))
diasdolar = [0]*dias

for i in range(0,dias):
     diasdolar[i] = int(input(f"Día {i+1} \n"))
    #  print("Día", i + 1)
    #  diasdolar[i] = float(input())
#Comparación
AlzaMayor = 0
for i in range(dias - 1):
    diferencia = diasdolar[i + 1] - diasdolar[i]
    if diferencia > AlzaMayor:
        AlzaMayor = diferencia
        print(f"El alza mayor es: {AlzaMayor}")
    elif diferencia < 0:
        print("No hubo alza")
