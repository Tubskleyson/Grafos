from grafos import GrafoLista
from estruturas import Heap

def prim(grafo, raiz=0):
    """
    Otem a agm por meio do Prim
    :param GrafoLista grafo:
    :param int raiz:
    :return GrafoLista:
    """

    agm = GrafoLista(grafo.n_vertices)

    n = grafo.n_vertices

    p = [0 for _ in range(n)]
    antecessor = [0 for _ in range(n)]

    vs = [0 for _ in range(n + 1)]
    itensHeap = [False for _ in range(n)]

    for u in range(n):
        antecessor[u] = -1
        p[u] = 9999999
        vs[u + 1] = u
        itensHeap[u] = True

    p[raiz] = 0

    heap = Heap(p, vs)
    heap.constroi()

    while not heap.vazio():

        u = heap.retiraMin()
        itensHeap[u] = False

        adjs = grafo.adjs(u)

        while adjs:

            adj = adjs[0]

            v = adj.v

            if itensHeap[v] and adj.peso < p[v]:
                antecessor[v] = u
                heap.diminuiChave(v, adj.peso)

            adjs = adjs[1:]

    for u in range(n):
        if antecessor[u] >= 0:
            agm.insere_aresta(u, antecessor[u])

    return agm