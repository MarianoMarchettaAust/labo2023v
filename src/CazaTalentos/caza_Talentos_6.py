import numpy as np

np.random.seed(100019)

#calcula cuantos encestes logra un jugador con indice de enceste prob
#que hace qyt tiros libres

def ftirar(prob, qty):
  return sum(np.random.rand(qty) < prob)



#defino los jugadores
mejor = 0.8
peloton = np.array(range(691, 790)) / 1000
jugadores = np.append(mejor, peloton)

#veo que tiene el vector
jugadores

#vectorizo la funcion  ftirar
vec_ftirar = np.vectorize(ftirar)
primero_ganador = 0
cantidad_experimientos = 10000

for i in range(cantidad_experimientos):
  #print(f'Iteracion numero {i}')

  vaciertos = vec_ftirar(jugadores, 50)
  mejores_cinco = sorted((vaciertos))[:5] #obtengo los primeros 5
  
  # for jugador in mejores_cinco:
  #   aciertos_torneo = vaciertos[jugador]
  #   aciertos_segunda = vec_ftirar(jugadores[jugador], 100) #a cada uno de los primeros 5 los hago volver a tirar
  #   print(aciertos_torneo, "\t", aciertos_segunda, "\t", aciertos_torneo/50, aciertos_segunda/100)
  maximo = np.max(vaciertos)
  #indice de maximo acertador
  indice_del_maximo = np.where(vaciertos == maximo)[0]
  mejor_jugador_experimiento = jugadores[indice_del_maximo][0]
  
  if mejor_jugador_experimiento == mejor:
    primero_ganador += 1

print(primero_ganador)
print(primero_ganador / cantidad_experimientos)
