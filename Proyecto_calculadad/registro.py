from datetime import datetime

class Registro:
    def __init__(self, usuario, num1, num2, tipo, resultado):
        self.__usuario = usuario
        self.__num1 = num1
        self.__num2 = num2
        self.__tipo = tipo
        self.__resultado = resultado
        self.__fecha = datetime.now().strftime("%Y-%m-%d")

    def mostrar(self):
        print(
            f"{self.__usuario.get_cedula()} | "
            f"{self.__usuario.get_nombre()} | "
            f"{self.__num1.get_valor()} | "
            f"{self.__num2.get_valor()} | "
            f"{self.__tipo} | {self.__resultado} | "
            f"{self.__fecha}"
        )