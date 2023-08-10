class Banco:
    def __init__(self, saldo=0, limite_saques=3):
        self.saldo = saldo
        self.limite_saques = limite_saques
        self.saques_realizados = 0

    def saque(self, valor, usuario):
        if self.saques_realizados < self.limite_saques:
            if self.saldo >= valor:
                self.saldo -= valor
                self.saques_realizados += 1
                print(f"Saque de {valor:.2f} realizado com sucesso para o usuário {usuario.nome}.")
            else:
                print("Saldo insuficiente.")
        else:
            print("Limite de saques atingido.")

    def deposito(self, valor, usuario):
        self.saldo += valor
        print(f"Depósito de {valor:.2f} realizado com sucesso para o usuário {usuario.nome}.")

    def extrato(self, usuario, conta):
        print(f"Extrato do usuário {usuario.nome}, CPF {usuario.cpf}, conta {conta}: Saldo = {self.saldo:.2f}")


class Usuario:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf


def criar_usuario():
    nome = input("Digite o nome do usuário: ")
    cpf = input("Digite o número de CPF do usuário: ")
    print(f"Usuário {nome} criado com sucesso.")
    return Usuario(nome, cpf)


def criar_conta(usuario, saldo_inicial=0, limite_saques=3):
    conta = Banco(saldo_inicial, limite_saques)
    print(f"Conta criada para o usuário {usuario.nome}.")
    return conta


# Função principal do programa
def main():
    usuarios = []

    while True:
        print("\n=== Sistema Bancário ===")
        print("1. Criar Usuário")
        print("2. Criar Conta")
        print("3. Saque")
        print("4. Depósito")
        print("5. Extrato")
        print("0. Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            usuarios.append(criar_usuario())
        elif opcao == 2:
            if usuarios:
                nome_usuario = input("Digite o nome do usuário para criar a conta: ")
                usuario = None
                for u in usuarios:
                    if u.nome == nome_usuario:
                        usuario = u
                        break
                if usuario:
                    saldo_inicial = float(input("Digite o saldo inicial da conta: "))
                    limite_saques = int(input("Digite o limite de saques da conta: "))
                    conta = criar_conta(usuario, saldo_inicial, limite_saques)
                else:
                    print("Usuário não encontrado.")
            else:
                print("Crie um usuário primeiro.")
        elif opcao == 3:
            if usuarios:
                nome_usuario = input("Digite o nome do usuário: ")
                valor_saque = float(input("Digite o valor do saque: "))
                usuario = None
                for u in usuarios:
                    if u.nome == nome_usuario:
                        usuario = u
                        break
                if usuario:
                    conta.saque(valor_saque, usuario)
                else:
                    print("Usuário não encontrado.")
            else:
                print("Crie um usuário primeiro.")
        elif opcao == 4:
            if usuarios:
                nome_usuario = input("Digite o nome do usuário: ")
                valor_deposito = float(input("Digite o valor do depósito: "))
                usuario = None
                for u in usuarios:
                    if u.nome == nome_usuario:
                        usuario = u
                        break
                if usuario:
                    conta.deposito(valor_deposito, usuario)
                else:
                    print("Usuário não encontrado.")
            else:
                print("Crie um usuário primeiro.")
        elif opcao == 5:
            if usuarios:
                nome_usuario = input("Digite o nome do usuário: ")
                usuario = None
                for u in usuarios:
                    if u.nome == nome_usuario:
                        usuario = u
                        break
                if usuario:
                    conta.extrato(usuario, "001")
                else:
                    print("Usuário não encontrado.")
            else:
                print("Crie um usuário primeiro.")
        elif opcao == 0:
            break
        else:
            print("Opção inválida. Tente novamente.")


# Executar o programa principal
main()
