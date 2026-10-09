#1 - Peça um numero para o usuário e diga se ele é par ou ímpar
numero = int(input("Digite um número: "))
if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")
#2 - Peça um número par ao usuário e diga se ele é positivo, negativo ou zero
numero2 = float(input("\nDigite outro número: "))
if numero2 > 0:
    print("O número é positivo.")
elif numero2 < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")
#3 - Peça a um usuário a senha. Se o usuário for 'admin' E a senha for '1234', mostre 'Acesso liberado', senão mostre 'Acesso negado'
usuario = input("\nDigite o usuário: ")
senha = input("Digite a senha: ")

if usuario == 'admin' and senha == '1234':
    print("Acesso liberado")
else:
    print("Acesso negado")
#4 - Peça uma idade e informe a categoria: criança(até 11), adolescente(12 a 17), adulto(18 a 59), idoso(60 ou mais)
idade = int(input("\nDigite a sua idade: "))

if idade <= 11:
    print("Categoria: Criança")
elif idade <= 17:
    print("Categoria: Adolescente")
elif idade <= 59:
    print("Categoria: Adulto")
else:
    print("Categoria: Idoso")