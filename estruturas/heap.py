class Heap:

    """
    Estrutura de dados utilizada para o algoritmo PRIM
    """

    def __init__(self, p, v):

        """
        Inicialização da variáveis
        :param float[] p:
        :param int[] v:
        """

        self.p = p
        self.fp = v

        self.n = len(self.fp) - 1
        self.pos = [0 for _ in range(self.n)]

        for i in range(self.n): self.pos[i] = i+1

    def refaz(self, e, d):

        """
        Refaz o heap minimo
        :param int e:
        :param int d:
        :return:
        """

        j = e * 2
        x = self.fp[e]

        while j <= d:

            if j < d and self.p[self.fp[j]] > self.p[self.fp[j+1]]: j += 1
            if self.p[x] <= self.p[self.fp[j]]: break

            self.fp[e] = self.fp[j]
            self.pos[self.fp[j]] = e

            e = j
            j *= 2

        self.fp[e] = x
        self.pos[x] = e

    def constroi(self):

        """
        Constrói o heap
        :return:
        """

        esq = self.n//2 + 1

        while esq > 1:

            esq -= 1
            self.refaz(esq, self.n)

    def retiraMin(self):

        """
        Retorna o valor mínimo
        :return int:
        """

        if self.n < 1:

            print("Heap está vazio")
            return None

        else:

            minimo = self.fp[1]
            self.fp[1] = self.fp[self.n]

            self.pos[self.fp[self.n]] = 1

            self.n -= 1

            self.refaz(1, self.n)

            return  minimo

    def diminuiChave(self, i, chaveNova):

        """
        Diminui o peso de um vertice
        :param int i:
        :param float chaveNova:
        :return:
        """

        if chaveNova < 0:

            print("Valor de chave invalido")
            return

        i = self.pos[i]
        x = self.fp[i]

        self.p[x] = chaveNova

        while i>1 and self.p[x] <= self.p[self.fp[i//2]]:

            self.fp[i] = self.fp[i//2]
            self.pos[self.fp[i//2]] = i
            i //= 2

        self.fp[i] = x
        self.pos[x] = i

    def vazio(self):

        """
        Indica se o heap está vazio
        :return bool:
        """

        return not self.n