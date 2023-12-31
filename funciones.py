import os.path
import pickle


class Ticket:
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
        vehiculo = Ticket(identificador, patente, tipo_vehiculo, forma_de_pago, pais_cabina, distancia)
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
    paises = ['Argentina', 'Brasil', 'Bolivia', 'Paraguay', 'Uruguay', 'Chile', 'Otro']

    while n.tell() < t:
        vehic = pickle.load(n)

        if patente_chi(vehic.patente):
            indice = 5
        elif patente_arg(vehic.patente):
            indice = 0
        elif patente_bol(vehic.patente):
            indice = 2
        elif patente_brz(vehic.patente):
            indice = 1
        elif patente_par(vehic.patente):
            indice = 3
        elif patente_uru(vehic.patente):
            indice = 4
        else:
            indice = 6

        print(f'{vehic} | {paises[indice]}')


def es_numero(i):
    if i in "0123456789":
        return True


def cargar_ticket():
    correcto = False
    while not correcto:
        inteable = True
        identificador = input("Codigo identificador: ")
        for i in identificador:  # revisamos si se puede transformar a int
            if not es_numero(i):
                inteable = False
        if inteable:  # de ser transformable ahora preguntar si es mayor a 0
            identificador = int(identificador)
            if identificador > 0:
                correcto = True
            else:
                print("ERROR - Codigo invalido [error 2] / Intente denuevo")
        else:
            print("ERROR - Codigo invalido [error 1] / Intente denuevo")

    patente = input("Patente: ")

    correcto = False
    while not correcto:
        tipo_vehiculo = input("Tipo de vehiculo (entre 0 y 2): ")
        if tipo_vehiculo in ["0", "1", "2"]:  # simplemente si no es 0 1 o 2 no es valido
            tipo_vehiculo = int(tipo_vehiculo)
            correcto = True
        else:
            print("ERROR - Digito invalido / Intente denuevo")

    correcto = False
    while not correcto:
        forma_de_pago = input("Forma de pago (entre 1 y 2): ")
        if forma_de_pago in ["1", "2"]:  # lo mismo que el anterior
            forma_de_pago = int(forma_de_pago)
            correcto = True
        else:
            print("ERROR - Digito invalido / Intente denuevo")

    correcto = False
    while not correcto:
        pais_cabina = input("Pais de Cabina (entre 0 y 4): ")
        if pais_cabina in ["0", "1", "2", "3", "4"]:  # "" "" "" "" x2
            pais_cabina = int(pais_cabina)
            correcto = True
        else:
            print("ERROR - Digito invalido / Intente denuevo")

    correcto = False
    while not correcto:
        inteable = True
        distancia = input("Distancia (KM desde cabina): ")
        for i in distancia:  # el mismo proceso del primero excepto que no pregunta si es mayor a 0
            if not es_numero(i):
                inteable = False
        if inteable:
            distancia = int(distancia)
            correcto = True
        else:
            print("ERROR - Numero invalido {str} / Intente denuevo")

    m1 = open("peajes-tp4.bin", "ab")
    v = Ticket(identificador, patente, tipo_vehiculo, forma_de_pago, pais_cabina, distancia)
    pickle.dump(v, m1)
    m1.close()


def patente():
    x = input("ingrese la patente a buscar:  ")
    fb = "peajes-tp4.bin"
    n = open(fb, "rb")
    t = os.path.getsize(fb)
    cont_total = 0

    while n.tell() < t:
        pat = pickle.load(n)
        if pat.patente == x.upper():
            cont_total += 1
            print(f'{pat}')
    print(f'\nCantidad de registros con la patente ||{x}||: {cont_total}')


def buscar_id():
    identif = input("Ingrese el codigo numerico a buscar: ")
    coincide = False
    fb = "peajes-tp4.bin"
    n = open(fb, "rb")
    t = os.path.getsize(fb)
    paises = ['Argentina', 'Brasil', 'Bolivia', 'Paraguay', 'Uruguay', 'Chile', 'Otro']

    while n.tell() < t:
        vehic = pickle.load(n)
        if vehic.identificador == identif:
            print("Codigo encontrado: \n")
            if patente_chi(vehic.patente):
                indice = 5
            elif patente_arg(vehic.patente):
                indice = 0
            elif patente_bol(vehic.patente):
                indice = 2
            elif patente_brz(vehic.patente):
                indice = 1
            elif patente_par(vehic.patente):
                indice = 3
            elif patente_uru(vehic.patente):
                indice = 4
            else:
                indice = 6

            print(f'{vehic} | {paises[indice]}')
            coincide = True
            break
    if not coincide:
        print("No se encontro un registro con el codigo introducido")


def contar_combinaciones():
    fb = "peajes-tp4.bin"
    n = open(fb, "rb")
    t = os.path.getsize(fb)

    combinaciones = [[0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0]]
    while n.tell() < t:
        vehic = pickle.load(n)
        tipo_vehiculo = vehic.tipo_vehiculo
        pais_cabina = vehic.pais_cabina
        combinaciones[int(tipo_vehiculo)][int(pais_cabina)] += 1
    n.close()
    return combinaciones


def mostrar_combinacion(arr):
    tipos_vehiculo = ['MOTOCICLETA', 'AUTOMÓVIL', 'CAMIÓN']
    paises_cabinas = ['Argentina', 'Bolivia', 'Brasil', 'Paraguay', 'Uruguay']
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] > 0:
                print(
                    f'La cantidad de vehiculos del tipo --{tipos_vehiculo[i]}-- de la cabina del pais --{paises_cabinas[j]}-- fue de {arr[i][j]} ')


def mostrar_opc7(arr):
    tipos_vehiculo = ['MOTOCICLETA', 'AUTOMÓVIL', 'CAMIÓN']
    paises_cabinas = ['Argentina', 'Bolivia', 'Brasil', 'Paraguay', 'Uruguay']
    total_vehiculo = 0
    total_pais = 0
    filas = len(arr)
    columnas = len(arr[0])

    for c in range(columnas):
        for f in range(filas):
            total_pais += arr[f][c]
        print(f"La cantidad de vehiculos que pasaron por la cabina del pais {paises_cabinas[c]} fue de: {total_pais}")
        total_pais = 0

    for f in range(filas):
        for c in range(columnas):
            total_vehiculo += arr[f][c]
        print(
            f"La cantidad de vehiculos del tipo {tipos_vehiculo[f]} que pasaron por alguna cabina fue de: {total_vehiculo}")
        total_vehiculo = 0


def calcular_distancia_promedio():
    fb = "peajes-tp4.bin"
    n = open(fb, "rb")
    t = os.path.getsize(fb)
    cant_vehiculos = 0
    distancia_total = 0
    while n.tell() < t:
        vehic = pickle.load(n)
        cant_vehiculos += 1
        distancia_total += int(vehic.distancia)

    distancia_promedio = distancia_total / cant_vehiculos

    return round(distancia_promedio, 2)


def vector_vehiculos_mayor_promedio(promedio):
    fb = "peajes-tp4.bin"
    n = open(fb, "rb")
    t = os.path.getsize(fb)
    arr = []
    while n.tell() < t:
        vehic = pickle.load(n)
        if int(vehic.distancia) > promedio:
            arr.append(vehic)

    return arr


def shell_sort(arr):
    n = len(arr)
    h = 1
    while h <= n // 9:
        h = 3 * h + 1
    while h > 0:
        for j in range(h, n):
            y = arr[j].distancia
            k = j - h
            while k >= 0 and y < arr[k].distancia:
                arr[k + h].distancia = arr[k].distancia
                k -= h
            arr[k + h].distancia = y
        h //= 3


def mostrar_arreglo(arr):
    for vehiculo in arr:
        print(vehiculo)
