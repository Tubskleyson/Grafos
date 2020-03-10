from busca import BuscaLargura
from caminhos.dijkstra import dijkstra

def caminho_simples(grafo, origem, v):
    """
    Retorna um caminho, se houver entre uma origem e um vertice v
    :param Grafo grafo:
    :param int origem:
    :param int v:
    :return bool:
    """

    busca_larga = BuscaLargura(grafo)

    busca_larga.busca(origem)

    if origem == v:
        print(origem)
        return True

    if busca_larga.antecessor[v] == -1:
        print("Não existe caminho de %d a %d" % (origem, v))
        return False

    caminho_simples(grafo, origem, busca_larga.antecessor[v])
    print(v)

def caminho_mais_curto(grafo, u, v):

    """
    Encontra o caminho mais curto entre dois vertices
    :param Grafo grafo:
    :param int u:
    :param int v:
    :return:
    """

    antecessor = dijkstra(grafo, u)

    if u == v:

        print(u)
        return True

    if antecessor[v] == -1:

        print("Não existe caminho de %d a %d" %(u, v))
        return False

    caminho_mais_curto(grafo, u, antecessor[v])
    print(v)