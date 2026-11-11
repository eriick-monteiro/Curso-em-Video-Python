class ContaBancaria:
    """
Cria uma conta bancária e permite fazer saques e depósitos
    """

    def __init__(self, id, nome, saldo=0):
        self.id = id
        self._titular = nome
        self.__saldo = saldo
        print(f"Conta {self.id} criada com sucesso! Saldo atual de R${saldo:,.2f}")

    def consultar_saldo(self):
        print(f"Saldo atual R${self.__saldo:,.2f}")

    def depositar(self, valor):
        valor = abs(valor)
        self.__saldo += valor
        print(f"Depósito de R${valor:,.2f} autorizado na conta {self.id}")
        self.consultar_saldo()

    def sacar(self, valor):
        valor = abs(valor)
        if valor > self.__saldo:
            print(f"Saque de R${valor:,.2f} NEGADO na conta {self.id}")
        else:
            self.__saldo -= valor
            print(f"Saque de R${valor:,.2f} autorizado na conta {self.id}")
            self.consultar_saldo()

    def __str__(self):
    #     return f"Conta: {self.id}\nTitular: {self._titular}\nSaldo: R${self.__saldo:,.2f}"
        return  f"Estado atual da conta: {self.__dict__}"

    
