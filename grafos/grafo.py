class Grafo:

    """
    Classe abstrata Grafo
    """

    def __init__(self, n_vertices, direcionado = False):

        """
        Inicia o grafo e seus atributos
        :param int n_vertices:
        :param bool direcionado:
        """

        self.n_vertices = n_vertices

        self.vertices = range(n_vertices)
        self.direcionado = direcionado

        self.arestas = []

    def insere_aresta(self, a, b, peso = 1):

        """
        Insere uma aresta que vai do ponto a para o ponto b
        :param int a:
        :param int b:
        :param float peso:
        :return bool:
        """

        pass

    def retira_aresta(self, a, b):

        """
        Retira uma aresta existente
        :param int a:
        :param int b:
        :return bool:
        """

        pass

    def existe_aresta(self, a, b):

        """
        Indica se uma certa aresta existe ou não
        :param int a:
        :param int b:
        :return bool:
        """

        pass

    def adjs(self, vertice):

        """
        Exibe vertices adjacentes ao vertice em questão
        :param int vertice:
        :return int[]:
        """

        pass

    def n_arestas(self):

        """
        Retorna o número de arestas do grafo
        :return int:
        """

        pass

    def transposto(self):

        """
        Retorna o grafo transposto
        :return Grafo:
        """

        pass

    def display(self):

        """
        Exibe o grafo
        :return:
        """

        pass