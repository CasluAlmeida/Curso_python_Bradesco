# nome = input('Digite seu nome: ')
# idade = int(input('Digite sua idade: '))
# salario = float(input('Digite seu salário: '))

nome = Matheus
idade = 18
salario = 4000.00

print(nome)
print(idade)
print(salario)


# Operadores aritméticos
#
#
# Operação	Símbolo
# Adição	+
# Subtração	-
# Multiplicação	*
# Divisão Real	/
# Divisão Inteiro	//
# Exponenciação	**
# Resto da Divisão	%


n1 = 115
n2 = 40

total = n1 % n2

print(total)


# Operadores relacionais
#
#
# Descrição	Símbolo
# Igual a	==
# Diferente de	!=
# Maior que	>
# Menor que	<
# Maior ou igual a	>=
# Menor ou igual a	<=

teste_relacional = n1 <= n2

print(teste_relacional)

# Operadores lógicos
#
#
# Algoritmo	Python
# E	and
# OU	or
# Não	not

operador_logico_and = n1 > n2 and n1 != n2
operador_logico_or = n1 > n2 or n1 < n2
operador_logico_not = not n1 > n2

print(operador_logico_and)
print(operador_logico_or)
print(operador_logico_not)