class Biblioteca:
    def __init__(self, nome: str, dias_de_emprestimo: int):
        self.nome = nome
        self.livros = []
        self.usuarios = []
        self.dias_de_emprestimo = dias_de_emprestimo

    def __str__(self):
        return f"Essa é a {self.nome}"

    def emprestar_livro(self, usuario, livro):
        if usuario not in self.usuarios:
            print("Usuário não cadastrado na biblioteca.")
            return

        if not livro.disponibilidade:
            print("O livro não está disponível.")
            return

        if len(usuario.livros_alugados) >= 3:
            print("Limite excedido de livros alugados.")
            return

        if not usuario.ativo:
            print("O usuário está inativo.")
            return

        # Se passou por todas as verificações acima, realiza o empréstimo
        usuario.livros_alugados.append(livro)
        livro.disponibilidade = False
        print("Livro emprestado ao usuário.")

    def devolver_livros(self, usuario, livro):
        if livro in usuario.livros_alugados:
            # Remover o livro da lista de usuário
            # Tornar a disponibilidade do livro true
            # Mensagem de conclusão
            usuario.livros_alugados.remove(livro)
            livro.disponibilidade = True
            print(f"O Livro: {livro.titulo} foi devolvido com sucesso!")
        else:
            print("Este livro não consta como alugado por este usuário.")

    def adicionar_livros(self, livro):
        if livro not in self.livros:
            self.livros.append(livro)
            print("Livro adicionado com sucesso.")
        else:
            print("O livro já está no sistema de dados.")

    def remover_livros(self, livro):
        if livro in self.livros:
            self.livros.remove(livro)
            print(f"Livro: {livro.titulo} foi removido com sucesso.")
        else:
            print("O livro já se encontra removido")

    def adicionar_usuario(self, usuario):
        if usuario.ativo is False:
            print("Usuário não cadastrado (CPF Inválido ou Inativo).")
            return

        for u in self.usuarios:
            if u.cpf == usuario.cpf:
                print("CPF já cadastrado.")
                return

        self.usuarios.append(usuario)
        print("usuario adicionado com sucesso.")

    def remover_usuarios(self, usuario):
        if usuario in self.usuarios:
            self.usuarios.remove(usuario)
            print(f"usuario: {usuario.nome} foi removido com sucesso.")
        else:
            print("O usuario já se encontra removido")


class Midia:
    def __init__(self, genero: list, autor: str, titulo: str):
        self.genero = genero
        self.autor = autor
        self.titulo = titulo
        self.disponibilidade = True

    def sinopse(self):
        print(f"{self.titulo} - {self.autor}")
        for item in self.genero:
            print(item)


class Livro(Midia):
    def __init__(self, genero, autor, titulo, paginas):
        super().__init__(genero, autor, titulo)
        self.paginas = paginas

    def sinopse(self):
        print(f"{self.titulo} - {self.autor}")
        for item in self.genero:
            print(item)
        print(f"O livro tem {self.paginas} páginas")


class CD(Midia):
    def __init__(self, genero, autor, titulo, duracao):
        super().__init__(genero, autor, titulo)
        self.duracao = duracao

    def sinopse(self):
        print(f"{self.titulo} - {self.autor}")
        for item in self.genero:
            print(item)
        print(f"O CD tem {self.duracao} minutos de duração")


class Revista(Livro):
    def __init__(self, genero, autor, titulo, paginas):
        super().__init__(genero, autor, titulo, paginas)


# SuperClasse usuário
class Usuario:
    def __init__(self, nome, cpf):
        cpf = cpf.replace(".", "").replace("-", "")

        valido = True

        if len(cpf) != 11 or cpf == cpf[0] * 11:
            valido = False

        soma = 0
        for i in range(9):
            soma += int(cpf[i]) * (10 - i)
        dig1 = (soma * 10 % 11) % 10

        soma = 0
        for i in range(10):
            soma += int(cpf[i]) * (11 - i)
        dig2 = (soma * 10 % 11) % 10

        if dig1 != int(cpf[9]) or dig2 != int(cpf[10]):
            valido = False

        self.nome = nome
        self.cpf = cpf
        self.ativo = valido

        if not valido:
            print("CPF inválido, usuário inativo")


# SubClasse Funcionário
class Funcionario(Usuario):
    def __init__(self, nome, cpf, cargo):
        super().__init__(nome, cpf)
        self.cargo = cargo


# SubClasse Cliente
class Cliente(Usuario):
    def __init__(self, nome, cpf):
        super().__init__(nome, cpf)
        self.livros_alugados = []

    def mostrar_livros(self):
        for livro in self.livros_alugados:
            print(livro.titulo)


# --- EXECUÇÃO ---

biblioteca_municipal = Biblioteca("BMNF", 15)
livro1 = Livro(["Romance", "Realismo", "Dramaturgia"], "Machado de Assis", "A Mão e a Luva", 300)

# Correção: CPF válido para o usuário ser ativado
usuario1 = Cliente("Zezinho", "00647828160") 

cd1 = CD(["Cientifico"], "National Geographic", "A vida dos animais", 30)
revista1 = Revista(["Anime", "Herói"], "Panini", "Shonen Jump", 50)

biblioteca_municipal.adicionar_livros(livro1)

print(biblioteca_municipal)

# Correção: É necessário adicionar o usuário à biblioteca antes de emprestar
biblioteca_municipal.adicionar_usuario(usuario1) 

biblioteca_municipal.emprestar_livro(usuario1, livro1)
usuario1.mostrar_livros()
print(usuario1.nome, usuario1.cpf)
biblioteca_municipal.devolver_livros(usuario1, livro1)
livro1.sinopse()
cd1.sinopse()
revista1.sinopse()
biblioteca_municipal.remover_livros(livro1)
biblioteca_municipal.adicionar_livros(livro1)



        
