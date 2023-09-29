#Questão 11
idade = int(input("Digite sua idade:"))
mes = int(input("Digite o mes do seu nascimento:"))
dia = int(input("Digite o dia do seu nascimento:"))

idadeEmDias = idade * 365
mesEmDias = mes * 30
diasTotais = idadeEmDias + mesEmDias + dia

print("Sua idade expressa em dias:",diasTotais)
