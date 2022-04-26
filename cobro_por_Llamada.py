




# input

X=int(input("Ingresa los minutos que duro la llamada:"))

# prossesing

if (X <= 3):
    msj = "el valor es de 3000"
else:
    msj = 300+(50 * (X - 3))

# output
print("El costo total es:" + str(msj))