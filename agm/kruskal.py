from grafos import GrafoLista
from estruturas import ConjuntoDisjunto

def kruskal(grafo):
    """
    Obtem a agm por meio de kruskal
    :param GrafoLista grafo:
    :return:
    """

    agm = GrafoLista(grafo.n_vertices)

    conj = ConjuntoDisjunto()

    arestas = []

    for u in grafo.vertices:

        conj.cria_conjunto(u)

        for v in grafo.vertices[u:]:

            aresta = grafo.existe_aresta(u, v)

            if aresta:
                arestas.append([aresta.peso, (u, v)])

    arestas.sort()

    arestas = [aresta[1] for aresta in arestas]

    for u, v in arestas:

        if conj.encontra_conjunto(u) != conj.encontra_conjunto(v):
            agm.insere_aresta(u, v)
            conj.uniao(u, v)

    return agm