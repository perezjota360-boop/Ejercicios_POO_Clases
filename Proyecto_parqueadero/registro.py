from datetime import datetime

class Registro:
    def __init__(self, usuario, vehiculo, puesto):
        self.__usuario = usuario
        self.__vehiculo = vehiculo
        self.__puesto = puesto
        self.__fecha = datetime.now().strftime("%Y-%m-%d")
        self.__hora_entrada = datetime.now().strftime("%H:%M")
        self.__hora_salida = None
        self.__estado = "Entrada"

    def registrar_salida(self):
        self.__hora_salida = datetime.now().strftime("%H:%M")
        self.__estado = "Salida"

    def get_placa(self):
        return self.__vehiculo.get_placa()

    def mostrar(self):
        print(
            f"{self.__usuario.get_nombre()} | "
            f"{self.__usuario.get_tipo_usuario()} | "
            f"{self.__vehiculo.get_placa()} | "
            f"{self.__usuario.get_cedula()} | "
            f"{self.__vehiculo.get_tipo()} | "
            f"{self.__vehiculo.get_color()} | "
            f"{self.__puesto} | "
            f"{self.__fecha} | "
            f"{self.__hora_entrada} | "
            f"{self.__hora_salida if self.__hora_salida else '---'} | "
            f"{self.__estado}"
        )