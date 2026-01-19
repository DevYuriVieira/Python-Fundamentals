from win10toast import ToastNotifier

toaster = ToastNotifier()

# Manager PetShop:   
# Classe Produto: Preço, quantidade_estoque, nome, validade, peso.
#Classe Clientes: Nome, CPF, telefone, clube, historico_compras.
#SUPERclasse Funcionario: Nome, CPF, Cargo
# subclasse Vendedor, Veterinario.
   
class PetShop:
    def __init__(self, nome:str):
        self.nome = nome
        self.clientes = []
        self.funcionarios = []
        self.produtos = []
        self.agenda = {}

    def cadastrar_produtos(self, produto,):
        if produto not in self.produtos:
            self.produtos.append(produto)
            print(f"O produto: {produto} foi cadastrado com sucesso")
        else:
            print(f"O produto: {produto} já foi cadastrado anteriormente")


    def vender_produtos(self, produto, cliente, quantidade):
        # A quantidadde em estoque deve ser maior ou igual a quantidade vendidada.
        if produto.quantidade_estoque >= quantidade:
            produto.quantidade_estoque -= quantidade
            valor_total = quantidade * produto.preco
            log_historico = f"{produto.nome} - {quantidade} - {valor_total}"
            cliente.historico_compras.append(log_historico)
            print(f"Compra realizada com sucesso. Valor total R$ {valor_total}")
            if produto.quantidade_estoque < 5:
                toaster.show_toast("Produto esgotando", f"Precisa repor o estoque {produto.nome}", duration=10)
        else:
            print(f"Estoque insuficiente. Demanda {quantidade}, em estoque: {produto.quantidade_estoque}")

    def agendar_servico(self, cliente, funcionario, data, servico):
        # Verificar disponibilidade de data e horário
        # Verificar disponibilidade de funcionário
        # Adicionar a data escolhida na agenda do servico
        # Adicionar no historico do cliente





class Produtos:
    def __init__(self, preco:float, quantidade_estoque:int, nome:str, validade:str, peso:float):
        self.preco = preco
        self.quantidade_estoque = quantidade_estoque
        self.nome = nome
        self.validade = validade
        self.peso = peso

class Servicos:
    def __init__(self, preco:float, nome: str, status:str):
        self.preco = preco
        self.nome = nome
        self.status = status  


class Clientes:
    def __init__(self, nome: str, cpf:str, telefone:str, tem_clube:bool, historico_compras:list):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.tem_clube = tem_clube
        self.historico_compras = historico_compras

class Funcionario:
    def __init__(self, nome:str, cpf:str, cargo:str):
        self.nome = nome
        self.cpf = cpf
        self.cargo = cargo

class Vendedor(Funcionario):
    def __init__(self, nome, cpf, cargo):
        super().__init__(nome, cpf, cargo)
        
class Veterinario(Funcionario):
    def __init__(self, nome, cpf, cargo, tipo, plantao):
        super().__init__(nome, cpf, cargo)
        self.tipo = tipo
        self.plantao = plantao

petshop = PetShop("Laravel")
produto = Produtos(119.99, 10, "Ração Pedigree 20 kg Cachorro Adulto", "01/01/2027", 20)
cliente = Clientes("Zezinho", "11971256969", "215484121112", False,[])
petshop.cadastrar_produtos(produto)

petshop.vender_produtos(produto, cliente, 6)



        
        