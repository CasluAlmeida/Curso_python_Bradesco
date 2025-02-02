notaA = float(input('Digite a primeira nota: '));
notaB = float(input('Digite a segunda nota: '));

# Calcular media
media_final = (notaA + notaB) / 2;

# Validação da média
if media_final >= 7.0:
    print('Você foi aprovado com a nota', media_final);
    # print('A média: %.1f - Aprovado!' % media_final)
else:
    print('Você foi reprovado com a nota', media_final);
    # print('A média: %.1f - Reprovado!' % media_final)