# Reto: Manejo de archivos
# Crea un programa que te permita realizar un registro mensual de gastos en un archivo .txt 
# es decir, registrar, mostrar y calcular gastos. 
# El programa deberá ser capaz de leer y escribir en un archivo para almacenar la información. 🧠


import random
import string
from datetime import date

gastos_2024= []

# CONSTANTES:
MESES_VALIDOS = range(1, 13)  # Los meses válidos son del 1 al 12
MESES = ["ENERO", "FEBRERO", "MARZO", "ABRIL", "MAYO", "JUNIO",
         "JULIO", "AGOSTO", "SEPTIEMBRE", "OCTUBRE", "NOVIEMBRE", "DICIEMBRE"]
AÑO_ACTUAL = str(date.today().year)  # se transforma a string para evitar errores

# FUNCIONES:
def generarArchivoDeGastos(archivoNombre:str="Gastos", encabezado:str=AÑO_ACTUAL):
    """Esta función recibe un encabezado opcional y un nombre de archivo opcional"""
    with open(f"{archivoNombre}.txt", "w") as archivo:
        archivo.write(encabezado)

def generar_id_random(longitud=5):
    """Esta función genera un id random con una longitud especificada"""
    caracteres = string.ascii_letters + string.digits
    return ''.join(random.choice(caracteres) for _ in range(longitud))

def registrarGasto(registro:list, gasto:float, actividad:str, mes:int):
    """Esta función permite registrar un gasto individual"""
    if not (gasto and actividad and mes):
        return None
    if mes in MESES_VALIDOS:
        id = generar_id_random()
        registro.append((id, {"gasto": gasto, "actividad": actividad, "mes": mes}))  # crea un registro con una tupla(id, detalles del gasto)
        return registro  # retorna el registro y el id para su uso en la función formatearGasto()
    else:
        return f" -{mes}- no es un número de mes válido"

def formatearGastos(gastos):
    """Esta función da un formato ordenado a todos los gastos registrados para cargarlo en un archivo.txt"""
    gastosTotales= 0
    gastos_por_mes = {}
    for tupla in gastos:
        mes = tupla[1]["mes"]
        if mes not in gastos_por_mes:
            gastos_por_mes[mes] = []
        gastos_por_mes[mes].append(tupla)

    resultado = ""
    for mes in sorted(gastos_por_mes):
        resultado += f"{MESES[mes-1]}\n"
        for gasto in gastos_por_mes[mes]:
            resultado += f"   - {gasto[1]['actividad']} --> ${gasto[1]['gasto']}\n"
        resultado += "\n"
        resultado += f"Gastos del mes: ${calcularTotalDelMes(gastos,mes)}\n \n"
        gastosTotales+=calcularTotalDelMes(gastos,mes)
    resultado+= f"GASTOS DEL AÑO {gastosTotales}"

    return resultado

def agregarGasto(nuevoGasto:str, archivoNombre:str="Gastos"):
    """Esta función agrega un dato previamente formateado al final de algún archivo.txt"""
    with open(f"{archivoNombre}.txt", "a") as archivo:
        archivo.write(nuevoGasto)

def calcularTotalDelMes(gastos:list, mes:int):
    """Esta función permite calcular el total gastado en un mes."""
    total = 0
    for gasto in gastos:
        if gasto[1]["mes"] == mes:
            total += gasto[1]["gasto"]
    return total

#* ZONA DE PRUEBAS:

encabezado = f"-||-||--|-||-|-||-|-|-|--||{AÑO_ACTUAL}||--|-|-|-||-|-||-|--||-||- \n\n\n"
nombreArchivo = "archivo de gastos"
generarArchivoDeGastos(nombreArchivo, encabezado)  # successful ✅

# Agregar registros de gastos
nuevoGasto = registrarGasto(gastos_2024, 156, "yoga", 12)  # successful ✅
nuevoGasto = registrarGasto(gastos_2024, 456, "yoga", 12)  # successful ✅
nuevoGasto = registrarGasto(gastos_2024, 200, "gimnasio", 1)    # successful ✅
nuevoGasto = registrarGasto(gastos_2024, 300, "libros", 3)  # successful ✅
nuevoGasto = registrarGasto(gastos_2024, 50, "peliculas", 4)   # successful ✅
nuevoGasto = registrarGasto(gastos_2024, 75, "cine", 5)  # successful ✅
nuevoGasto = registrarGasto(gastos_2024, 100, "recitales", 6)  # successful ✅
nuevoGasto = registrarGasto(gastos_2024, 45, "remises", 7)    # successful ✅
nuevoGasto = registrarGasto(gastos_2024, 90, "kiosko", 8)  # successful ✅
nuevoGasto = registrarGasto(gastos_2024, 25, "volley", 9)  # successful ✅
nuevoGasto = registrarGasto(gastos_2024, 120, "mascotas", 10)  # successful ✅
nuevoGasto = registrarGasto(gastos_2024, 1200, "comida", 3)  # successful ✅

# Formatear todos los gastos
gastos_formateados = formatearGastos(gastos_2024)
agregarGasto(gastos_formateados, nombreArchivo)