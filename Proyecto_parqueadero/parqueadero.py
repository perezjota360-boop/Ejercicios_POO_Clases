from registro import Registro

class Parqueadero:
    def __init__(self):
        self.__registros = []

    def ingresar_vehiculo(self, usuario, vehiculo, puesto):
        registro = Registro(usuario, vehiculo, puesto)
        self.__registros.append(registro)
        print("Vehículo ingresado correctamente.")

    def retirar_vehiculo(self, placa):
        for registro in self.__registros:
            if registro.get_placa() == placa:
                registro.registrar_salida()
                print("Vehículo retirado correctamente.")
                return
        print("Vehículo no encontrado.")

    def mostrar_registros(self):
        print("\n=== REGISTROS ===")
        for r in self.__registros:
            r.mostrar()