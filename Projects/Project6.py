# Búsqueda Ingenua / Naive Search
# Búsqueda Binaria / Binary Search

import random
import time

def naive_search(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i
    return -1

def binary_search(list, target, limit_bottom=None, limit_top=None):
    if limit_bottom is None:
        limit_bottom = 0  # Inicio de la lista
    if limit_top is None:
        limit_top = len(list) - 1  # Final de la lista
    if limit_top < limit_bottom:
        return -1
    
    middle_point = (limit_bottom + limit_top) // 2

    if list[middle_point] == target:
        return middle_point
    elif target < list[middle_point]:
        return binary_search(list, target, limit_bottom, middle_point - 1)
    else:
        return binary_search(list, target, middle_point + 1, limit_top)


if __name__ == '__main__':
  # Crear una lista ordenada con 10000 números aleatorios.
  size = 100000
  initial_set = set()

  while len(initial_set) < size:
      initial_set.add(random.randint(-3*size, 3*size))

  ordered_list = sorted(list(initial_set))

  # Medir el tiempo de búsqueda ingenua
  start = time.time()
  for target in ordered_list:
      binary_search(ordered_list, target)
  end = time.time()
  print(f"Tiempo de búsqueda ingenua: {end - start} segundos.")
  
  # Medir el tiempo de búsqueda binaria
  start = time.time()
  for target in ordered_list:
      binary_search(ordered_list, target)
  end = time.time()
  print(f"Tiempo de búsqueda binaria: {end - start} segundos.")