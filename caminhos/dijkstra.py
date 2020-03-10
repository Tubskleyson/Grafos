from estruturas import Heap

def dijkstra(grafo, raiz):
    """
    Realiza o algoritmo de dijkstra partindo de uma origem
    :param Grafo grafo:
    :param int raiz:
    :return int[]:
    """

    n = grafo.n_vertices

    p = [0 for _ in range(n)]
    antecessor = [0 for _ in range(n)]

    vs = [0 for _ in range(n + 1)]

    for u in range(n):
        antecessor[u] = -1
        p[u] = 9999999
        vs[u + 1] = u

    p[raiz] = 0

    heap = Heap(p, vs)

    heap.constroi()

    while not heap.vazio():

        u = heap.retiraMin()

        adjs = grafo.adjs(u)

        while adjs:

            adj = adjs[0]

            v = adj.v

            if p[v] > p[u] + adj.peso:
                antecessor[v] = u
                heap.diminuiChave(v, p[u] + adj.peso)

            adjs = adjs[1:]

    return antecessor