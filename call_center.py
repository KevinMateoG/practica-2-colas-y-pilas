from time import sleep
from cola_prioritarias import *
import os
from random import randint

lista_de_experiencia = ["novato", "intermedio", "experto"]

class Agentes:
    def __init__(self, mensaje):
        self.id: int = id
        self.nivel_experiencia: str = lista_de_experiencia[randint(0,2)]
        self.estado: str = "disponible"
        self.tiempo_respuesta: int = self.calcular_tiempo_respuesta(mensaje)

    def calcular_tiempo_respuesta(self, mensaje_recibido):
        tiempo_estimando = (len(mensaje_recibido.mensaje) / 10) + (mensaje_recibido.prioridad / 2)

        if self.nivel_experiencia == "novato":
            tiempo_respuesta = tiempo_estimando
            self.estado = "ocupado"
        
        elif self.nivel_experiencia == "intermedio":
            tiempo_respuesta = tiempo_estimando*0.25
            self.estado = "ocupado"
        
        elif self.nivel_experiencia == "experto":
            tiempo_respuesta = tiempo_estimando*0.5
            self.estado = "ocupado"

        return tiempo_respuesta

class Mensaje:
    
    def __init__(self, mensaje):
        self.mensaje: str = mensaje
        self.prioridad: int = self.calcular_prioridad()

    def calcular_prioridad(self) -> tuple[str, int] :
        palabras_clave: dict[str, int] = {
        "duda": 1 ,
        "urgente": 8,
        "fallo critico": 9,
        "problema": 5,
        "consulta": 2,
        "emergencia": 10,
        "error": 6}
        prioridad = 0
        for clave in palabras_clave:
            if clave in self.mensaje:
                prioridad += palabras_clave[clave]
        return prioridad

    def __lt__(self, other):
        return self.prioridad < other.prioridad

    def __repr__(self):
        return self.mensaje

def ingresar_mensajes(mensaje: str, nombre_archivo: str):
    mensaje.lower()
    with open(f"mensajes_call_center/{nombre_archivo}.txt", "w") as archivo:
        archivo.write(mensaje)

def leer_mensaje():
    lista_mensajes: list[str] = []
    directorio = 'mensajes_call_center'
    archivos = os.listdir(directorio)
    for i in archivos:
        with open(f'mensajes_call_center/{i}', 'r') as archivo:
            contenido = archivo.read()
            lista_mensajes.append(contenido)
    return lista_mensajes

def agregar_a_cola():
    mensajes_a_recibir = leer_mensaje()
    crear_cola = PriorityQueue(orden)
    for mensaje in mensajes_a_recibir:
        crear_objeto_mensaje = Mensaje(mensaje)
        crear_cola.enqueue(crear_objeto_mensaje)
    return crear_cola

ingresar_mensajes(
    "tengo una duda mesale un mensaje con una ventana que dice error", "fallos"
)

orden = "max"
cola = agregar_a_cola()
agente_1 = Agentes(cola.first())
print(agente_1.tiempo_respuesta)
sleep(agente_1.tiempo_respuesta)
print("esta listo")