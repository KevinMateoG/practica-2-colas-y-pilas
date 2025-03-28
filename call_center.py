from cola_prioritarias import *
import os

prioridad: dict[str, int] = {
    "duda": 1 ,
    "urgente": 8,
    "fallo critico": 9,
    "problema": 5,
    "consulta": 2,
    "emergencia": 10,
    "error": 6
}

def ingresar_mensajes(mensaje: str, nombre_archivo: str):
    mensaje.lower()
    with open(f"mensajes_call_center\{nombre_archivo}.txt", "w") as archivo:
        archivo.write(mensaje)
    
def leer_mensaje():
    lista_mensajes: list[str] = []
    directorio = 'mensajes_call_center'
    archivos = os.listdir(directorio)
    for i in archivos:
        with open(f'mensajes_call_center\{i}', 'r') as archivo:
            contenido = archivo.read()
            lista_mensajes.append(contenido)
    return lista_mensajes

def verificar_prioridad():
    lista_mensajes = leer_mensaje()
    lista_de_mensaje_prioridad: list[tuple[str, int]]=[]
    for mensaje in lista_mensajes:
        for clave in prioridad:
            if clave in mensaje:
                mensaje_con_prioridad = (mensaje, prioridad[clave])
                lista_de_mensaje_prioridad.append(mensaje_con_prioridad)
    return lista_de_mensaje_prioridad

def agragar_a_cola():
    lista_con_prioridad = verificar_prioridad()
    priorizacion = PriorityQueue("max")
    for priorizar, prioridad in lista_con_prioridad:
        priorizacion.enqueue(priorizar, prioridad)
    return priorizacion


ingresar_mensajes(
    "tengo una emergencia", "ensima"
)
ingresar_mensajes(
    "hubo un fallo critico en la pagina arreglenlo por favor", "arreglar_fallo"
)

print(agragar_a_cola())
