class Restaurante:
    restaurantes = []
    
    def __init__(self, nome, categoria): 
        self.nome = nome 
        self.categoria = categoria
        self._ativo = False # definindo o atributo como privado para que o usuario nao o modifique
        Restaurante.restaurantes.append(self) 
    
    def __str__(self): 
        return f'{self.nome} - {self.categoria}'
    
    def listar_restaurantes(): 
        print (f'{'Nome do restaurante.'.ljust(25)} | {'Categoria'.ljust(25)} | Ativo') # ljust define quantos espaços deve haver apos a string
        for restaurante in Restaurante.restaurantes:
            print (f'{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo}')

    @property # usado para modificar a forma como o atributo vai ser acessado (lido)
    def ativo(self):
        return '☒' if self._ativo else '☐'
    

restaurante_praca = Restaurante('praça', 'churrascaria')
restaurante_pizza = Restaurante('pizza place', 'fast food')

Restaurante.listar_restaurantes()