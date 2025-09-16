# EXERCICIO 1 
# Na classe, ContaBancaria, converta saldo para uma atributo privado. 
# Crie um método setter e um getter para acessar e modificar essa atributo,
# seguindo uma regra lógica (Ex: saldo não pode ser negativo)

class ContaBancaria:
    def _init_(self, saldo_inicial=0):
        if saldo_inicial >= 0:
            self.__saldo = saldo_inicial
        else:
            self.__saldo = 0

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, valor):
        if valor >= 0:
            self.__saldo = valor
        else:
            print("Erro: o saldo não pode ser negativo.")
if __name__ == "_main_":
    conta = ContaBancaria(100)
    print(conta.get_saldo())

#     EXERCICIO 2
# Crie uma classe, Pessoa, que tenha os atributos: nome, data de nascimento, cpf, identidade. Deixe os 
# atributos cpf e identidade como privado e monte os métodos setters 
# e getters para acessar e editar os valores

class Pessoa:
    def _init_(self, nome, data_nascimento, cpf, identidade):
        # públicos
        self.nome = nome
        self.data_nascimento = data_nascimento
        # privados
        self.__cpf = cpf
        self.__identidade = identidade

    # Getters (ler valores privados)
    def get_cpf(self):
        return self.__cpf

    def get_identidade(self):
        return self.__identidade

    # Setters (alterar valores privados)
    def set_cpf(self, novo_cpf):
        self.__cpf = novo_cpf

    def set_identidade(self, nova_identidade):
        self.__identidade = nova_identidade

# Testando a classe
if __name__ == "__main__":
    pessoa = Pessoa("Nayara", "22/11/2007", "123.456.789-00", "1234567")
    print(pessoa.nome)           
    print(pessoa.data_nascimento) 
    print(pessoa.get_cpf())       
    print(pessoa.get_identidade()) 
    pessoa.set_cpf("987.654.321-00")
    print(pessoa.get_cpf())        
