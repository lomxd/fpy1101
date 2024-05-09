import os

import time

limpieza_pantalla = "cls"
# tienda de sushi ( con solo 4 tipos)
def calcular_descuento(total, codigo):
    if codigo == "soyotaku":
        descuento = total * 0.1
        total -= descuento
        return total, True
    else:
        return total, False
#a qui damos las opciones dadas para el cliente
def mostrar_menu():
    print("Bienvenido al sistema pedido de sushi:")
    print("1. Pikachu Roll - $4500")
    print("2. Otaku Roll - $5000")
    print("3. Pulpo Venenoso Roll - $5200")
    print("4. Anguila Eléctrica Roll - $4800")
    print("X. Finalizar pedido")
# definir el menu
def main():
    menu ={ 
        1: ("Pikachu Roll", 4500),
        2: ("Otaku Roll", 5000),
        3: ("Pulpo Venenoso Roll", 5200),
        4: ("Anguila Eléctrica Roll", 4800)
    }

    pedido = []
    total_pedido = 0

    while True:
        mostrar_menu()
        opcion = input("Seleccione un roll (1-4) o X para finalizar el pedido: ")

        if opcion.upper() == "X":
            break

        try:
            opcion = int(opcion)
            if opcion not in menu:
                print("Opción no válida. Por favor, seleccione una opción válida.")
                continue

            roll = menu[opcion]
            pedido.append(roll)
            total_pedido += roll[1]
            print(f"Se agregó {roll[0]} al pedido.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número válido.")

    print("Pedido completo.")
    codigo_descuento = input("¿Tiene un código de descuento? Ingréselo o X para salir: ")

    if codigo_descuento == "X":
        print("Gracias por su pedido.")
    else:
        total_pedido, descuento_aplicado = calcular_descuento(total_pedido, codigo_descuento)
        if descuento_aplicado:
            print("Descuento aplicado correctamente.")
        else:
            while codigo_descuento != "X":
                print("Código no válido.")
                codigo_descuento = input("Ingrese un código válido o X para salir: ")
                if codigo_descuento == "soyotaku":
                    total_pedido, descuento_aplicado = calcular_descuento(total_pedido, codigo_descuento)
                    if descuento_aplicado:
                        print("Descuento aplicado correctamente.")
                        break
        print("Detalle del pedido:")
        for roll, precio in pedido:
            print(f"- {roll}: ${precio}")
        print(f"Total a pagar: ${total_pedido}")

if __name__ == "__main__":
    main()
#ocupe informacion de mis apuntes, escrbir mucho me marea, y "aprendi"a ocupar def, for, return, main y {}, ayuda a ahorrarse hartas lineas de algoritmo