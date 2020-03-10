class ConjuntoDisjunto:

    def __init__(self):

        """
        Inicialização de variáveis
        """

        self.conjuntos = []

    def cria_conjunto(self, v):

        """
        Cria um conjunto a partir de um valor
        :param int v:
        :return:
        """

        self.conjuntos.append([v])

    def encontra_conjunto(self, v):

        """
        Retorna conjunto que possui determinado valor
        :param int v:
        :return int[]:
        """

        return [ conjunto for conjunto in self.conjuntos if v in conjunto ] [0]

    def uniao(self, u, v):

        """
        Une dois conjuntos que contém determinado valor
        :param int u:
        :param int v:
        :return:
        """
        
        c_u = self.encontra_conjunto(u)
        c_v = self.encontra_conjunto(v)

        self.conjuntos.remove(c_u)
        self.conjuntos.remove(c_v)

        self.conjuntos.append(c_u+c_v)