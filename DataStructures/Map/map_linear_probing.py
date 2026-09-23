from DataStructures.List import array_list as lt
from DataStructures.Map import map_entry as me
from DataStructures.Map import map_functions as mf 
import random 


def new_map(num_elements, load_factor, prime=109345121):
    capacity = mf.next_prime(int(num_elements / load_factor))
    scale = random.randint(1, prime - 1)
    shift = random.randint(0, prime - 1)
 
    table = lt.new_list()
    for _ in range(capacity):
        empty_entry = me.new_map_entry(None, None)
        lt.add_last(table, empty_entry)
 
    my_map = {
        "prime": prime,
        "capacity": capacity,
        "scale": scale,
        "shift": shift,
        "table": table,
        "current_factor": 0,
        "limit_factor": load_factor,
        "size": 0,
    }
    return my_map


def find_slot(my_map, key, hash_value):
   first_avail = None
   found = False
   ocupied = False
   while not found:
      if mf.is_available(my_map["table"], hash_value):
            if first_avail is None:
               first_avail = hash_value
            entry = lt.get_element(my_map["table"], hash_value)
            if me.get_key(entry) is None:
               found = True
      elif mf.default_compare(key, lt.get_element(my_map["table"], hash_value)) == 0:
            first_avail = hash_value
            found = True
            ocupied = True
      hash_value = (hash_value + 1) % my_map["capacity"]
   return ocupied, first_avail

def put(my_map, key, value):
    hash_value = mf.hash_value(my_map, key)
    ocupied, pos = find_slot(my_map, key, hash_value)
 
    entry = me.new_map_entry(key, value)
    lt.change_info(my_map["table"], pos, entry)
 
    if not ocupied:
        my_map["size"] += 1
        my_map["current_factor"] = my_map["size"] / my_map["capacity"]
        if my_map["current_factor"] >= my_map["limit_factor"]:
            rehash(my_map)
 
    return my_map
 
 
def contains(my_map, key):
    hash_value = mf.hash_value(my_map, key)
    ocupied, _ = find_slot(my_map, key, hash_value)
    return ocupied

def rehash(my_map):
    old_table = my_map["table"]
    old_capacity = my_map["capacity"]
 
    new_capacity = mf.next_prime(old_capacity * 2)
    new_table = lt.new_list()
    for i in range(new_capacity):
        empty_entry = me.new_map_entry(None, None)
        lt.add_last(new_table, empty_entry)
 
    my_map["table"] = new_table
    my_map["capacity"] = new_capacity
    my_map["size"] = 0
    my_map["current_factor"] = 0
 
    for pos in range(old_capacity):
        entry = lt.get_element(old_table, pos)
        key = me.get_key(entry)
        if key is not None and key != mf.AVAILABLE:
            value = me.get_value(entry)
            put(my_map, key, value)
 
    return my_map


def get(my_map, key):
   """
   Retorna el valor asociado a la llave ``key`` en el mapa.

   :param my_map: Mapa del cual se desea obtener el valor.
   :type my_map: :ref:`map<map>`
   :param key: Llave de la cual se desea obtener el valor.
   :type key: any

   :return: Valor asociado a la llave ``key`` en el mapa.
   :rtype: any
   """
   hash_value = mf.hash_value(my_map, key)
   ocupied, slot = find_slot(my_map, key, hash_value)
   if ocupied:
      entry = lt.get_element(my_map["table"], slot)
      return me.get_value(entry)
   else:
      return None

def remove(my_map, key):
   """
   Elimina la entrada asociada a la llave ``key`` en el mapa.

   :param my_map: Mapa del cual se desea eliminar la entrada.
   :type my_map: :ref:`map<map>`
   :param key: Llave de la entrada que se desea eliminar.
   :type key: any

   :return: Valor asociado a la llave ``key`` en el mapa antes de ser eliminada.
   :rtype: any
   """
   hash_value = mf.hash_value(my_map, key)
   ocupied, slot = find_slot(my_map, key, hash_value)
   if ocupied:
      entry = lt.get_element(my_map["table"], slot)
      value = me.get_value(entry)
      me.set_key(entry, None)
      me.set_value(entry, None)
      return value
   else:
      return None
  
def size(my_map):
   """
   Retorna el número de entradas en el mapa.

   :param my_map: Mapa del cual se desea obtener el tamaño.
   :type my_map: :ref:`map<map>`

   :return: Número de entradas en el mapa.
   :rtype: int
   """
   return my_map["size"]

