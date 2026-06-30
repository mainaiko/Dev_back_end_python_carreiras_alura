class Restaurante:
    restaurantes = []
    
    def __init__(self, nome, categoria): 
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False 
        Restaurante.restaurantes.append(self) 
    
    def __str__(self): 
        return f'{self.nome} - {self.categoria}'
    
    @classmethod #metodo que nao esta referenciando nehuma instancia, mas sim um metodo que referencia a classe
    def listar_restaurantes(cls): 
        print (f'{'Nome do restaurante.'.ljust(25)} | {'Categoria'.ljust(25)} | Ativo') 
        for restaurante in cls.restaurantes:
            print (f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante._ativo}')

    @property
    def ativo(self):
        return '☒' if self._ativo else '☐'
    
    # metodo para os objetos, ou seja nao é um classmethod
    def alternar_estado(self): 
        self._ativo = not self._ativo # quando chamado alterna o estado do restaurante
    

restaurante_praca = Restaurante('praça', 'churrascaria')
restaurante_praca.alternar_estado()
restaurante_pizza = Restaurante('pizza place', 'fast food')

Restaurante.listar_restaurantes()