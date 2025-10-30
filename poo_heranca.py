#1 Crie uma classe Usuario com atributos nome e email. Depois, crie uma classe Cliente que herde de Usuario. 
# Crie uma instancia de um cliente e acesse todos os atributos.
class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

class Cliente(Usuario):
    pass

cliente = Cliente("Lorena", "lorena@email.com")
print(cliente.nome)   
print(cliente.email)


#2 Implemente um método exibir_informacoes() na classe Usuario e herde esse método em Cliente.
#  Mostre como chamar o método herdado a partir de um objeto Cliente.
class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}, Email: {self.email}")

class Cliente(Usuario):
    pass

cliente = Cliente("Lorena", "lorena@email.com")
cliente.exibir_informacoes() 

#3 Na classe Usuario, crie um método saudacao() que retorna "Olá, usuário".
#  Na classe Cliente, sobrescreva esse método para retornar "Olá, cliente". Mostre como funciona a chamada.
class Usuario:
    def saudacao(self):
        return "Olá, usuário"

class Cliente(Usuario):
    def saudacao(self):
        return "Olá, cliente"

cliente = Cliente()
print(cliente.saudacao())  

#4 Na classe Cliente, adicione o atributo saldo. 
# Adicione um método construtor em Cliente que inicialize também os atributos de Usuario usando super().
class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

class Cliente(Usuario):
    def __init__(self, nome, email, saldo):
        super().__init__(nome, email)
        self.saldo = saldo

cliente = Cliente("Lorena", "lorena@email.com", 150.0)
print(cliente.nome, cliente.email, cliente.saldo)

#5Crie uma classe Funcionario que herda de Usuario e, em seguida, crie uma classe Gerente que herda de Funcionario. 
# Mostre como instanciar um gerente e acessar seus atributos.

class Funcionario(Usuario):
    def __init__(self, nome, email, cargo):
        super().__init__(nome, email)
        self.cargo = cargo

class Gerente(Funcionario):
    def __init__(self, nome, email, cargo, setor):
        super().__init__(nome, email, cargo)
        self.setor = setor

gerente = Gerente("fred", "fred@email.com", "Gerente", "TI")
print(gerente.nome, gerente.email, gerente.cargo, gerente.setor)


#6 Crie uma classe Autenticacao com um método login(). Crie outra classe Permissao com um método verificar_permissao().
#  Em seguida, crie uma classe Administrador que herda de ambas. Como usar os métodos herdados?
class Autenticacao:
    def login(self):
        print("Login realizado")

class Permissao:
    def verificar_permissao(self):
        print("Permissão verificada")

class Administrador(Autenticacao, Permissao):
    pass

adm = Administrador()
adm.login()
adm.verificar_permissao()


#7Usando o exemplo anterior, adicione um método status() em Autenticacao e também em Permissao. 
# Se a classe Administrador herda das duas, qual versão de status() será chamada? Use Administrador.__mro__ para mostrar a ordem.

class Autenticacao:
    def status(self):
        return "Autenticado"

class Permissao:
    def status(self):
        return "Permissão concedida"

class Administrador(Autenticacao, Permissao):
    pass

adm = Administrador()
print(adm.status()) 
print(Administrador.__mro__)
