import  numpy as np

np.random.seed(100019)

#calcula cuantos encestes logra un jugador con indice de enceste prob
#haciendo qyt tiros libres

def ftirar(prob, qty):
  return sum(np.random.rand(qty) < prob)



#defino los jugadores
jugadores = np.array([0.82, 0.81])

#veo que tiene el vector
jugadores

#vectorizo la funcion  ftirar
vec_ftirar = np.vectorize(ftirar)

segundo_regular = 0
cantidad_tiros = 100

for i in range(10000): #diez mil experimentos
  vaciertos = vec_ftirar(jugadores, 100) #10 tiros libres cada jugador

  if vaciertos[1] / cantidad_tiros >= 0.81:
    segundo_regular += 1


print(segundo_regular)
print(segundo_regular / 10000)