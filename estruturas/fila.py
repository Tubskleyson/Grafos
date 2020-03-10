class Node:

    def __init__(self, valor):

        self.valor = valor
        self.prox = None

class Fila:

    def __init__(self):

        self.raiz = None
        self.ponta = None

    def enfileira(self, valor):

        node = Node(valor)

        if self.raiz is None:

            self.raiz = node
            self.ponta = node

        else:

            self.ponta.prox = node
            self.ponta = node


    def desenfileira(self):

        node = self.raiz

        if node: self.raiz = node.prox

        return node.valor if node else node
