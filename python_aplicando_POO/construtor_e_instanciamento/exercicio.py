'''
Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. Crie uma instância dessa classe e atribua valores aos seus atributos.
Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.
Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros e inicia ativo como False por padrão. Crie uma instância utilizando o construtor.
Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância, seja exibida uma mensagem formatada com o nome e a categoria. Exiba essa mensagem para uma instância de restaurante.
Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.
'''

class Carro:
    modelo = ''
    cor = ''
    ano = ''

class Restaurante:
    def __init__(self, nome, categoria, ativo = False):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo

    def __str__(self):
        return f'{self.nome} - {self.categoria}'

restaurante_1 = Restaurante('peixin', 'churrascaria')

print (restaurante_1)

class Cliente:
    def __init__(self, nome, sobrenome, idade, email):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.email = email

cliente_1 = Cliente('joaozin', 'mendes', 18, 'joaozinmendes@.com')
cliente_2 = Cliente('pedrin', 'mendes', 20, 'pedrinmendes@.com')
cliente_3 = Cliente('mariazinha', 'mendes', 22, 'mariazinhamendes@.com')
