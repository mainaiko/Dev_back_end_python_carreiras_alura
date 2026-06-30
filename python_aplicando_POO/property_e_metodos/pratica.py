class ContaBancaria:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    def __str__(self):
        return f'{self._titular} - {self._saldo} - {self._ativo}'
    
    @property
    def ativo(self):
        return self._ativo
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def titular(self):
        return self._titular
    
    def ativar_conta(self):
        self._ativo = not self._ativo
    
    
# teste_1 = ContaBancaria('natalia', 1000)
# print(teste_1)
# teste_1.ativar_conta()
# print(teste_1._ativo)
# teste_1.ativar_conta()
# print(teste_1._ativo)

class ClienteBanco:
    def __init__(self, nome, idade, data_aniversario, endereco, telefone):
        self.nome = nome
        self.idade = idade
        self.data_aniversario = data_aniversario
        self.endereco = endereco
        self.telefone = telefone

    def __str__(self):
        return f'{self.nome} - {self.idade} - {self.data_aniversario} - {self.endereco} - {self.telefone}'

    @classmethod
    def criar_conta(cls, titular, saldo):
        conta = ContaBancaria(titular, saldo)
        return conta
    
cliente_1 = ClienteBanco('patati', 28, '01/02/03', 'rua araucaria', '9999 9999')
cliente_2 = ClienteBanco('patata', 40, '01/05/08', 'rua juarez', '8888 8888')

print(cliente_1)
print(cliente_2)

conta_1 = cliente_1.criar_conta('natalia', 1000)
print(conta_1)