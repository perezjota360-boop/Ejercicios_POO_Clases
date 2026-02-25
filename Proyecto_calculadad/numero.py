class Numero:
    def __init__(self, valor):
        self.__valor = valor

    def get_valor(self):
        return self.__valor

    def set_valor(self, nuevo_valor):
        self.__valor = nuevo_valor