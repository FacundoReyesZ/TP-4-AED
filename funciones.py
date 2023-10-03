class Vehiculo:
    def __init__(self, identificador, patente, tipo_vehiculo, forma_de_pago, pais_cabina, distancia):
        self.identificador = identificador
        self.patente = patente
        self.tipo_vehiculo = tipo_vehiculo
        self.forma_de_pago = forma_de_pago
        self.pais_cabina = pais_cabina
        self.distancia = distancia

    def __str__(self):
        return 'Codigo: ' + str(self.identificador) \
            + ' | Patente: ' + self.patente \
            + ' | Vehiculo tipo: ' + str(self.tipo_vehiculo) \
            + ' | Forma de pago: ' + str(self.forma_de_pago) \
            + ' | Pais de cabina: ' + str(self.pais_cabina) \
            + ' | Distancia: ' + str(self.distancia)


def crear_archivo_binario(file):
    m = open(file, 'rt')
    m.readline()
    cont = 0
    for linea in m:
        cont += 1
        if cont < 10:
            print(linea)
        else:
            break



def validar_opc(opcion):
    numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    if opcion in numeros:
        opcion = int(opcion)
        return opcion
    else:
        return None