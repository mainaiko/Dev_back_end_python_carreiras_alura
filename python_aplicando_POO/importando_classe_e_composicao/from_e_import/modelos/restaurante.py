from avaliacao import Avaliacao

class Restaurante:
    restaurantes = []
    
    def __init__(self, nome, categoria): 
        self._nome = nome.title() 
        self._categoria = categoria.upper() 
        self._ativo = False
        self._avaliacoes = [] # atributo privado avaliação que foi atribuido uma lista vazia
        Restaurante.restaurantes.append(self) 
        
    
    def __str__(self): 
        return f'{self.nome} - {self.categoria}'
    
    def listar_restaurantes(): 
        print (f'{'Nome do restaurante.'.ljust(25)} | {'Categoria'.ljust(25)} | Ativo') 
        for restaurante in Restaurante.restaurantes:
            print (f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return '☒' if self._ativo else '☐'
    
    def alterar_estado(self):
        self._ativo = not self._ativo

    # metodo que recebe a classe avaliação e passa como parametros o cliente e a nota logo apos da um append no atributo avaliações que foi definido como uma lista vazia
    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota) # objeto criado
        self._avaliacoes.append(avaliacao) # objeto armazenado

    @property
    def media_avaliacoes(self):
        if not self._avaliacoes: # verifica se tem alguma avaliação na lista
            return 0
        soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacoes) # soma todas as notas
        quantidade_de_notas = len(self._avaliacoes) # quantidade de notas
        media = round(soma_notas / quantidade_de_notas, 1) # divide a quantidade pela soma com somente uma casa decimal com o metodo round do python
        return media # retorna a media


