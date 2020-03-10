class TempoTermino:

    """
        Tempo para o término talvez?
    """

    def __init__(self, n):

        """
        Iniciando algumas variáveis
        :param int n:
        """

        self.t = [ 0 for _ in range(n)]
        self.restantes = [False for _ in range(n)]
        self.n_restantes = n

    def maxTT(self):

        """
        Retorna o índice do vértice restante que contém o máximo
        tempo de término
        :return int:
        """

        vMax = 0

        while not self.restantes[vMax]: vMax += 1

        for i in range(len(self.t)):

            if self.restantes[i]:

                if self.t[i] > self.t[vMax]: vMax = i

        return vMax

