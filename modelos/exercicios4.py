class ContaBancariaPythonica():
    def __init__(self, titular, saldo):
        self._titular = titular.title()
        self._saldo = saldo
        self._ativo = False
    
    def __str__(self):
        return f'Titular: {self._titular} | Saldo: R$ {self._saldo} | Status: {self._ativo}'
    
    @classmethod
    def ativar_conta(cls, conta):
        conta._ativo = True

    @property
    def titular(self):
        return self._titular
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def ativo(self):
        return self._ativo  

class ClienteBanco():
    def __init__(self, nome, idade, endereco, cpf, profissao):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.cpf = cpf
        self.profissao = profissao

    @classmethod    
    def criar_conta(cls, titular, saldo_inicial):
        conta = ContaBancariaPythonica(titular, saldo_inicial)
        return conta

    
conta1 = ContaBancariaPythonica('bob', 1000000)
conta2 = ContaBancariaPythonica('lula molusco', 5000000)
conta3 = ContaBancariaPythonica('Sandy', 2000000)
print(conta1)
print(conta2)

print(f'sandy ativo: {conta3._ativo}')
ContaBancariaPythonica.ativar_conta(conta3)
print(f'sandy ativo: {conta3._ativo}')

conta4 = ContaBancariaPythonica('sirigueijo', 150000000)
print(f'titular da conta 4: {conta4.titular}')

cliente1= ClienteBanco('fualno', 23, 'rua 2', '00002222', 'carpinteiro')
cliente2 = ClienteBanco('beltrano', 12, 'rua 4', '00004444', 'estudante')
cliente3 = ClienteBanco('siclano', 49, 'rua 1', '00001111', 'engenheiro')

conta_cliente1 = ClienteBanco.criar_conta('fualno', 5000)

print(f'Conta de {conta_cliente1.titular} criada com saldo inicial de {conta_cliente1.saldo}')




