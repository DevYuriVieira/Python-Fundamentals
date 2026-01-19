#banco(contas)
# cliente conta, sacar, depositar, saldo

class Banco:
    def __init__(self, nome:str):
        self.nome = nome
        self.clientes = []
        self.contas = []
        self.login_ativo = []
        
    def cadastrar_cliente(self, nome:str, cpf:str, senha:str):
        cliente_ativo = False
        for cliente in self.clientes:
            if cliente.cpf == cpf:
                cliente_ativo = cliente
        if cliente_ativo:
                    print("Cliente já ativo")
                    return cliente_ativo
        else:
            cliente = Cliente(nome, cpf, senha)
            conta = banco.criar_conta()
            cliente.conta = conta
            banco.clientes.append(cliente)
            banco.contas.append(conta)
            print("Cliente cadastrado com sucesso!")
            return cliente
                

    def criar_conta(self):
        conta = Conta()
        return conta

    def login (self, cpf, senha):
        cliente_ativo = False
        for cliente in self.clientes:
            if cpf == cliente.cpf:
                cliente_ativo = True
                if senha == cliente.senha:
                    self.login_ativo.append(cpf)
                    print("Login feito com sucesso")
                    return cliente
        if cliente_ativo == False:
            print("Conta não encontrada, deseja criar conta?")

class Cliente:
    def __init__(self, nome: str, cpf: str, senha:str):
        self.nome = nome
        self.cpf = cpf
        self.senha = senha
        self.conta = ""
    

class Conta:
    def __init__(self):
        self._saldo = 100

    @property
    def saldo(self):
        return f"R$ {self._saldo}"
    
    def saque(self, valor):
        novo_valor = self._saldo - valor
        if novo_valor <= 0:
            print("Seu saldo é insuficiente")
        else:
            self.saldo = novo_valor
            print(f"Seu novo saldo é {novo_valor}")

    def deposito(self, valor):
        novo_valor = self._saldo + valor
        if novo_valor < 0:
            print("Valor inválido")
        else:
            self.saldo = novo_valor
            print(f"Foram adicionados {valor} a sua conta. Seu novo saldo é de {novo_valor}")

    def ver_saldo(self):
        return f"R$ {self._saldo}"

conta_cliente = Conta()

banco = Banco("Sicoob")

while True:
    print("=======\nBem vindo ao Sicoob\n=======")
    menu = int(input("1 - criar conta | 2 - login | 3 - sair: "))
    match menu:
        case 1:
            if menu == 1:
                nome = input("Qual seu nome: ")
                cpf = input("Qual seu CPF: ")
                senha = input("Digite uma senha: ")
                banco.cadastrar_cliente(nome, cpf, senha)
            else:
                pass
        case 2:
            if menu == 2:
                cpf = input("Digite seu CPF: ")
                senha = input("Digite sua senha: ")
                banco.login(cpf,senha)
                conta = banco.login(cpf, senha)
                if cpf in banco.login_ativo:
                    while True:
                        menu_login = int(input("1 - Saldo | 2 - Saque | 3 - Depósito | 4 sair: "))
                        conta = banco.login(cpf, senha)
                        match menu_login:
                            case 1:
                                valor = int(input("Valor do seu saldo é: "))
                                conta_cliente.saldo
                            case 2:
                                valor = int(input("Quanto deseja sacar: "))
                                conta_cliente.saque(valor)
                            case 3:
                                valor = int(input("Qual valor do depósito: "))
                                conta_cliente.deposito(valor)
                            case 4:
                                break

    