numero1 = float(input("Digite o primeiro numero:"))
numero2 = float(input("Digite o segundo numero:"))

while numero1 == numero2:
    print("Digite numeros diferentes")
    numero1 = float(input("Digite novamente o primeiro numero:"))
    numero2 = float(input("Digite novamente o segundo numero:"))

if numero1 > numero2:
    print(f"Ordem Crescente: {numero1} ---- {numero2}")
else:
    print(f"Ordem Crescente: {numero2} ---- {numero1}")
