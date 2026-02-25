class Vehiculo:
    def __init__(self, placa, tipo, color):
        self.__placa = placa
        self.__tipo = tipo
        self.__color = color

    def get_placa(self):
        return self.__placa

    def get_tipo(self):
        return self.__tipo

    def get_color(self):
        return self.__color