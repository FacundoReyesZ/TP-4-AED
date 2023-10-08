import io
import os.path
import pickle


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


def crear_archivo_binario():
    m = open("peajes-tp4.csv", 'rt')
    n = open("peajes-tp4.bin", "wb")
    lineas = m.readlines()
    for linea in lineas[2:]:
        datos = linea.split(",")
        identificador = datos[0]
        patente = datos[1]
        tipo_vehiculo = datos[2]
        forma_de_pago = datos[3]
        pais_cabina = datos[4]
        distancia = datos[5]
        if distancia[-1] == "\n":
            distancia = distancia[:-1]
        vehiculo = Vehiculo(identificador, patente, tipo_vehiculo, forma_de_pago, pais_cabina, distancia)
        pickle.dump(vehiculo, n)
    n.close()
    m.close()


def validar_opc(opcion):
    numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    if opcion in numeros:
        opcion = int(opcion)
        return opcion
    else:
        return None
