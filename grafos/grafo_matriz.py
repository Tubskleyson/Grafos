from grafos.grafo import Grafo

class GrafoMatriz(Grafo):

    def __init__(self, n_vertices, direcionado = False):

        super(Grafo).__init__(n_vertices, direcionado)

        self.arestas = [ [ 0 for _ in self.vertices] for _ in self.vertices ]


    def insere_aresta(self, a, b):

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

            self.arestas[a][b] = 1

            if not self.direcionado: self.arestas[b][a] = 1

            return True



    def retira_aresta(self, a, b):

        if a not in self.vertices or b not in self.vertices:
            print("Você está indicando vértices que não existem no grafo")
            return False

        else:

            if not self.existe_aresta(a,b):

                print("Aresta inexistente")
                return False

            self.arestas[a][b] = 0

            if not self.direcionado: self.arestas[b][a] = 0

            return True


    def existe_aresta(self, a, b):

        return bool(self.arestas[a][b])


    def adjs(self, vertice):

        return [ i for i in self.vertices if self.arestas[vertice][i] ]


    def n_arestas(self):

        n_arestas = sum( sum(self.arestas[i]) for i in self.vertices )

        if self.direcionado: return n_arestas

        return n_arestas // 2

    def grau(self, vertice):

        saida = sum(self.arestas[vertice])

        if self.direcionado:

            entrada = sum( self.arestas[i][vertice] for i in self.vertices if i != vertice)
            return [entrada, saida]

        return saida

    def transposto(self):

        transposto = Grafo(self.n_vertices, self.direcionado)
        transposto.vertices = self.vertices

        if not self.direcionado:
            transposto.arestas = self.arestas

            return transposto

        for i in self.vertices:

            for j in self.vertices:

                if self.arestas[i][j]:transposto.insere_aresta(j, i)

        return transposto

    def display(self):

        print("  x"+ ("{:3d}"*self.n_vertices).format(*self.vertices))

        for i in self.vertices:

            print( "{:3d}".format(i)+("{:3d}"*self.n_vertices).format(*[self.arestas[i][j] for j in self.vertices]))








