from usuario import Usuario
from vehiculo import Vehiculo
from parqueadero import Parqueadero

def main():
    parqueadero = Parqueadero()

    while True:
        print("=== PARQUEADERO ===")
        print("1. Ingresar vehículo")
        print("2. Retirar vehículo")
        print("3. Ver registros")
        print("4. Salir")

        opcion = input("Seleccione: ")

        if opcion == "1":
            cedula = input("Cédula: ")
            nombre = input("Nombre: ")
            tipo_usuario = input("Tipo usuario Usuario: ")

            placa = input("Placa: ")
            tipo_carro = input("Tipo carro: ")
            color = input("Color: ")
            puesto = input("Puesto: ")

            usuario = Usuario(cedula, nombre, tipo_usuario)
            vehiculo = Vehiculo(placa, tipo_carro, color)

            parqueadero.ingresar_vehiculo(usuario, vehiculo, puesto)

        elif opcion == "2":
            placa = input("Placa del vehículo: ")
            parqueadero.retirar_vehiculo(placa)

        elif opcion == "3":
            parqueadero.mostrar_registros()

        elif opcion == "4":
            print("Saliendo...")
            break

        else:
            print("Opción inválida")


if __name__ == "__main__":
    main()