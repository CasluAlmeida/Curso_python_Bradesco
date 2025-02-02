# Notas das três primeiras provas
n1 = 8.0;
n2 = 10.0;
n3 = 8.5;
n4 = 8;

# Calculando a média das três provas
media_tres_provas = (n1 + n2 + n3) / 3;

# Considerando que essas provas valem 40% (peso 0.4)
media_parcial = media_tres_provas * 0.4;

# Considerando que essa prova vale 60% (peso 0.6)
media_parcial_n4 = n4 * 0.6;

# Calculando media final
media_final = media_parcial + media_parcial_n4;

# Exibindo a média parcial
print(f"Média parcial (40%): {media_parcial:.2f}");

# Exibindo a média final
print(f"Média final (100%): {media_final:.2f}");

