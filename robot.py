from direcciones import Direcciones


def moverse(movi):
    x, y = 0, 0
    direccion = Direcciones.POSITIVEY

    for pasos in movi:
        if direccion == Direcciones.POSITIVEY:
            y += pasos
        elif direccion == Direcciones.NEGATIVEX:
            x -= pasos
        elif direccion == Direcciones.NEGATIVEY:
            y -= pasos
        elif direccion == Direcciones.POSITIVEX:
            x += pasos

        direccion = direccion.turn()

    return print(f"El robot se encuentra en la posición: {x} {y}")


moverse([10, 5, -2])
moverse([-10, 3, -10])
moverse([-5, 4, -9])
moverse([-15, 10, -5])
moverse([-30, 8, -7])
