class Restaurante:
    restaurantes = []
    
    def __init__(self, nome, categoria): 
        self._nome = nome.title() #define que a primeira letra do atributo sempre sera maiuscula
        self._categoria = categoria.upper() # define que todos as letras desse atributo vao ser maiusculas
        self._ativo = False 
        Restaurante.restaurantes.append(self) 
        # boa pratica é definir todos os atributos como privados
    
    def __str__(self): 
        return f'{self.nome} - {self.categoria}'
    
    def listar_restaurantes(): 
        print (f'{'Nome do restaurante.'.ljust(25)} | {'Categoria'.ljust(25)} | Ativo') 
        for restaurante in Restaurante.restaurantes:
            print (f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante._ativo}')

    @property
    def ativo(self):
        return '☒' if self._ativo else '☐'
    

restaurante_praca = Restaurante('praça', 'churrascaria')
restaurante_pizza = Restaurante('pizza place', 'fast food')

Restaurante.listar_restaurantes()