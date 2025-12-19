class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self._titular = titular
        self._saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if valor <= 0:
            print("Valor de saque inválido.")
        elif valor > self._saldo:
            print("Saldo insuficiente.")
        else:
            self._saldo -= valor

    def exibir_saldo(self):
        print(f"Saldo atual: R$ {self._saldo:.2f}")


# Exemplo de uso
conta = ContaBancaria("João", 100)

conta.depositar(50)
conta.sacar(30)
conta.exibir_saldo()
