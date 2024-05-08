import datetime

class Conta:
    def __init__(self):
        self.depositos = []
        self.saques = []
        self.limite_diario = 3  # Limite de saques por dia
        self.ultimo_reset = datetime.date.today()
        self.saques_hoje = 0
        self.menu()
       

    def menu(self):
        while True:
            opcao = input('Escolha uma opção:\n'
                          '1 - Depositar\n'
                          '2 - Sacar\n'
                          '3 - Extrato\n'
                          '4 - Sair\n'
                          'Opção: ')

            if opcao == '1':
                valor = float(input('Digite o valor a depositar: '))
                self.deposito(valor)
            elif opcao == '2':
                valor = float(input('Digite o valor a sacar: '))
                self.saque(valor)
            elif opcao == '3':
                self.extrato()
                self.saldo()
            elif opcao == '4':
                print('Saindo...')
                break
            else:
                print('Opção inválida!')

    def deposito(self, valor):
        if valor > 0:
            self.depositos.append(valor)
            print('Depósito realizado com sucesso!')
        else:
            print('Valor inválido.')

    def saque(self, valor):
        today = datetime.date.today()
        if today != self.ultimo_reset:
            self.ultimo_reset = today
            self.saques_hoje = 0
        if self.saques_hoje < self.limite_diario:
            if valor <= sum(self.depositos):
                self.saques.append(valor)
                self.saques_hoje += 1
                print('Saque realizado com sucesso!')
            else:
                print('Saldo insuficiente.')
        else:
            print('Limite diário de saques atingido.')

    def extrato(self):
        print('Depósitos:', self.depositos)
        print('Saques:', self.saques)

    def saldo(self):
        saldo_final = sum(self.depositos) - sum(self.saques)
        print('Saldo :', saldo_final)

# Para testar o código
conta = Conta()
