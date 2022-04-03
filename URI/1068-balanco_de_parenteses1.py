class No:
    def __init__(self, dado):
        self.dado = dado
        self.anterior = None


class Pilha:
    def __init__(self):
        self._quantidade = 0
        self._topo = None

    @property
    def quantidade(self):
        return self._quantidade

    @property
    def topo(self):
        return self._topo

    @property
    def vazia(self):
        return self._quantidade == 0

    def _inserir_pilha_vazia(self, dado):
        novo_no = No(dado)
        self._topo = novo_no
        self._quantidade += 1

    def inserir(self, dado):
        if self.vazia:
            self._inserir_pilha_vazia(dado)
            return

        novo_no = No(dado)
        novo_no.anterior = self.topo
        self._topo = novo_no
        self._quantidade += 1

    def _remover_ultimo_elemento(self):
        removido = self.topo
        self._topo = None
        self._quantidade -= 1
        removido.anterior = None

        return removido.dado

    def remover(self):
        if self.quantidade == 1:
            return self._remover_ultimo_elemento()

        removido = self.topo
        self._topo = removido.anterior
        self._quantidade -= 1
        removido.anterior = None

        return removido.dado

    def limpar(self):
        for i in range(0, self.quantidade):
            self.remover()


parenteses = Pilha()
while True:
    try:
        frase = input()
        frase_errada = False
        for char in frase:
            if char == '(':
                parenteses.inserir(char)

            if char == ')':
                if parenteses.quantidade == 0:
                    frase_errada = True
                    break
                parenteses.remover()

        if parenteses.quantidade > 0:
            frase_errada = True
        parenteses.limpar()
        if frase_errada:
            print('incorrect')
        else:
            print('correct')

    except EOFError:
        break
