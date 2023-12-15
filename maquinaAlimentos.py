def costo(precio):
    bandera = True
    auxiliar = 0

    while bandera:
        bande = False
        while not bande:
            moneda = int(input("Ingrese las monedas: "))
            if moneda == 10 or moneda == 50 or moneda == 100:
                bande = True
            else:
                print("Ingrese una moneda que sea válida")

        auxiliar += moneda
        if auxiliar >= precio:
            bandera = False

    return auxiliar

def cambio(precioTotal, precio):
    vueltos = precioTotal - precio
    aux = vueltos / 50

    if int(aux) == 0:
        aux = vueltos / 10
        if int(aux) != 0:
            print("Cambio:", int(aux), "monedas de 10")
        else:
            print("Completo")
    else:
        cM = int(aux)
        vueltos -= 50
        aux = vueltos / 10
        if int(aux) != 0:
            print("Su cambio es:", cM, "de 50 y", int(aux), "de 10")
        else:
            print("No hay más cambio")

comida = [0, 270, 340, 390]
print("¿Qué producto desea?")
for i in range(1, 4):
    print(i, ". Producto:", i, comida[i])
producto = int(input())



precioTotal = costo(comida[producto])
cambio(precioTotal, comida[producto])