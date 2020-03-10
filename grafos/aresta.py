class Aresta:

    """
    Representação de aresta
    """

    def __init__(self, u, v, peso):

        """
        Inicialização das variaveis
        :param int u:
        :param int v:
        :param float peso:
        """

        self.u = u
        self.v = v

        self.peso = peso