from busca.busca import Busca


class BuscaProfundidade(Busca):

    """
        Representa a busca em profundidade num certo grafo
    """

    def busca(self):

        """
        Realiza a busca, sobrescrevendo o método abstrato
        :return:
        """

        self.arestas = []

        n = self.grafo.n_vertices

        tempo = 0

        tempo = 0
        cor = [None for i in range(n)]

        for u in range(n): self.antecessor[u] = -1

        for u in range(n):

            if cor[u] is None: tempo = self.visita_dfs(u, tempo, cor)

    def visita_dfs(self, u, tempo, cor):

        """
        Algoritmo recursivo onde a magia acontece
        :param int u:
        :param int tempo:
        :param int[] cor:
        :return:
        """

        cor[u] = 0
        tempo += 1

        self.d[u] = tempo

        adjs = self.grafo.adjs(u)

        if adjs:

            for v in adjs:

                if cor[v] is None:

                    self.arestas.append(0)
                    self.antecessor[v] = u

                    tempo = self.visita_dfs(v, tempo, cor)

                elif not cor[v] and (self.grafo.direcionado or self.antecessor[u] != v and u != v):

                    self.arestas.append(1)

        cor[u] = 1
        tempo += 1

        self.t[u] = tempo

        return tempo