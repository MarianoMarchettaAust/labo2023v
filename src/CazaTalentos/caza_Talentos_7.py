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
  while np.count_nonzero(jugadores_indexes) > 5:
    for i, jugador in enumerate(jugadores):
      if erra(jugador) and jugadores_indexes[i] == True:
        jugadores_indexes[i] = False
        
      if np.count_nonzero(jugadores_indexes) == 5:
        break
  
  jugadores = jugadores * jugadores_indexes
  
  #print(jugadores)
  vaciertos = vec_ftirar(jugadores, 100)
  #print(vaciertos)
  
  max_index = np.argmax(vaciertos)
  
  if max_index == 0:
   primero_ganador += 1

print(primero_ganador)
print(primero_ganador / cantidad_experimientos)