import numpy as np

np.random.seed(100019)

#calcula cuantos encestes logra un jugador con indice de enceste prob
#que hace qyt tiros libres

def ftirar(prob, qty):
  return sum(np.random.rand(qty) < prob)

#defino los jugadores
mejor = 0.8
peloton = np.array(range(700, 799)) / 1000

#vectorizo la funcion  ftirar
vec_ftirar = np.vectorize(ftirar)
primero_ganador = 0
cantidad_experimientos = 10000

for i in range(cantidad_experimientos):
  jugadores = np.append(mejor, peloton)

  vaciertos = vec_ftirar(jugadores, 50) #50 tiros por cada pibe
  idx_max = vaciertos.argsort()[-5:]

  # Creamos un array de ceros con la misma forma que el array original
  arr_zeros = np.zeros_like(vaciertos)

  # Asignamos los 5 mayores elementos al nuevo array
  arr_zeros[idx_max] = vaciertos[idx_max]
  jugadores = jugadores * arr_zeros
  
  #print(jugadores)
  vaciertos = vec_ftirar(jugadores, 100)
  #print(vaciertos)
  
  max_index = np.argmax(vaciertos)
  
  if max_index == 0:
   primero_ganador += 1

print(primero_ganador)
print(primero_ganador / cantidad_experimientos)
