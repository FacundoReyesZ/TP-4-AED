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


def validar_opc(opcion):
    numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    if opcion in numeros:
        opcion = int(opcion)
        return opcion
    else:
        return None


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


def patente_arg(pat):
    if len(pat) < 7:
        return False

    if pat[:2].isalpha() and pat[2:5].isdigit() and pat[5:].isalpha():
        return True
    return False


def patente_brz(pat):
    if len(pat) < 7:
        return False

    if pat[:3].isalpha() and pat[3].isdigit() and pat[4].isalpha() and pat[5:].isdigit():
        return True
    return False


def patente_bol(pat):
    if len(pat) < 7:
        return False

    if pat[:2].isalpha() and pat[2:].isdigit():
        return True
    return False


def patente_par(pat):
    if len(pat) < 7:
        return False

    if pat[:4].isalpha() and pat[4:].isdigit():
        return True
    return False


def patente_uru(pat):
    if len(pat) < 7:
        return False

    if pat[:3].isalpha() and pat[3:].isdigit():
        return True
    return False


def patente_chi(pat):
    if pat[0].isspace():
        pat = pat[1:]
        if len(pat) < 6:
            return False

        if pat[:4].isalpha() and pat[4:].isdigit():
            return True
        return False


def mostrar_registros():
    fb = "peajes-tp4.bin"
    n = open(fb, "rb")
    t = os.path.getsize(fb)

    while n.tell() < t:
        vehic = pickle.load(n)

        if patente_chi(vehic.patente):
            pais = "Chile"
        elif patente_arg(vehic.patente):
            pais = "Argentina"
        elif patente_bol(vehic.patente):
            pais = "Bolivia"
        elif patente_brz(vehic.patente):
            pais = "Brasil"
        elif patente_par(vehic.patente):
            pais = "Paraguay"
        elif patente_uru(vehic.patente):
            pais = "Uruguay"
        else:
            pais = "Otro"

        print(f'{vehic} | {pais}')
