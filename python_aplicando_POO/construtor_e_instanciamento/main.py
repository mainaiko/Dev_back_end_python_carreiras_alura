class Restaurante:
    restaurantes = [] # atributo de classe
    
    def __init__(self, nome, categoria, ativo): # metodo especial construtor para dizer que cada objeto tenha seus atributos especificos definidos como parametros (obrigatorios)
        self.nome = nome # o metodo construtor é o primeiro metodo a ser instanciado na criação de um objeto
        self.categoria = categoria
        self.ativo = ativo
        Restaurante.restaurantes.append(self) # toda vez que um objeto restaurante for criado ele sera adicionado a lista
    

    def __str__(self): # metodo especial que retorna alguma informação do objeto em formato de string
        return f'{self.nome} - {self.categoria}'
    
    def listar_restaurantes(): # metodo criado por mim que retorna todos os restaurantes na lista e seus atributos obrigatorios
        for restaurante in Restaurante.restaurantes:
            print (f'{restaurante.nome} - {restaurante.categoria} - {restaurante.ativo}')
    

restaurante_praca = Restaurante('praça', 'churrascaria', True)
restaurante_pizza = Restaurante('pizza place', 'fast food', True)

Restaurante.listar_restaurantes()
