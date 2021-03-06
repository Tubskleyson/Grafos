from grafos import GrafoLista
from utils import *
from caminhos import *

a1 = [(0,1,3),(0,3,6),(0,4,9),(1,2,2),(1,3,4),(1,4,9),(1,5,9),
      (2,3,2),(2,5,8),(2,6,9),(3,6,9),(4,5,8),(4,9,8),(5,6,7),
      (5,8,9),(5,9,10),(6,7,4),(6,8,5),(7,8,1),(7,9,4),(8,9,3)]

g1 = GrafoLista(10)

for ar in a1: g1.insere_aresta(*ar)

a2 = [(0,1,4),(0,3,6),(0,4,13),(1,2,10),(1,3,2),(1,4,9),
      (2,4,1),(3,2,7),(3,6,2),(4,8,2),(5,7,2),(5,2,4),(5,8,3),
      (6,2,5),(6,5,1),(6,7,3),(8,7,1),(8,2,1)]

g2 = GrafoLista(9, True)


for ar in a2: g2.insere_aresta(*ar)



