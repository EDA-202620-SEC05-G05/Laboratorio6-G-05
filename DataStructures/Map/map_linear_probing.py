from DataStructures.List import array_list as lt
from DataStructures.Map import map_entry as me
from DataStructures.Map import map_functions as mf  



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

