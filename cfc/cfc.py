from cfc.tempo_termino import TempoTermino
from busca import BuscaProfundidade

class Cfc:

    """
        Busca por componentes fortemente conectados
    """

    def __init__(self, grafo):

        """
        Iniciando algumas variáveis
        :param Grafo grafo:
        """

        self.grafo = grafo


    def get(self):

        """
        Realiza a busca
        :return:
        """

        dfs = BuscaProfundidade(self.grafo)
        dfs.busca()

        tt = TempoTermino(self.grafo.n_vertices)

        for u in range(self.grafo.n_vertices):

            tt.t[u] = dfs.t[u]
            tt.restantes[u] = True

        grafoT = self.grafo.transposto()

        while tt.n_restantes:

            vRaiz = tt.maxTT()
            print("Raiz da pŕoxima árvore:", vRaiz)
            self.visitaDfs(grafoT,vRaiz,tt)


    def visitaDfs(self, grafo, u, tt):

        """
        Pequena busca
        :param Grafo grafo:
        :param int u:
        :param TempoTermino tt:
        :return:
        """

        tt.restantes[u] = False
        tt.n_restantes -= 1

        print("Vertice:", u)

        adjs = grafo.adjs(u)

        if adjs:

            for v in adjs:

                if tt.restantes[v]: self.visitaDfs(grafo, v, tt)


