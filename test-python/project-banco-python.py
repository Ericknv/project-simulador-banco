class Banco:
    def __init__(self, saldo=0, limite_saques=3):
        self.saldo = saldo
        self.limite_saques = limite_saques
        self.saques_realizados = 0

    def saque(self, valor):
        if self.saques_realizados < self.limite_saques:
            if self.saldo >= valor:
                self.saldo -= valor
                self.saques_realizados += 1
                print("Saque de", valor, "realizado com sucesso.")
            else:
                print("Saldo insuficiente.")
        else:
            print("Limite de saques atingido.")

    def deposito(self, valor):
        self.saldo += valor
        print("Depósito de", valor, "realizado com sucesso.")

    def extrato(self):
        print("Saldo:", self.saldo)


# Função principal do programa
def main():
    banco = Banco()

    while True:
        print("\n=== Sistema Bancário ===")
        print("1. Saque")
        print("2. Depósito")
        print("3. Extrato")
        print("0. Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            valor_saque = float(input("Digite o valor do saque: "))
            banco.saque(valor_saque)
        elif opcao == 2:
            valor_deposito = float(input("Digite o valor do depósito: "))
            banco.deposito(valor_deposito)
        elif opcao == 3:
            banco.extrato()
        elif opcao == 0:
            break
        else:
            print("Opção inválida. Tente novamente.")


# Executar o programa principal
main()
