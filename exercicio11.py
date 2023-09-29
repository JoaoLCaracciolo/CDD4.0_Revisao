quantMaca = int(input("Digite a quantidade de maçãs:"))

if quantMaca < 12:
    preco = quantMaca * 1.30
else:
    preco = quantMaca * 1

print(f"---MAÇÃS---\nQuantidade de maçãs:{quantMaca}\nPreço:R${preco}")