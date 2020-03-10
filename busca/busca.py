class Busca:

    """
    Classe abstrata de busca em grafos
    """
    def __init__(self, grafo):

        """
        Inicia as variáveis
        :param Grafo grafo:
        """

        self.grafo = grafo
        n = grafo.n_vertices

        self.d = [0 for _ in range(n)]
        self.t = [0 for _ in range(n)]
        self.antecessor = [0 for _ in range(n)]

        self.arestas = []

    def busca(self):
        """
        Método abstrato para efetuar a busca em um grafo
        :return None:
        """
        pass