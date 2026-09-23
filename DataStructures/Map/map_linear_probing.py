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




