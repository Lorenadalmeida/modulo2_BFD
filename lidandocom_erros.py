#1 Escreva um programa que peça ao usuário para digitar um número. 
# Trate o erro caso ele digite algo que não seja um número inteiro.

try:
    numero = int(input("Digite um número inteiro: "))
    print("Você digitou:", numero)
except ValueError:
    print("Erro: você não digitou um número inteiro!")

#2 Peça ao usuário dois números e tente multiplicá-los. 
# Se o usuário digitar algo inválido, exiba uma mensagem de erro.

try:
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    print("Resultado:", n1 * n2)
except ValueError:
    print("Erro: você digitou um valor inválido!")


#3 Crie um programa que peça ao usuário um número inteiro. 
# Se a conversão for bem-sucedida, mostre uma mensagem usando o bloco else.

try:
    numero = int(input("Digite um número inteiro: "))
except ValueError:
    print("Erro: valor inválido!")
else:
    print("Número válido digitado:", numero)


#4 Implemente um programa que abra um arquivo chamado dados.txt (não precisa existir). 
# Use try e finally para garantir que uma mensagem de "Encerrando programa" seja sempre exibida.

try:
    arquivo = open("dados.txt", "a")  # cria ou abre
    arquivo.write("Salvando algo...\n")
finally:
    print("Encerrando programa")
    arquivo.close()


#5 Crie uma função dividir(a, b) que lance (raise) uma exceção ZeroDivisionError se 
# b for igual a zero. Caso contrário, retorne o resultado da divisão.

def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("Divisão por zero não permitida!")
    return a / b
try:
    print(dividir(10, 2))
    print(dividir(5, 0))
except ZeroDivisionError as e:
    print("Erro:", e)


#6 Crie uma exceção personalizada chamada IdadeInvalidaError. 
# Depois, crie uma função cadastrar_idade(idade) que lance essa exceção caso a idade seja negativa.

class IdadeInvalidaError(Exception):
    pass

def cadastrar_idade(idade):
    if idade < 0:
        raise IdadeInvalidaError("Idade não pode ser negativa!")
    print("Idade cadastrada:", idade)

try:
    cadastrar_idade(-5)
except IdadeInvalidaError as e:
    print("Erro:", e)


#7 Peça ao usuário dois números e divida o primeiro pelo segundo. Trate dois tipos de erro:
# - ValueError se o usuário digitar algo inválido
# - ZeroDivisionError se tentar dividir por zero

try:
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    print("Resultado:", n1 / n2)
except ValueError:
    print("Erro: valor inválido!")
except ZeroDivisionError:
    print("Erro: divisão por zero!")

# 8Crie um programa que peça ao usuário um número inteiro e verifique se ele é par. Use:
# - try para a conversão,
# - else para verificar se é par ou ímpar,
# - finally para exibir "Fim do programa".

try:
    numero = int(input("Digite um número inteiro: "))
except ValueError:
    print("Erro: valor inválido!")
else:
    if numero % 2 == 0:
        print("Número par")
    else:
        print("Número ímpar")
finally:
    print("Fim do programa")


# 9Crie uma função sacar(saldo, valor) que:
# - Lance (raise) uma exceção personalizada SaldoInsuficienteError se o valor for maior que o saldo.
# - Caso contrário, retorne o novo saldo. Teste a função dentro de um try-except 
# e exiba uma mensagem apropriada ao usuário.

def sacar(saldo, valor):
    if valor > saldo:
        raise ValueError("Saldo insuficiente!")
    return saldo - valor

try:
    novo_saldo = sacar(100, 150)
    print("Novo saldo:", novo_saldo)
except ValueError as e:
    print("Erro:", e)

