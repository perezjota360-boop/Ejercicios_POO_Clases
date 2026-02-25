class Operacion:
    def __init__(self, num1, num2):
        self.__num1 = num1  # objeto Numero
        self.__num2 = num2  # objeto Numero

    def sumar(self):
        return self.__num1.get_valor() + self.__num2.get_valor()

    def restar(self):
        return self.__num1.get_valor() - self.__num2.get_valor()

    def multiplicar(self):
        return self.__num1.get_valor() * self.__num2.get_valor()

    def dividir(self):
        if self.__num2.get_valor() == 0:
            return "Error: División por 0"
        return self.__num1.get_valor() / self.__num2.get_valor()