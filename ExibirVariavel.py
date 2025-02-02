coodigo = 15
nome_completo = input('Digite um nome completo: ')
idade = int(input('Digite sua idade: '))
salario = float(input('Digite seu salário: '))
ativo = True

print('Código: %d ' % coodigo)

tipo = type (nome_completo)
print(tipo)
print('O nome digitado foi', nome_completo)

tipo_idade = type (idade)
print(tipo_idade)
print('A idade digitada foi', idade)

tipo_salario = type (salario)
print(tipo_salario)
print('O salário digitado foi', salario)

print('Ativo: %r '% ativo)

