a = 5;
b = 10;
c = 21;

print('a == b and b > c', a == b and b > c);
print('a < b or b > c', a < b or b > c);
print('not a == b', not a == b);


idade = int(input('Digite a sua idade: '));

if idade >= 18:
    print('Maior idade!');
elif idade >= 12:
    print('Infanto juvenil!');
else:
    print('Menor idade!');

