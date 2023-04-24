import numpy as np

np.random.seed(100019)

#calcula cuantos encestes logra un jugador con indice de enceste prob
#que hace qyt tiros libres

def ftirar(prob, qty):
  return sum(np.random.rand(qty) < prob)

def erra(prob):
  return np.random.rand() < prob


#defino los jugadores
mejor = 0.8
peloton = np.array(range(681, 780)) / 1000
jugadores = np.append(mejor, peloton)

#veo que tiene el vector
jugadores

#vectorizo la funcion  ftirar
vec_ftirar = np.vectorize(ftirar)
primero_ganador = 0
cantidad_experimientos = 10000

for i in range(10000): #diez mil experimentos
  jugadores = np.append(mejor, peloton)
  jugadores_indexes = np.full(len(jugadores), True, dtype=bool)

  #Itero hasta que queden 5 jugadores
  for i, jugador in enumerate(jugadores):
    if erra(jugador) and jugadores_indexes[i] == True:
      jugadores_indexes[i] = False
      
    if np.count_nonzero(jugadores_indexes) == 5:
      break
  
  #filtro los jugadores que no erraron (usando jugadores_indexes que es un array de booleanos) y los hago tirar 100 veces
  vaciertos = vec_ftirar(jugadores[jugadores_indexes], 100) 
  #maxima cantidad de aciertos
  maximo = np.max(vaciertos)
  #indice de maximo acertador
  indice_del_maximo = np.where(vaciertos == maximo)[0]
  mejor_jugador_experimiento = jugadores[indice_del_maximo][0]
  
  if mejor_jugador_experimiento == mejor:
    primero_ganador += 1

print(primero_ganador)
print(primero_ganador / cantidad_experimientos)