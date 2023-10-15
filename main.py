import os.path
import funciones


def main():
    opc = 0
    while opc != 9:
        print('\nMenu de opciones:\n')
        print('1. Crear archivo binario de registros ')
        print('2. Cargar por teclado los datos de un ticket')
        print('3. Mostrar todos los datos de todos los registros del archivo binario')
        print('4. Mostrar todos los registros del archivo binario cuya patente sea igual a la patente ingresada')
        print('5. Buscar registro por ID')
        print('6. Determinar y mostrar la cantidad de vehículos de cada combinación posible entre tipo de vehículo y país de cabina')
        print('7. Mostrar cantidad de vehiculos por tipo de vehiculo y por pais de cabina')
        print('8. Mostrar el arreglo con todos los vehiculos que recorrieron mas de la distancia promedio')
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
                if os.path.exists("peajes-tp4.bin"):
                    funciones.mostrar_registros()
                else:
                    print("Error - No existe el archivo binario, porfavor ingrese 1 en el menu")

            elif opc_validada == 4:
                if os.path.exists("peajes-tp4.bin"):
                    funciones.patente()
                else:
                    print("Error - No existe el archivo binario, porfavor ingrese 1 en el menu")

            elif opc_validada == 5:
                if os.path.exists("peajes-tp4.bin"):
                    funciones.buscar_id()
                else:
                    print("Error - No existe el archivo binario, porfavor ingrese 1 en el menu")

            elif opc_validada == 6:
                if os.path.exists("peajes-tp4.bin"):
                    funciones.mostrar_combinacion(funciones.contar_combinacions())
                else:
                    print("Error - No existe el archivo binario, porfavor ingrese 1 en el menu")

            elif opc_validada == 7:
                if os.path.exists("peajes-tp4.bin"):
                    funciones.mostrar_opc7(funciones.contar_combinacions())
                else:
                    print("Error - No existe el archivo binario, porfavor ingrese 1 en el menu")

            elif opc_validada == 8:
                if os.path.exists("peajes-tp4.bin"):
                    distancia_promedio = funciones.calcular_distancia_promedio()
                    arreglo_vehiculos = funciones.vector_vehiculos_mayor_promedio(distancia_promedio)
                    funciones.shell_sort(arreglo_vehiculos)
                    funciones.mostrar_arreglo(arreglo_vehiculos)
                    print(f'La distancia promedio es de: {distancia_promedio} KM')
                else:
                    print("Error - No existe el archivo binario, porfavor ingrese 1 en el menu")

            elif opc_validada == 9:
                break


if __name__ == '__main__':
    main()
