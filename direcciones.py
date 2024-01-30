from enum import Enum


class Direcciones(Enum):
    POSITIVEY = 1
    NEGATIVEX = 2
    NEGATIVEY = 3
    POSITIVEX = 4

    def turn(self):
        if self == Direcciones.POSITIVEY:
            return Direcciones.NEGATIVEX
        elif self == Direcciones.NEGATIVEX:
            return Direcciones.NEGATIVEY
        elif self == Direcciones.NEGATIVEY:
            return Direcciones.POSITIVEX
        elif self == Direcciones.POSITIVEX:
            return Direcciones.POSITIVEY
