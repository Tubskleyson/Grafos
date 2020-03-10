from busca.busca import Busca
from estruturas import Fila

class BuscaLargura(Busca):

    """
        Representa a busca em largura num certo grafo
    """

    def busca(self, origem = 0):

        """
            Realiza a busca, sobrescrevendo o método abstrato
            :return:
        """

        n = self.grafo.n_vertices

        cor = [None for i in range(n)]

        l = list(range(n))
        l.remove(origem)
        l = [origem] + l


        for u in l:
            self.antecessor[u] = -1
            self.d[u] = 10 ** 1000

        for u in l:

            if cor[u] is None: self.visita_dfs(u, cor)

    def visita_dfs(self, u, cor):

        """
        Algoritmo recursivo onde a magia acontece
        :param int u:
        :param int[] cor:
        :return:
        """

        cor[u] = 0
        self.d[u] = 0

        fila = Fila()
        fila.enfileira(u)

        while fila.raiz:

            u = fila.desenfileira()

            adjs = self.grafo.adjs(u)

            if adjs:

                for a in adjs:


                    v = a.v

                    if cor[v] is None:

                        cor[v] = 0
                        self.d[v] = self.d[u] + 1
                        self.antecessor[v] = u
                        fila.enfileira(v)

        cor[u] = 1