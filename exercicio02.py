soma = 0
for i in range(4):
    numero = int(input(f"Digite o {i+1}º numero:"))
    soma += numero

media = soma/4

print(f"A soma: {soma}\nA media: {media}")
