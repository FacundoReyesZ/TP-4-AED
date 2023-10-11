import os.path

import funciones


def main():
    opc = 0
    while opc != 9:
        print('\nMenu de opciones:\n')
        print('1. Crear archivo binario de registros ')
        print('2. ')
        print('3. ')
        print('4. ')
        print('5. ')
        print('6.  Determinar y mostrar la cantidad de vehículos de cada combinación posible entre tipo de vehículo y país de cabina')
        print('7. ')
        print('8. ')
        print('9. Salir')

        opc = input('\nIngrese su eleccion: \n')
        opc_validada = funciones.validar_opc(opc)
        if opc_validada is not None:
            if opc_validada == 1:
                if os.path.exists("peajes-tp4.bin"):
                    print("El archivo 'archivo.bin' ya existe. ¿Desea eliminarlo? (s/n): ")
                    respuesta = input()
                    if respuesta.lower() == "s":
                        print("El archivo binario ha sido eliminado y luego creado desde 0")
                        os.remove("peajes-tp4.bin")
                        funciones.crear_archivo_binario()
                    else:
                        print("La operación ha sido cancelada.")
                else:
                    funciones.crear_archivo_binario()
                    print('El archivo binario ha sido creado con exito...')

            elif opc_validada == 2:
                funciones.cargar_ticket()

            elif opc_validada == 3:
                funciones.mostrar_registros()

            elif opc_validada == 6:
                funciones.mostrar_combinacion(funciones.contar_combinacions())


if __name__ == '__main__':
    main()
