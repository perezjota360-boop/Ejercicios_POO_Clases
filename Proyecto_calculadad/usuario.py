class Usuario:
    def __init__(self, cedula, nombre):
        self.__cedula = cedula
        self.__nombre = nombre

    def get_cedula(self):
        return self.__cedula

    def get_nombre(self):
        return self.__nombre