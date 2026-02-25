from usuario import Usuario
from numero import Numero
from operacion import Operacion
from registro import Registro

def main():
    print("____ CALCULADORA POO ____")

    cedula = input("Ingrese cédula: ")
    nombre = input("Ingrese nombre: ")

    usuario = Usuario(cedula, nombre)

    valor1 = float(input("Número 1: "))
    valor2 = float(input("Número 2: "))

    num1 = Numero(valor1)
    num2 = Numero(valor2)

    op = Operacion(num1, num2)

    print(" _____Seleccione operación:____")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    opcion = input("Opción: ")

    if opcion == "1":
        resultado = op.sumar()
        tipo = "Suma"
    elif opcion == "2":
        resultado = op.restar()
        tipo = "Resta"
    elif opcion == "3":
        resultado = op.multiplicar()
        tipo = "Multiplicación"
    elif opcion == "4":
        resultado = op.dividir()
        tipo = "División"
    else:
        print("Opción inválida")
        return

    registro = Registro(usuario, num1, num2, tipo, resultado)

    print("___ RESULTADO ____")
    registro.mostrar()


if __name__ == "__main__":
    main()