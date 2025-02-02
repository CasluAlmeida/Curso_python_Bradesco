a = input('Digite um valor para A: ')
b = input('Digite um valor para B: ')

if a > b:
    aux = a;
    a = b;
    b = aux;

print('O valor atualizado de A é ', a)
print('O valor atualizado de B é ', b)