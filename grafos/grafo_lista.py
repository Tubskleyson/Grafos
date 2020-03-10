from grafos.grafo import Grafo
from grafos.aresta import Aresta

class GrafoLista(Grafo):

    def __init__(self, n_vertices, direcionado = False):

        super().__init__(n_vertices, direcionado)

        self.arestas = [ [] for _ in self.vertices ]


    def insere_aresta(self, a, b, peso = 1):

        if a not in self.vertices or b not in self.vertices:

            print("Você está indicando vértices que não existem no grafo")
            return False

        if not self.direcionado and a == b:

            print("Não é possível criar um self-loop em um grafo não direcionado")
            return False

        else:

            if self.existe_aresta(a,b):

                print("Aresta já existe")
                return False

            self.arestas[a].append(Aresta(a, b, peso))

            if not self.direcionado: self.arestas[b].append(Aresta(b, a, peso))

            return True


    def retira_aresta(self, a, b):

        if a not in self.vertices or b not in self.vertices:
            print("Você está indicando vértices que não existem no grafo")
            return False

        else:

            if not self.existe_aresta(a, b):
                print("Aresta inexistente")
                return False

            self.arestas[a] = [i for i in self.arestas[a] if i.v != b]

            if not self.direcionado: self.arestas[b] = [i for i in self.arestas[b] if i.v != a]

            return True



    def existe_aresta(self, a, b):

        l = [ aresta for aresta in self.arestas[a] if aresta.v == b]

        if l: return l[0]
        return False


    def adjs(self, vertice):

        return self.arestas[vertice]


    def n_arestas(self):

        n_arestas = sum(len(i) for i in self.arestas)

        if self.direcionado: return n_arestas

        return n_arestas // 2


    def grau(self, vertice):

        """
        Retorna o grau de um determinado vertice
        :param int vertice:
        :return int or int[]:
        """

        saida = len(self.arestas[vertice])

        if self.direcionado:

            entrada = sum((aresta.v == vertice for aresta in l) for l in self.arestas)

            return [entrada, saida]

        return saida

    def transposto(self):

        transposto = Grafo(self.n_vertices, self.direcionado)
        transposto.vertices = self.vertices

        if not self.direcionado:

            transposto.arestas = self.arestas

            return transposto

        for i in self.vertices:

            for j in self.arestas[i]:

                transposto.insere_aresta(j.v, i)

        return transposto



    def display(self):


        for i in self.vertices:

            print("{:3d} :".format(i)+("{:3d}"*len(self.arestas[i])).format(*[aresta.v for aresta in self.arestas[i]]))


