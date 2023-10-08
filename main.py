import funciones


def main():
    opc = 0
    while opc != 9:
        print('\nMenu de opciones:\n')
        print('1. ')
        print('2. ')
        print('3. ')
        print('4. ')
        print('5. ')
        print('6. ')
        print('7. ')
        print('8. ')
        print('9. Salir')

        opc = input('\nIngrese su eleccion: \n')
        opc_validada = funciones.validar_opc(opc)
        if opc_validada is not None:
            if opc_validada == 1:
                funciones.crear_archivo_binario()


if __name__ == '__main__':
    main()
