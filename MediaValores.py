qtd = 0;
soma = 0;
media = 0;
valor = float(input('Digite um valor: '));

while (valor > 0.0):
    soma = soma + valor;
    qtd = qtd + 1;
    # Entrada de valores
    valor = float(input('Digite um valor: '));

media = soma / qtd;
print(f'\n Total da Soma: {soma}');
print(f'\n Quantidade de valores digitados: {qtd}');
print(f'\n Média dos valores: {media}');