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

class Mensaje:
    def __init__(self, mensaje):
        self.mensaje: str = mensaje
    
    def calcular_prioridad(self) -> tuple[str, int] :
        for clave in prioridad:
            if clave in self.mensaje:
                return prioridad[clave]

    def __repr__(self):
        return self.mensaje

def ingresar_mensajes(mensaje: str, nombre_archivo: str):
    mensaje.lower()
    with open(f"mensajes_call_center\{nombre_archivo}.tcrear_objeto_mensajet", "w") as archivo:
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

def agragar_a_cola():
    mensajes_a_recibir = leer_mensaje()
    crear_cola = PriorityQueue(orden)
    for mensaje in mensajes_a_recibir:
        crear_objeto_mensaje = Mensaje(mensaje)
        priorizacion = crear_objeto_mensaje.calcular_prioridad()
        crear_cola.enqueue(mensaje, priorizacion)
    return crear_cola


ingresar_mensajes(
    "tengo una emergencia", "ensima"
)

ingresar_mensajes(
    "hubo un fallo critico en la pagina arreglenlo por favor", "arreglar_fallo"
)
orden = "max"
print(agragar_a_cola())