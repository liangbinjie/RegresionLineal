def main():
    opcion = input("Selecciona que desea hacer:" +
                   "\n1. Calcular Recta Regresion Lineal Simple" +
                   "\nx. Salir"
                   "\n> ")
    if opcion == "1":
        array_x = input("Ingrese los valores de X separados por comas: ")
        array_y = input("Ingrese los valores de Y separados por comas: ")
        array_x = [float(i) for i in array_x.split(",")]
        array_y = [float(i) for i in array_y.split(",")]
        if len(array_x) != len(array_y):
            print("Error: Los arreglos deben tener la misma longitud.")
            return
        n = len(array_x)
        sum_x = sum(array_x)
        sum_y = sum(array_y)
        sum_xy = sum(x * y for x, y in zip(array_x, array_y))
        sum_x2 = sum(x ** 2 for x in array_x)
        sum_y2 = sum(y ** 2 for y in array_y)
        b = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
        a = (sum_y - b * sum_x) / n
        print("Resultados:")
        print("∑x:", sum_x)
        print("∑y:", sum_y)
        print("∑xy:", sum_xy)
        print("∑x^2:", sum_x2)
        print("∑y^2:", sum_y2)
        print(f"La ecuacion de la recta de regresion es: y = {a} + {b}x")
    elif opcion.lower() == "x":
        print("Saliendo del programa.")
        return
    else:
        print("Opcion no valida. Intente de nuevo.")
        main()

if __name__ == "__main__":
    main()