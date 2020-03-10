from busca import  BuscaProfundidade
from cfc import Cfc




def ciclico(grafo):
    """
    Informa se o grafo em análise é cíclico
    :param Grafo grafo:
    :return boolean or None:
    """

    busca_profunda = BuscaProfundidade(grafo)

    busca_profunda.busca()

    return 1 in busca_profunda.arestas


def ord_topologica(grafo):

    """
    Retorno uma lista com a ordem topológica dos vertices de um grafo direcionado acíclico
    :param Grafo grafo:
    :return int[] or None:
    """

    busca_profunda = BuscaProfundidade(grafo)
    busca_profunda.busca()

    return [j[1] for j in sorted([(busca_profunda.t[i], i) for i in range(len(busca_profunda.t))])][::-1]


def fortement_conectados(grafo):
    """
    Exibe vertices fortemente conectados
    :param Grafo grafo:
    :return:
    """

    Cfc(grafo).get()