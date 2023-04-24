import numpy as np

np.random.seed(100019)

#calcula cuantos encestes logra un jugador con indice de enceste prob
#haciendo qyt tiros libres

def ftirar(prob, qty):
  return sum(np.random.rand(qty) < prob)



#defino los jugadores
mejor = 0.80
jugadores = np.array(mejor)

#vectorizo la funcion  ftirar
vec_ftirar = np.vectorize(ftirar)

primero_ganador = 0
cantidad_tiros = 100

for i in range(10000): #diez mil experimentos
  vaciertos = vec_ftirar(jugadores, cantidad_tiros) #100 tiros libres cada jugador

  if (vaciertos / cantidad_tiros) >= mejor:
    primero_ganador += 1


print(primero_ganador)
print(primero_ganador / 10000)