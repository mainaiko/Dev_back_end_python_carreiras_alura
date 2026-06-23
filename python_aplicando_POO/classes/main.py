class Restaurante:
    nome = ''       # variaveis dentro de uma classe recebem o nome de atributos (caracteristicas)
    categoria = '' # desse modo posso definir qual sera o atributo posteriormente
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'praça'
restaurante_praca.categoria = 'churrascaria'
restaurante_praca.ativo = True

print (dir(restaurante_praca)) # exibe os metodos do objeto
'''
terminal:

['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__firstlineno__', '__format__', '__ge__', '__getattribute__', '__getstate__', 
'__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
'__setattr__', '__sizeof__', '__static_attributes__', '__str__', '__subclasshook__', '__weakref__', 'ativo', 'categoria', 'nome']

todas os metodos especiais que toda classe python tem
bom para classes desconhecidas em que quero saber quais sao os metodos da classe
'''

print (vars(restaurante_praca)) # exibe os atributos do objeto em forma de tupla
'''
terminal:
{'nome': 'praça', 'categoria': 'churrascaria', 'ativo': True}
bom para listar os atributos de uma classe desconhecida
'''