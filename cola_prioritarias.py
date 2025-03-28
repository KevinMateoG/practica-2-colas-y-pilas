class EmptyQueue(Exception):
  ...

class PriorityQueue:
  def __init__(self, priority: str):
    self.__queue: list[int] = []
    self.__priority: str = priority

  # agrega al final de la cola
  def enqueue(self, mensaje: str, prioridad: int):
    self.__queue.append((mensaje,prioridad))
    if self.__priority == "min":
      self.__queue.sort(Key= lambda x: x[1])
    if self.__priority == "max":
      self.__queue.sort(key=lambda x : x[1], reverse=True)

  # retorna y elimina el primer elemento que entró
  def dequeue(self) -> int:
    if(len(self.__queue) == 0):
      raise EmptyQueue("Cola Vacía...")
    return self.__queue.pop(0)

  # retorna el primer elemento que entró
  def first(self) -> int:
    if(len(self.__queue) == 0):
      raise EmptyQueue("Cola Vacía...")
    return self.__queue[0]

  def __repr__(self):
    return str(self.__queue)

  def __len__(self):
    return len(self.__queue)

"""def priorizacion(mensaje: tuple) -> int:
  return mensaje[1]"""