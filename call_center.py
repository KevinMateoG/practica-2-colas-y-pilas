from time import sleep
from cola_prioritarias import PriorityQueue
import os
from random import randint

lista_de_experiencia = ["novato", "intermedio", "experto"]

class Agentes:
    def __init__(self):
        self.id: int = randint(1, 400)
        self.nivel_experiencia: str = lista_de_experiencia[randint(0,2)]
        self.estado: str = "disponible"

    def calcular_tiempo_respuesta(self, mensaje_recibido):
        tiempo_estimando = (len(mensaje_recibido.mensaje) / 10) + (mensaje_recibido.prioridad / 2)

        if self.nivel_experiencia == "novato":
            tiempo_respuesta = tiempo_estimando
        
        elif self.nivel_experiencia == "intermedio":
            tiempo_respuesta = tiempo_estimando*0.25
        
        elif self.nivel_experiencia == "experto":
            tiempo_respuesta = tiempo_estimando*0.5
        
        return tiempo_respuesta
    
    def __repr__(self):
        return str(self.id)

class Mensaje:
    
    def __init__(self, mensaje):
        self.mensaje: str = mensaje
        self.prioridad: int = self.calcular_prioridad()

    def calcular_prioridad(self):
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

    def __len__(self):
        return len(self.mensaje)
        
    def __lt__(self, other):
        return self.prioridad < other.prioridad

    def __repr__(self):
        return str(self.prioridad)

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

def agregar_a_cola() -> PriorityQueue:
    mensajes_a_recibir = leer_mensaje()
    crear_cola = PriorityQueue("max")
    for mensaje in mensajes_a_recibir:
        crear_objeto_mensaje = Mensaje(mensaje)
        crear_cola.enqueue(crear_objeto_mensaje)
    return crear_cola

def crear_agentes(cola: PriorityQueue) -> list[Agentes]:
    lista_de_agentes = []
    for i in range(len(cola)):
        agente = Agentes()
        lista_de_agentes.append(agente)
    return lista_de_agentes

def agente_con_mensaje(cola: PriorityQueue, lista_agentes: list[Agentes]):
    nueva_cola = PriorityQueue("max")
    for agente in lista_agentes:
        if agente.estado == "disponible":
            mensaje = cola.dequeue()
            nueva_cola.enqueue(mensaje)
            tiempo_de_espera = agente.calcular_tiempo_respuesta(mensaje)
            agente.estado = "ocupado"
            print("---------------------")
            print(f"el agente {agente.id} esta atendiendo tu mensaje, tiempo de respuesta {tiempo_de_espera}")
            sleep(tiempo_de_espera)
            print("PROBLEMA SOLUCIONADO")
        agente.estado = "disponible"
    
    for _ in range(len(nueva_cola)):
        cola.enqueue(nueva_cola.dequeue())
    print("---------------------")

def conjunto_de_mayor_prioridad(cola: PriorityQueue):
    tamaño_primer_cola = len(cola)-1
    aux = PriorityQueue("max")
    primer_mensaje = cola.dequeue()
    segundo_mensaje = cola.dequeue()
    aux.enqueue(primer_mensaje)
    aux.enqueue(segundo_mensaje)
    tamaño = 1
    maximo = 1
    nueva = PriorityQueue("max")
    for _ in range(tamaño_primer_cola):
        if len(cola) >= 1:
            if primer_mensaje.prioridad == segundo_mensaje.prioridad:
                tamaño += 1
                primer_mensaje = segundo_mensaje
                segundo_mensaje = cola.dequeue()
                aux.enqueue(segundo_mensaje)
            
            elif primer_mensaje.prioridad != segundo_mensaje.prioridad:
                tamaño = 1
                nueva = PriorityQueue("max")
                primer_mensaje = segundo_mensaje
                segundo_mensaje = cola.dequeue()
                aux.enqueue(segundo_mensaje)
            
            nueva.enqueue(primer_mensaje)

            if tamaño > maximo:
                maximo = tamaño
                cola_maxima = nueva
        
        else:
            if primer_mensaje.prioridad == segundo_mensaje.prioridad:
                tamaño += 1
                nueva.enqueue(segundo_mensaje)
            if tamaño > maximo:
                maximo = tamaño
                cola_maxima = nueva

    for _ in range(len(aux)):
        cola.enqueue(aux.dequeue())
    
    return cola_maxima

def atender_primero_y_ultimo(cola: PriorityQueue, lista_agentes):
    cola_con_mayor_prioridad = conjunto_de_mayor_prioridad(cola)
    print(cola_con_mayor_prioridad)
    primer_mensaje = cola_con_mayor_prioridad.first()
    seleccionar_agente = lista_agentes[randint(0, len(lista_agentes)-1)]
    tiempo_repuesta =seleccionar_agente.calcular_tiempo_respuesta(primer_mensaje)
    print(f"el agente {seleccionar_agente.id} esta atendiendo tu mensaje, tiempo de respuesta {tiempo_repuesta}")
    sleep(tiempo_repuesta)
    print("PROBLEMA SOLUCIONADO")
    print("---------------------")
    for _ in range (len(cola_con_mayor_prioridad)):
        ultimo_mensaje = cola_con_mayor_prioridad.dequeue()
    seleccionar_agente = lista_agentes[randint(0, len(lista_agentes)-1)]
    tiempo_repuesta =seleccionar_agente.calcular_tiempo_respuesta(ultimo_mensaje)
    print(f"el agente {seleccionar_agente.id} esta atendiendo tu mensaje, tiempo de respuesta {tiempo_repuesta}")
    sleep(tiempo_repuesta)
    print("PROBLEMA SOLUCIONADO")
    print("---------------------")

def promedio_de_cola(cola: PriorityQueue):
    aux = PriorityQueue("max")
    tamaño_mensajes = 0
    primer_mensaje = cola.dequeue()
    aux.enqueue(primer_mensaje)
    for _ in range(len(cola)):
        if len(cola) >= 0:
            tamaño_mensajes += primer_mensaje.prioridad
            primer_mensaje = cola.dequeue()
            aux.enqueue(primer_mensaje)
    for _ in range(len(aux)):
        cola.enqueue(aux.dequeue())
    return tamaño_mensajes/len(cola)

def eliminar_de_cola_mayor(cola:PriorityQueue):
    promedio = promedio_de_cola(cola)
    conjunto_mayor = conjunto_de_mayor_prioridad(cola)
    promedio -= len(conjunto_mayor)
    for _ in range(round(promedio)):
        conjunto_mayor.dequeue()
    return conjunto_mayor

cola_con_mensaje = agregar_a_cola()
lista_agentes = crear_agentes(cola_con_mensaje)
print(cola_con_mensaje)
print(promedio_de_cola(cola_con_mensaje))
print(eliminar_de_cola_mayor(cola_con_mensaje))
"""
while True:
    requiere_mensaje = input("¿Quieres agregar un nuevo mensaje?, si deseas salir pon la palabra SALIDA: ")
    
    if requiere_mensaje.lower() == "si":
        texto_del_mensaje = input("¿Que mensaje deseas ingresar?: ")
        nombre_mensaje = input("Pon un titulo al mensaje: ")
        ingresar_mensajes(texto_del_mensaje, nombre_mensaje)
    if requiere_mensaje.lower() == "salida":
        break
    cola_con_mensaje = agregar_a_cola()
    lista_agentes = crear_agentes(cola_con_mensaje)
    
    if requiere_mensaje.lower() == "p":
        atender_primero_y_ultimo(cola_con_mensaje, lista_agentes)
    agente_con_mensaje(cola_con_mensaje, lista_agentes)
"""
